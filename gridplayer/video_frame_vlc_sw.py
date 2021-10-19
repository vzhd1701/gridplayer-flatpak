import contextlib
import logging
from multiprocessing import Array, Lock, Value

from gridplayer.params_vlc import pre_import_embed_vlc

pre_import_embed_vlc()
import vlc
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QImage, QPainter, QPixmap
from PyQt5.QtWidgets import QFrame, QGraphicsPixmapItem, QStackedLayout

from gridplayer.params_static import VideoAspect
from gridplayer.utils.multiprocessing import SafeSharedMemory, releasing
from gridplayer.video_frame_vlc_base import (
    InstanceProcessVLC,
    VlcPlayerThreaded,
    VLCVideoDriverThreaded,
)


class ImageDecoder:
    def __init__(self, shared_memory, frame_ready_cb=None):
        super().__init__()

        self.is_paused = True

        self.lock_cb = self.get_libvlc_lock_callback()
        self.unlock_cb = self.get_libvlc_unlock_callback()

        self._stopped = False

        self._row_size = None
        self._width = None
        self._height = None

        self._shared_memory = shared_memory
        self._frame_ready_cb = frame_ready_cb

        self._prev_frame_head = None

    def set_frame(self, width, height):
        self._width = width
        self._height = height

        self._row_size = self._width * 4

        buf_size = self._height * self._row_size

        self._shared_memory.allocate(buf_size)

    def attach_media_player(self, media_player):
        media_player.video_set_callbacks(self.lock_cb, self.unlock_cb, None, None)
        media_player.video_set_format("RV32", self._width, self._height, self._row_size)

    def get_libvlc_lock_callback(self):
        @vlc.CallbackDecorators.VideoLockCb
        def _cb(opaque, planes):
            self._shared_memory.acquire()
            planes[0] = self._shared_memory.get_ptr()

        return _cb

    def get_libvlc_unlock_callback(self):
        @vlc.CallbackDecorators.VideoUnlockCb
        def _cb(opaque, picta, planes):
            with releasing(self._shared_memory):
                if self._stopped:
                    return

                # Callback is firing while on pause,
                # so check if the frame content actually changed
                if self.is_paused:
                    new_frame_head = bytes(self._shared_memory.get_memory_buf()[:1024])
                    if new_frame_head == self._prev_frame_head:
                        return
                    else:
                        self._prev_frame_head = new_frame_head

                self._frame_ready_cb()

        return _cb

    def stop(self):
        self._stopped = True

        # make sure that memory lock released in case it was locked mid-callback
        with contextlib.suppress(ValueError):
            self._shared_memory.release()

        self._shared_memory.close()
        self._shared_memory.unlink()


class InstanceProcessVLCSW(InstanceProcessVLC):
    def __init__(
        self,
        players_per_instance,
        pm_callback_pipe,
        pm_log_queue,
        log_level,
        log_level_vlc,
    ):
        super().__init__(
            players_per_instance,
            pm_callback_pipe,
            pm_log_queue,
            log_level,
            log_level_vlc,
        )

        # shared data multiprocess
        self._memory_locks = [
            {"lock": Lock(), "is_busy": Value("i", 0), "player_id": Array("c", 16)}
            for _ in range(players_per_instance)
        ]

        self._vlc_options = ["--vout=vdummy"]

    def init_player_shared_data(self, player_id):
        available_locks = (l for l in self._memory_locks if l["is_busy"].value == 0)

        player_lock = next(available_locks)

        player_lock["is_busy"].value = 1
        player_lock["player_id"].value = player_id.encode()

        self._players_shared_data[player_id] = self.get_player_shared_memory(player_id)

    def release_player_shared_data(self, player_id):
        player_lock = self.get_player_lock(player_id)

        player_lock["player_id"].value = b""
        player_lock["is_busy"].value = 0

    def get_player_lock(self, player_id):
        return next(
            l for l in self._memory_locks if l["player_id"].value == player_id.encode()
        )

    def get_player_shared_memory(self, player_id):
        player_lock = self.get_player_lock(player_id)
        return SafeSharedMemory(player_id, player_lock["lock"])

    def new_player(self, player_id, init_data, pipe):
        init_data["shared_memory"] = self.get_player_shared_memory(player_id)

        player = PlayerProcessSingleVLCSW(
            player_id,
            self._vlc_instance,
            self.release_player,
            init_data,
            self.crash,
            pipe,
        )
        self._players[player_id] = player


class PlayerProcessSingleVLCSW(VlcPlayerThreaded):
    def __init__(
        self, player_id, vlc_instance, release_callback, init_data, crash_func, pipe
    ):
        VlcPlayerThreaded.__init__(self, vlc_instance, crash_func, pipe)

        self.id = player_id
        self.release_callback = release_callback

        self.shared_memory = init_data["shared_memory"]
        self.decoder = None
        self.media_options.append("avcodec-hw=none")

        self.start()

    def init_player(self):
        super().init_player()

        self.decoder = ImageDecoder(self.shared_memory, self.ready_signal)

    def ready_signal(self):
        self.cmd_send("process_image")

    def cleanup(self):
        super().cleanup()

        self.decoder.stop()

        self.release_callback(self.id)

    def cleanup_final(self):
        self.cmd_loop_terminate()

    def load_video_player(self):
        width, height = self.video_dimensions

        self.decoder.set_frame(width, height)
        self.decoder.attach_media_player(self.media_player)

        self.cmd_send("init_frame", width, height)

        super().load_video_player()

    def play(self):
        self.decoder.is_paused = False

        super().play()

    def set_pause(self, is_paused):
        self.decoder.is_paused = is_paused

        super().set_pause(is_paused)


