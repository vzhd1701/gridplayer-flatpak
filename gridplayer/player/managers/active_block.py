from pathlib import Path

from PyQt5.QtCore import QEvent, pyqtSignal

from gridplayer.player.managers.base import ManagerBase
from gridplayer.utils.qt import is_modal_open, translate
from gridplayer.widgets.video_block import VideoBlock


class ActiveBlockManager(ManagerBase):
    active_block_change = pyqtSignal(VideoBlock)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._ctx.active_block = None

    @property
    def event_map(self):
        return {
            QEvent.MouseMove: self.update_active_under_mouse,
            QEvent.MouseButtonPress: self.update_active_under_mouse,
            QEvent.MouseButtonRelease: self.update_active_under_mouse,
            QEvent.NonClientAreaMouseMove: self.update_active_reset,
            QEvent.NonClientAreaMouseButtonPress: self.update_active_reset,
            QEvent.Drop: self.update_active_under_mouse,
            QEvent.DragMove: self.update_active_under_mouse,
        }

    @property
    def commands(self):
        return {
            "active": self.cmd_active,
            "is_active_runtime_param_set_to": self.is_active_runtime_param_set_to,
            "is_active_param_set_to": self.is_active_param_set_to,
            "is_active_initialized": self.is_active_initialized,
            "is_active_seekable": self.is_active_seekable,
            "is_active_live": self.is_active_live,
            "is_active_multistream": self.is_active_multistream,
            "is_active_local_file": self.is_active_local_file,
            "is_active_has_audio": self.is_active_has_audio,
            "is_active_has_video": self.is_active_has_video,
            "menu_generator_stream_quality": self.menu_generator_stream_quality,
            "menu_generator_video_track": self.menu_generator_video_track,
            "menu_generator_audio_track": self.menu_generator_audio_track,
            "next_active": self.next_active,
            "previous_active": self.previous_active,
        }

    @property
    def is_no_active_block(self):
        return self._ctx.active_block is None

    def cmd_active(self, command, *args):
        if self.is_no_active_block:
            return None

        is_inactive_command = command in {"switch_stream_quality", "reload", "close"}

        if not is_inactive_command and not self.is_active_initialized():
            return None

        return getattr(self._ctx.active_block, command)(*args)

    def is_active_initialized(self):
        if self.is_no_active_block:
            return False

        return self._ctx.active_block.is_video_initialized

    def is_active_param_set_to(self, param_name, param_value):
        if self.is_no_active_block:
            return False

        active_video_param = getattr(self._ctx.active_block.video_params, param_name)

        return active_video_param == param_value

    def is_active_runtime_param_set_to(self, param_name, param_value):
        if self.is_no_active_block:
            return False

        active_video_param = getattr(self._ctx.active_block, param_name)

        return active_video_param == param_value

    def is_active_seekable(self):
        if not self.is_active_initialized():
            return False

        return not self._ctx.active_block.is_live

    def is_active_live(self):
        if not self.is_active_initialized():
            return False

        return self._ctx.active_block.is_live

    def is_active_local_file(self):
        if not self.is_active_initialized():
            return False

        return isinstance(self._ctx.active_block.video_params.uri, Path)

    def is_active_has_audio(self):
        if not self.is_active_initialized():
            return False

        return bool(self._ctx.active_block.audio_tracks)

    def is_active_has_video(self):
        if not self.is_active_initialized():
            return False

        return bool(self._ctx.active_block.video_tracks)

    def is_active_multistream(self):
        if self.is_no_active_block:
            return False

        return len(self._ctx.active_block.streams) > 1

    def menu_generator_stream_quality(self):
        if self.is_no_active_block:
            return []

        video_streams = self._ctx.active_block.streams.video_streams
        audio_only_streams = self._ctx.active_block.streams.audio_only_streams

        streams = [
            _stream_menu_item(quality)
            for quality, stream in reversed(list(video_streams.items()))
        ]

        audio_only_streams = [
            _stream_menu_item(quality)
            for quality, stream in reversed(list(audio_only_streams.items()))
        ]

        if audio_only_streams:
            if streams:
                streams += ["---"]
            streams += audio_only_streams

        return streams

    def menu_generator_video_track(self):
        if self.is_no_active_block or not self._ctx.active_block.video_tracks:
            return {}

        menu = [
            {
                "title": translate("Actions", "Disable Video"),
                "icon": "empty",
                "func": ("active", "set_video_track", -1),
                "check_if": ("is_active_param_set_to", "video_track_id", -1),
                "show_if": "is_active_initialized",
            }
        ]

        menu += [
            {
                "title": track.info,
                "icon": "empty",
                "func": ("active", "set_video_track", track_id),
                "check_if": ("is_active_param_set_to", "video_track_id", track_id),
                "show_if": "is_active_initialized",
            }
            for track_id, track in self._ctx.active_block.video_tracks.items()
        ]

        return menu

    def menu_generator_audio_track(self):
        if self.is_no_active_block or not self._ctx.active_block.audio_tracks:
            return {}

        menu = [
            {
                "title": translate("Actions", "Disable Audio"),
                "icon": "empty",
                "func": ("active", "set_audio_track", -1),
                "check_if": ("is_active_param_set_to", "audio_track_id", -1),
                "show_if": "is_active_initialized",
            }
        ]

        menu += [
            {
                "title": track.info,
                "icon": "empty",
                "func": ("active", "set_audio_track", track_id),
                "check_if": ("is_active_param_set_to", "audio_track_id", track_id),
                "show_if": "is_active_initialized",
            }
            for track_id, track in self._ctx.active_block.audio_tracks.items()
        ]

        return menu

    def update_active_under_mouse(self):
        if is_modal_open():
            return

        self._update_active_block(self._get_hover_video_block())
        self.cmd_active("show_overlay")

    def update_active_reset(self):
        if is_modal_open():
            return

        self._update_active_block(None)

    def next_active(self):
        if self.is_no_active_block:
            next_active = self._ctx.video_blocks[0]
        else:
            next_block_index = (
                self._ctx.video_blocks.index(self._ctx.active_block) + 1
            ) % len(self._ctx.video_blocks)
            next_active = self._ctx.video_blocks[next_block_index]

        self._update_active_block(next_active)
        self.cmd_active("show_overlay")

    def previous_active(self):
        if self.is_no_active_block:
            next_active = self._ctx.video_blocks[-1]
        else:
            next_block_index = (
                self._ctx.video_blocks.index(self._ctx.active_block) - 1
            ) % len(self._ctx.video_blocks)
            next_active = self._ctx.video_blocks[next_block_index]

        self._update_active_block(next_active)
        self.cmd_active("show_overlay")

    def _update_active_block(self, new_active_block):
        old_active_block = self._ctx.active_block
        self._ctx.active_block = new_active_block

        if self._ctx.active_block is not None:
            self._ctx.active_block.is_active = True

        if self._ctx.active_block != old_active_block:
            if old_active_block is not None:
                old_active_block.is_active = False

            self.active_block_change.emit(self._ctx.active_block)

    def _get_hover_video_block(self):
        visible_blocks_under_cursor = (
            v for v in self._ctx.video_blocks if v.isVisible() and v.is_under_cursor()
        )

        return next(visible_blocks_under_cursor, None)

    def _get_current_cursor_pos(self):
        parent = self.parent()
        return parent.mapFromGlobal(parent.cursor().pos())


def _stream_menu_item(quality: str):
    return {
        "title": quality,
        "icon": "empty",
        "func": ("active", "switch_stream_quality", quality),
        "check_if": ("is_active_param_set_to", "stream_quality", quality),
        "show_if": "is_active_multistream",
    }
