# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'right_columnhWInbL.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_RightColumn(object):
    def setupUi(self, RightColumn):
        if not RightColumn.objectName():
            RightColumn.setObjectName(u"RightColumn")
        RightColumn.resize(240, 580)
        self.main_pages_layout = QVBoxLayout(RightColumn)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.menus = QStackedWidget(RightColumn)
        self.menus.setObjectName(u"menus")
        self.menu_1 = QWidget()
        self.menu_1.setObjectName(u"menu_1")
        self.verticalLayout = QVBoxLayout(self.menu_1)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.label_1 = QLabel(self.menu_1)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setMaximumSize(QSize(16777215, 33))
        font = QFont()
        font.setPointSize(16)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet(u"font-size: 16pt")
        self.label_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_1)

        self.frame_2 = QFrame(self.menu_1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 70))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.btn_lang_lay = QHBoxLayout(self.frame_2)
        self.btn_lang_lay.setSpacing(10)
        self.btn_lang_lay.setObjectName(u"btn_lang_lay")
        self.btn_lang_lay.setContentsMargins(0, 0, 0, 6)

        self.verticalLayout.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.menu_1)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 70))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.btn_theme_lay = QGridLayout(self.frame_4)
        self.btn_theme_lay.setObjectName(u"btn_theme_lay")
        self.btn_theme_lay.setContentsMargins(0, 0, 0, 6)

        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.menu_1)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 70))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.cnfrm_stngBtn = QHBoxLayout(self.frame_5)
        self.cnfrm_stngBtn.setObjectName(u"cnfrm_stngBtn")
        self.cnfrm_stngBtn.setContentsMargins(0, 6, 0, 0)

        self.verticalLayout.addWidget(self.frame_5)

        self.frame = QFrame(self.menu_1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.right_lay_1 = QVBoxLayout(self.frame)
        self.right_lay_1.setObjectName(u"right_lay_1")
        self.right_lay_1.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.right_lay_1.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        self.menus.addWidget(self.menu_1)
        self.menu_2 = QWidget()
        self.menu_2.setObjectName(u"menu_2")
        self.verticalLayout_2 = QVBoxLayout(self.menu_2)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.label_2 = QLabel(self.menu_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font-size: 16pt")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.menus.addWidget(self.menu_2)

        self.main_pages_layout.addWidget(self.menus)


        self.retranslateUi(RightColumn)

        self.menus.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(RightColumn)
    # setupUi

    def retranslateUi(self, RightColumn):
        RightColumn.setWindowTitle(QCoreApplication.translate("RightColumn", u"Form", None))
        self.label_1.setText(QCoreApplication.translate("RightColumn", u"Settings", None))
        self.label_2.setText(QCoreApplication.translate("RightColumn", u"Menu 2 - Right Menu", None))
    # retranslateUi

