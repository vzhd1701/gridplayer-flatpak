from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        self.lay_main = QtWidgets.QVBoxLayout(AboutDialog)
        self.lay_main.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.lay_main.setContentsMargins(20, 20, 20, 20)
        self.lay_main.setSpacing(12)
        self.lay_main.setObjectName("lay_main")
        self.logo_lay = QtWidgets.QHBoxLayout()
        self.logo_lay.setObjectName("logo_lay")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.logo_lay.addItem(spacerItem)
        self.logo = QtWidgets.QLabel(AboutDialog)
        self.logo.setMinimumSize(QtCore.QSize(250, 250))
        self.logo.setMaximumSize(QtCore.QSize(250, 250))
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.logo_lay.addWidget(self.logo)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.logo_lay.addItem(spacerItem1)
        self.lay_main.addLayout(self.logo_lay)
        self.name = QtWidgets.QLabel(AboutDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.name.setText("App Name")
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.lay_main.addWidget(self.name)
        self.version = QtWidgets.QLabel(AboutDialog)
        self.version.setText("version X.X.X")
        self.version.setAlignment(QtCore.Qt.AlignCenter)
        self.version.setObjectName("version")
        self.lay_main.addWidget(self.version)
        self.info = QtWidgets.QLabel(AboutDialog)
        self.info.setText("about info")
        self.info.setTextFormat(QtCore.Qt.RichText)
        self.info.setAlignment(QtCore.Qt.AlignCenter)
        self.info.setWordWrap(True)
        self.info.setOpenExternalLinks(True)
        self.info.setObjectName("info")
        self.lay_main.addWidget(self.info)
        self.attributionsTitle = QtWidgets.QLabel(AboutDialog)
        self.attributionsTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.attributionsTitle.setWordWrap(True)
        self.attributionsTitle.setObjectName("attributionsTitle")
        self.lay_main.addWidget(self.attributionsTitle)
        self.attributionsBox = QtWidgets.QTextBrowser(AboutDialog)
        self.attributionsBox.setMinimumSize(QtCore.QSize(350, 200))
        self.attributionsBox.setMaximumSize(QtCore.QSize(16777215, 200))
        self.attributionsBox.setOpenExternalLinks(True)
        self.attributionsBox.setObjectName("attributionsBox")
        self.lay_main.addWidget(self.attributionsBox)

        self.retranslateUi(AboutDialog)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        _translate = QtCore.QCoreApplication.translate
        AboutDialog.setWindowTitle(_translate("AboutDialog", "About"))
        self.attributionsTitle.setText(
            _translate("AboutDialog", "This software was built using:")
        )
