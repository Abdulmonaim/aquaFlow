# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledoZtLXr.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_cloumn(object):
    def setupUi(self, cloumn):
        if not cloumn.objectName():
            cloumn.setObjectName(u"cloumn")
        cloumn.resize(861, 100)
        self.verticalLayout = QVBoxLayout(cloumn)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(cloumn)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_2.setLayoutDirection(Qt.LeftToRight)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(0, 0))
        self.pushButton.setMaximumSize(QSize(16777215, 35))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setAcceptDrops(True)
        self.pushButton.setLayoutDirection(Qt.LeftToRight)
        self.pushButton.setStyleSheet(u"background-color: transparent;\n"
"border:0px;\n"
"text-align:left;")
        icon = QIcon()
        icon.addFile(u"../../images/svg_icons/icon_arrow_right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setAutoDefault(False)

        self.verticalLayout_3.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setLayoutDirection(Qt.LeftToRight)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(50, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QSize(0, 0))
        self.pushButton_2.setMaximumSize(QSize(16777215, 35))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setAcceptDrops(True)
        self.pushButton_2.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_2.setStyleSheet(u"background-color: transparent;\n"
"border:0px;\n"
"text-align:left;")
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setAutoExclusive(False)
        self.pushButton_2.setAutoDefault(False)

        self.verticalLayout_4.addWidget(self.pushButton_2)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(cloumn)

        QMetaObject.connectSlotsByName(cloumn)
    # setupUi

    def retranslateUi(self, cloumn):
        cloumn.setWindowTitle(QCoreApplication.translate("cloumn", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("cloumn", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("cloumn", u"PushButton", None))
    # retranslateUi

