from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(442, 541)
        self.lay_main = QtWidgets.QVBoxLayout(SettingsDialog)
        self.lay_main.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.lay_main.setObjectName("lay_main")
        self.lay_body = QtWidgets.QHBoxLayout()
        self.lay_body.setObjectName("lay_body")
        self.lay_left_column = QtWidgets.QVBoxLayout()
        self.lay_left_column.setObjectName("lay_left_column")
        self.lay_section_player = QtWidgets.QVBoxLayout()
        self.lay_section_player.setObjectName("lay_section_player")
        self.section_player = QtWidgets.QLabel(SettingsDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.section_player.setFont(font)
        self.section_player.setObjectName("section_player")
        self.lay_section_player.addWidget(self.section_player)
        self.playerPauseBackgroundVideos = QtWidgets.QCheckBox(SettingsDialog)
        self.playerPauseBackgroundVideos.setObjectName("playerPauseBackgroundVideos")
        self.lay_section_player.addWidget(self.playerPauseBackgroundVideos)
        self.playerPauseWhenMinimized = QtWidgets.QCheckBox(SettingsDialog)
        self.playerPauseWhenMinimized.setObjectName("playerPauseWhenMinimized")
        self.lay_section_player.addWidget(self.playerPauseWhenMinimized)
        self.playerInhibitScreensaver = QtWidgets.QCheckBox(SettingsDialog)
        self.playerInhibitScreensaver.setObjectName("playerInhibitScreensaver")
        self.lay_section_player.addWidget(self.playerInhibitScreensaver)
        self.playerOneInstance = QtWidgets.QCheckBox(SettingsDialog)
        self.playerOneInstance.setObjectName("playerOneInstance")
        self.lay_section_player.addWidget(self.playerOneInstance)
        self.lay_left_column.addLayout(self.lay_section_player)
        self.lay_section_playlist = QtWidgets.QVBoxLayout()
        self.lay_section_playlist.setObjectName("lay_section_playlist")
        self.section_playlist = QtWidgets.QLabel(SettingsDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.section_playlist.setFont(font)
        self.section_playlist.setObjectName("section_playlist")
        self.lay_section_playlist.addWidget(self.section_playlist)
        self.playlistSaveWindow = QtWidgets.QCheckBox(SettingsDialog)
        self.playlistSaveWindow.setObjectName("playlistSaveWindow")
        self.lay_section_playlist.addWidget(self.playlistSaveWindow)
        self.playlistSavePosition = QtWidgets.QCheckBox(SettingsDialog)
        self.playlistSavePosition.setObjectName("playlistSavePosition")
        self.lay_section_playlist.addWidget(self.playlistSavePosition)
        self.playlistSaveState = QtWidgets.QCheckBox(SettingsDialog)
        self.playlistSaveState.setObjectName("playlistSaveState")
        self.lay_section_playlist.addWidget(self.playlistSaveState)
        self.playlistSeekSync = QtWidgets.QCheckBox(SettingsDialog)
        self.playlistSeekSync.setObjectName("playlistSeekSync")
        self.lay_section_playlist.addWidget(self.playlistSeekSync)
        self.playlistTrackChanges = QtWidgets.QCheckBox(SettingsDialog)
        self.playlistTrackChanges.setObjectName("playlistTrackChanges")
        self.lay_section_playlist.addWidget(self.playlistTrackChanges)
        self.lay_left_column.addLayout(self.lay_section_playlist)
        self.lay_section_grid = QtWidgets.QVBoxLayout()
        self.lay_section_grid.setObjectName("lay_section_grid")
        self.section_grid = QtWidgets.QLabel(SettingsDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.section_grid.setFont(font)
        self.section_grid.setObjectName("section_grid")
        self.lay_section_grid.addWidget(self.section_grid)
        self.lay_gridMode = QtWidgets.QHBoxLayout()
        self.lay_gridMode.setObjectName("lay_gridMode")
        self.gridModeLabel = QtWidgets.QLabel(SettingsDialog)
        self.gridModeLabel.setObjectName("gridModeLabel")
        self.lay_gridMode.addWidget(self.gridModeLabel)
        self.gridMode = QtWidgets.QComboBox(SettingsDialog)
        self.gridMode.setObjectName("gridMode")
        self.lay_gridMode.addWidget(self.gridMode)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.lay_gridMode.addItem(spacerItem)
        self.lay_section_grid.addLayout(self.lay_gridMode)
        self.lay_gridSize = QtWidgets.QHBoxLayout()
        self.lay_gridSize.setObjectName("lay_gridSize")
        self.gridSize = QtWidgets.QSpinBox(SettingsDialog)
        self.gridSize.setObjectName("gridSize")
        self.lay_gridSize.addWidget(self.gridSize)
        self.gridSizeLabel = QtWidgets.QLabel(SettingsDialog)
        self.gridSizeLabel.setObjectName("gridSizeLabel")
        self.lay_gridSize.addWidget(self.gridSizeLabel)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.lay_gridSize.addItem(spacerItem1)
        self.lay_section_grid.addLayout(self.lay_gridSize)
        self.gridFit = QtWidgets.QCheckBox(SettingsDialog)
        self.gridFit.setObjectName("gridFit")
        self.lay_section_grid.addWidget(self.gridFit)
        self.lay_left_column.addLayout(self.lay_section_grid)
        self.lay_section_video_defaults = QtWidgets.QVBoxLayout()
        self.lay_section_video_defaults.setObjectName("lay_section_video_defaults")
        self.section_video_defaults = QtWidgets.QLabel(SettingsDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.section_video_defaults.setFont(font)
        self.section_video_defaults.setObjectName("section_video_defaults")
        self.lay_section_video_defaults.addWidget(self.section_video_defaults)
        self.lay_aspect = QtWidgets.QHBoxLayout()
        self.lay_aspect.setObjectName("lay_aspect")
        self.videoAspectLabel = QtWidgets.QLabel(SettingsDialog)
        self.videoAspectLabel.setObjectName("videoAspectLabel")
        self.lay_aspect.addWidget(self.videoAspectLabel)
        self.videoAspect = QtWidgets.QComboBox(SettingsDialog)
        self.videoAspect.setObjectName("videoAspect")
        self.lay_aspect.addWidget(self.videoAspect)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.lay_aspect.addItem(spacerItem2)
        self.lay_section_video_defaults.addLayout(self.lay_aspect)
        self.lay_repeat = QtWidgets.QHBoxLayout()
        self.lay_repeat.setObjectName("lay_repeat")
        self.repeatModeLabel = QtWidgets.QLabel(SettingsDialog)
        self.repeatModeLabel.setObjectName("repeatModeLabel")
        self.lay_repeat.addWidget(self.repeatModeLabel)
        self.repeatMode = QtWidgets.QComboBox(SettingsDialog)
        self.repeatMode.setObjectName("repeatMode")
        self.lay_repeat.addWidget(self.repeatMode)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.lay_repeat.addItem(spacerItem3)
        self.lay_section_video_defaults.addLayout(self.lay_repeat)
        self.videoRandomLoop = QtWidgets.QCheckBox(SettingsDialog)
        self.videoRandomLoop.setObjectName("videoRandomLoop")
        self.lay_section_video_defaults.addWidget(self.videoRandomLoop)
        self.videoPaused = QtWidgets.QCheckBox(SettingsDialog)
        self.videoPaused.setObjectName("videoPaused")
        self.lay_section_video_defaults.addWidget(self.videoPaused)
        self.videoMuted = QtWidgets.QCheckBox(SettingsDialog)
        self.videoMuted.setObjectName("videoMuted")
        self.lay_section_video_defaults.addWidget(self.videoMuted)
        self.lay_left_column.addLayout(self.lay_section_video_defaults)
        spacerItem4 = QtWidgets.QSpacerItem(
            0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.lay_left_column.addItem(spacerItem4)
        self.lay_body.addLayout(self.lay_left_column)
        self.lay_right_column = QtWidgets.QVBoxLayout()
        self.lay_right_column.setObjectName("lay_right_column")
        self.languageBox = QtWidgets.QGroupBox(SettingsDialog)
        self.languageBox.setObjectName("languageBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.languageBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.language = QtWidgets.QComboBox(self.languageBox)
        self.language.setObjectName("language")
        self.verticalLayout.addWidget(self.language)
        self.lay_right_column.addWidget(self.languageBox)
        self.playerVideoDriverBox = QtWidgets.QGroupBox(SettingsDialog)
        self.playerVideoDriverBox.setObjectName("playerVideoDriverBox")
        self.lay_playerVideoDriverBox = QtWidgets.QVBoxLayout(self.playerVideoDriverBox)
        self.lay_playerVideoDriverBox.setObjectName("lay_playerVideoDriverBox")
        self.playerVideoDriver = QtWidgets.QComboBox(self.playerVideoDriverBox)
        self.playerVideoDriver.setObjectName("playerVideoDriver")
        self.lay_playerVideoDriverBox.addWidget(self.playerVideoDriver)
        self.lay_playerVideoDriverPlayers = QtWidgets.QHBoxLayout()
        self.lay_playerVideoDriverPlayers.setObjectName("lay_playerVideoDriverPlayers")
        self.playerVideoDriverPlayersLabel = QtWidgets.QLabel(self.playerVideoDriverBox)
        self.playerVideoDriverPlayersLabel.setObjectName(
            "playerVideoDriverPlayersLabel"
        )
        self.lay_playerVideoDriverPlayers.addWidget(self.playerVideoDriverPlayersLabel)
        self.playerVideoDriverPlayers = QtWidgets.QSpinBox(self.playerVideoDriverBox)
        self.playerVideoDriverPlayers.setObjectName("playerVideoDriverPlayers")
        self.lay_playerVideoDriverPlayers.addWidget(self.playerVideoDriverPlayers)
        self.lay_playerVideoDriverPlayers.setStretch(0, 1)
        self.lay_playerVideoDriverBox.addLayout(self.lay_playerVideoDriverPlayers)
        self.lay_right_column.addWidget(self.playerVideoDriverBox)
        self.lay_section_timeouts = QtWidgets.QVBoxLayout()
        self.lay_section_timeouts.setObjectName("lay_section_timeouts")
        self.section_timeouts = QtWidgets.QLabel(SettingsDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.section_timeouts.setFont(font)
        self.section_timeouts.setObjectName("section_timeouts")
        self.lay_section_timeouts.addWidget(self.section_timeouts)
        self.timeoutOverlayFlag = QtWidgets.QCheckBox(SettingsDialog)
        self.timeoutOverlayFlag.setObjectName("timeoutOverlayFlag")
        self.lay_section_timeouts.addWidget(self.timeoutOverlayFlag)
        self.lay_timeoutOverlay = QtWidgets.QHBoxLayout()
        self.lay_timeoutOverlay.setObjectName("lay_timeoutOverlay")
        self.timeoutOverlay = QtWidgets.QSpinBox(SettingsDialog)
        self.timeoutOverlay.setObjectName("timeoutOverlay")
        self.lay_timeoutOverlay.addWidget(self.timeoutOverlay)
        self.timeoutOverlayLabel = QtWidgets.QLabel(SettingsDialog)
        self.timeoutOverlayLabel.setObjectName("timeoutOverlayLabel")
        self.lay_timeoutOverlay.addWidget(self.timeoutOverlayLabel)
        self.lay_timeoutOverlay.setStretch(1, 1)
        self.lay_section_timeouts.addLayout(self.lay_timeoutOverlay)
        self.timeoutMouseHideFlag = QtWidgets.QCheckBox(SettingsDialog)
        self.timeoutMouseHideFlag.setObjectName("timeoutMouseHideFlag")
        self.lay_section_timeouts.addWidget(self.timeoutMouseHideFlag)
        self.lay_timeoutMouseHide = QtWidgets.QHBoxLayout()
        self.lay_timeoutMouseHide.setObjectName("lay_timeoutMouseHide")
        self.timeoutMouseHide = QtWidgets.QSpinBox(SettingsDialog)
        self.timeoutMouseHide.setObjectName("timeoutMouseHide")
        self.lay_timeoutMouseHide.addWidget(self.timeoutMouseHide)
        self.timeoutMouseHideLabel = QtWidgets.QLabel(SettingsDialog)
        self.timeoutMouseHideLabel.setObjectName("timeoutMouseHideLabel")
        self.lay_timeoutMouseHide.addWidget(self.timeoutMouseHideLabel)
        self.lay_timeoutMouseHide.setStretch(1, 1)
        self.lay_section_timeouts.addLayout(self.lay_timeoutMouseHide)
        self.lay_right_column.addLayout(self.lay_section_timeouts)
        self.lay_section_logging = QtWidgets.QVBoxLayout()
        self.lay_section_logging.setObjectName("lay_section_logging")
        self.section_logging = QtWidgets.QLabel(SettingsDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.section_logging.setFont(font)
        self.section_logging.setObjectName("section_logging")
        self.lay_section_logging.addWidget(self.section_logging)
        self.lay_logLevel = QtWidgets.QHBoxLayout()
        self.lay_logLevel.setObjectName("lay_logLevel")
        self.logLevelLabel = QtWidgets.QLabel(SettingsDialog)
        self.logLevelLabel.setObjectName("logLevelLabel")
        self.lay_logLevel.addWidget(self.logLevelLabel)
        self.logLevel = QtWidgets.QComboBox(SettingsDialog)
        self.logLevel.setObjectName("logLevel")
        self.lay_logLevel.addWidget(self.logLevel)
        self.lay_section_logging.addLayout(self.lay_logLevel)
        self.lay_logLevelVLC = QtWidgets.QHBoxLayout()
        self.lay_logLevelVLC.setObjectName("lay_logLevelVLC")
        self.logLevelVLCLabel = QtWidgets.QLabel(SettingsDialog)
        self.logLevelVLCLabel.setObjectName("logLevelVLCLabel")
        self.lay_logLevelVLC.addWidget(self.logLevelVLCLabel)
        self.logLevelVLC = QtWidgets.QComboBox(SettingsDialog)
        self.logLevelVLC.setObjectName("logLevelVLC")
        self.lay_logLevelVLC.addWidget(self.logLevelVLC)
        self.lay_section_logging.addLayout(self.lay_logLevelVLC)
        self.lay_right_column.addLayout(self.lay_section_logging)
        self.section_misc = QtWidgets.QLabel(SettingsDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.section_misc.setFont(font)
        self.section_misc.setObjectName("section_misc")
        self.lay_right_column.addWidget(self.section_misc)
        self.miscOpaqueHWOverlay = QtWidgets.QCheckBox(SettingsDialog)
        self.miscOpaqueHWOverlay.setObjectName("miscOpaqueHWOverlay")
        self.lay_right_column.addWidget(self.miscOpaqueHWOverlay)
        self.lay_section_misc = QtWidgets.QVBoxLayout()
        self.lay_section_misc.setObjectName("lay_section_misc")
        self.lay_right_column.addLayout(self.lay_section_misc)
        spacerItem5 = QtWidgets.QSpacerItem(
            0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.lay_right_column.addItem(spacerItem5)
        self.lay_body.addLayout(self.lay_right_column)
        self.lay_body.setStretch(0, 1)
        self.lay_main.addLayout(self.lay_body)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logFileOpen = QtWidgets.QPushButton(SettingsDialog)
        self.logFileOpen.setMinimumSize(QtCore.QSize(130, 0))
        self.logFileOpen.setObjectName("logFileOpen")
        self.horizontalLayout.addWidget(self.logFileOpen)
        self.buttonBox = QtWidgets.QDialogButtonBox(SettingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok
        )
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.lay_main.addLayout(self.horizontalLayout)

        self.retranslateUi(SettingsDialog)
        self.buttonBox.accepted.connect(SettingsDialog.accept)
        self.buttonBox.rejected.connect(SettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingsDialog.setWindowTitle(_translate("SettingsDialog", "Settings"))
        self.section_player.setText(_translate("SettingsDialog", "Player"))
        self.playerPauseBackgroundVideos.setText(
            _translate("SettingsDialog", "Pause background videos on single mode")
        )
        self.playerPauseWhenMinimized.setText(
            _translate("SettingsDialog", "Pause videos when minimized")
        )
        self.playerInhibitScreensaver.setText(
            _translate("SettingsDialog", "Disable screensaver while playing")
        )
        self.playerOneInstance.setText(
            _translate("SettingsDialog", "Allow only one instance")
        )
        self.section_playlist.setText(_translate("SettingsDialog", "Playlist"))
        self.playlistSaveWindow.setText(
            _translate("SettingsDialog", "Save window position and size")
        )
        self.playlistSavePosition.setText(
            _translate("SettingsDialog", "Save videos playback position")
        )
        self.playlistSaveState.setText(
            _translate("SettingsDialog", "Save videos playing / paused status")
        )
        self.playlistSeekSync.setText(
            _translate("SettingsDialog", "Synchronize seek by default")
        )
        self.playlistTrackChanges.setText(
            _translate("SettingsDialog", "Warn about unsaved changes")
        )
        self.section_grid.setText(
            _translate("SettingsDialog", "Default Grid Parameters")
        )
        self.gridModeLabel.setText(_translate("SettingsDialog", "Grid mode"))
        self.gridSizeLabel.setText(_translate("SettingsDialog", "Grid size"))
        self.gridFit.setText(_translate("SettingsDialog", "Fit grid cells"))
        self.section_video_defaults.setText(
            _translate("SettingsDialog", "Default Video Parameters")
        )
        self.videoAspectLabel.setText(_translate("SettingsDialog", "Aspect mode"))
        self.repeatModeLabel.setText(_translate("SettingsDialog", "Repeat mode"))
        self.videoRandomLoop.setText(
            _translate("SettingsDialog", "Start at random position")
        )
        self.videoPaused.setText(_translate("SettingsDialog", "Paused"))
        self.videoMuted.setText(_translate("SettingsDialog", "Muted"))
        self.languageBox.setTitle(_translate("SettingsDialog", "Language"))
        self.playerVideoDriverBox.setTitle(
            _translate("SettingsDialog", "Video Decoder")
        )
        self.playerVideoDriverPlayersLabel.setText(
            _translate("SettingsDialog", "Videos per process")
        )
        self.section_timeouts.setText(_translate("SettingsDialog", "Timeouts"))
        self.timeoutOverlayFlag.setText(
            _translate("SettingsDialog", "Hide overlay after timeout")
        )
        self.timeoutOverlayLabel.setText(
            _translate("SettingsDialog", "Video overlay timeout (sec)")
        )
        self.timeoutMouseHideFlag.setText(
            _translate("SettingsDialog", "Hide mouse after timeout")
        )
        self.timeoutMouseHideLabel.setText(
            _translate("SettingsDialog", "Mouse hide timeout (sec)")
        )
        self.section_logging.setText(_translate("SettingsDialog", "Logging"))
        self.logLevelLabel.setText(_translate("SettingsDialog", "Log level"))
        self.logLevelVLCLabel.setText(_translate("SettingsDialog", "Log level (VLC)"))
        self.section_misc.setText(_translate("SettingsDialog", "Misc"))
        self.miscOpaqueHWOverlay.setText(
            _translate("SettingsDialog", "Opaque overlay (fix black screen)")
        )
        self.logFileOpen.setText(_translate("SettingsDialog", "Open log file"))