class VideoDriverVLCSW(VLCVideoDriverThreaded):
    set_dummy_frame_sig = QtCore.pyqtSignal()
    image_ready_sig = QtCore.pyqtSignal()

    def __init__(self, image_dest, process_manager, parent=None):
        VLCVideoDriverThreaded.__init__(self, parent=parent)

        self._width = None
        self._height = None

        self._image_dest = image_dest
        self._shared_memory = None

        self._pix = None

        self.set_dummy_frame_sig.connect(self.set_dummy_frame)
        self.image_ready_sig.connect(self.image_ready)

        self.player = process_manager.init_player({}, self.cmd_child_pipe())

        self.log = logging.getLogger("VideoDriverVLCSW")

    def init_frame(self, width, height):
        self._shared_memory = self.player.get_player_shared_data()

        self._width = width
        self._height = height

        self.set_dummy_frame_sig.emit()

    def set_dummy_frame(self):
        pix = QPixmap(self._width, self._height)
        pix.fill(Qt.black)
        self._image_dest.setPixmap(pix)

    def process_image(self):
        if self._shared_memory is None:
            return

        try:
            with self._shared_memory:
                px = QImage(
                    self._shared_memory.get_memory_buf(),
                    self._width,
                    self._height,
                    QImage.Format_RGB32,
                )
        except AttributeError as e:
            # Very rare race condition
            self.log.warning("Shared memory is cleared already")
            return

        self._pix = QPixmap.fromImage(px)

        self.image_ready_sig.emit()

    def image_ready(self):
        self._image_dest.setPixmap(self._pix)

    def cleanup(self):
        if self._shared_memory is not None:
            shared_memory = self._shared_memory
            self._shared_memory = None

            shared_memory.close()

        super().cleanup()

        self.player.cleanup()


class VideoFrameVLCSW(QtWidgets.QWidget):
    time_changed = QtCore.pyqtSignal(int)
    video_ready = QtCore.pyqtSignal()
    error = QtCore.pyqtSignal()
    crash = QtCore.pyqtSignal(str)

    def __init__(self, process_manager, parent=None):
        super().__init__(parent)

        self._aspect = Qt.KeepAspectRatio
        self._scale = 1.0

        self.is_video_initialized = False

        self.setup_ui()

        self.video_driver = VideoDriverVLCSW(self._videoitem, process_manager, self)
        self.video_driver.time_changed.connect(self.time_change_emit)
        self.video_driver.load_finished.connect(self.load_video_finish)
        self.video_driver.error.connect(self.error_state)
        self.video_driver.crash.connect(self.crash_driver)

    def setup_ui(self):
        self.setWindowFlags(Qt.WindowTransparentForInput)
        self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
        self.setMouseTracking(True)

        QStackedLayout(self)
        self.layout().setSpacing(0)
        self.layout().setContentsMargins(0, 0, 0, 0)

        # =========

        self._scene = QtWidgets.QGraphicsScene(self)
        self._videoitem = QGraphicsPixmapItem()
        self._videoitem.setTransformationMode(Qt.SmoothTransformation)
        self._videoitem.setShapeMode(QGraphicsPixmapItem.BoundingRectShape)
        self._scene.addItem(self._videoitem)

        self._gv = QtWidgets.QGraphicsView(self._scene, self)
        self._gv.setBackgroundBrush(QBrush(Qt.black))
        self._gv.setWindowFlags(Qt.WindowTransparentForInput)
        self._gv.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
        self._gv.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self._gv.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self._gv.setFrameStyle(QFrame.NoFrame)
        self._gv.setLineWidth(0)
        self._gv.setRenderHints(
            QPainter.Antialiasing
            | QPainter.SmoothPixmapTransform
            | QPainter.TextAntialiasing
            | QPainter.HighQualityAntialiasing
        )

        # =========

        self.layout().addWidget(self._gv)

    def resizeEvent(self, event):
        self.adjust_view()

    def showEvent(self, event):
        self.adjust_view()

    def crash_driver(self, exception_txt):
        self.crash.emit(exception_txt)

    def error_state(self):
        self.cleanup()

        self.error.emit()

    def cleanup(self):
        # need to remove it before cleanup to avoid occasional segmentation fault
        self._scene.removeItem(self._videoitem)

        self.video_driver.cleanup()

    def adjust_view(self):
        self._gv.fitInView(self._videoitem, self._aspect)
        self._gv.scale(self._scale + 0.05, self._scale + 0.05)

    def time_change_emit(self, new_time):
        self.time_changed.emit(new_time)

    def load_video(self, file_path):
        self.video_driver.load_video(file_path)

    def load_video_finish(self):
        self.is_video_initialized = True

        self.video_ready.emit()

    def play(self):
        self.video_driver.play()

    def set_pause(self, is_paused):
        self.video_driver.set_pause(is_paused)

    def set_time(self, seek_ms):
        self.video_driver.set_time(seek_ms)

    def set_playback_rate(self, rate):
        self.video_driver.set_playback_rate(rate)

    def get_ms_per_frame(self):
        return self.video_driver.get_ms_per_frame()

    def audio_set_mute(self, is_muted):
        self.video_driver.audio_set_mute(is_muted)

    def audio_set_volume(self, volume):
        self.video_driver.audio_set_volume(volume)

    def set_aspect_ratio(self, aspect: VideoAspect):
        aspect_map = {
            VideoAspect.FIT: Qt.KeepAspectRatioByExpanding,
            VideoAspect.STRETCH: Qt.IgnoreAspectRatio,
            VideoAspect.NONE: Qt.KeepAspectRatio,
        }

        self._aspect = aspect_map[aspect]

        self.adjust_view()

    def set_scale(self, scale):
        self._scale = scale

        self.adjust_view()

    @property
    def length(self):
        return self.video_driver.length
