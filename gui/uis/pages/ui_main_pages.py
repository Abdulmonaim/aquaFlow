# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagesNzRTYa.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(874, 520)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.pages.setStyleSheet(u"font: 12pt \"Sofia Pro\";")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"font-size: 11pt;")
        self.page_1_layout = QVBoxLayout(self.page_1)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.scrollArea = QScrollArea(self.page_1)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background: transparent;")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setWidgetResizable(True)
        self.main_apge = QWidget()
        self.main_apge.setObjectName(u"main_apge")
        self.main_apge.setGeometry(QRect(0, 0, 854, 500))
        self.main_apge.setAutoFillBackground(False)
        self.verticalLayout_mn = QVBoxLayout(self.main_apge)
        self.verticalLayout_mn.setSpacing(0)
        self.verticalLayout_mn.setObjectName(u"verticalLayout_mn")
        self.verticalLayout_mn.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.main_apge)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_12)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.frame_12)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_23)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_28 = QFrame(self.frame_23)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMaximumSize(QSize(16777215, 30))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.HomesalesName = QHBoxLayout(self.frame_28)
        self.HomesalesName.setSpacing(0)
        self.HomesalesName.setObjectName(u"HomesalesName")
        self.HomesalesName.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_28)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 18))

        self.HomesalesName.addWidget(self.label_7)


        self.verticalLayout_9.addWidget(self.frame_28)

        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMaximumSize(QSize(16777215, 80))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.Homesales1 = QHBoxLayout(self.frame_24)
        self.Homesales1.setSpacing(0)
        self.Homesales1.setObjectName(u"Homesales1")
        self.Homesales1.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_9.addWidget(self.frame_24)

        self.frame_25 = QFrame(self.frame_23)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_25)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QFrame(self.frame_25)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.Homesales2 = QGridLayout(self.frame_26)
        self.Homesales2.setSpacing(0)
        self.Homesales2.setObjectName(u"Homesales2")
        self.Homesales2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_10.addWidget(self.frame_26)

        self.frame_27 = QFrame(self.frame_25)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMaximumSize(QSize(16777215, 60))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.Homesales3 = QHBoxLayout(self.frame_27)
        self.Homesales3.setSpacing(0)
        self.Homesales3.setObjectName(u"Homesales3")
        self.Homesales3.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_10.addWidget(self.frame_27)


        self.verticalLayout_9.addWidget(self.frame_25)


        self.verticalLayout_5.addWidget(self.frame_23)


        self.horizontalLayout_3.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_9)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(130, 16777215))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_13)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_13)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 33))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_11)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.frame_11)

        self.frame_16 = QFrame(self.frame_13)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.critical_layout = QVBoxLayout(self.frame_16)
        self.critical_layout.setSpacing(0)
        self.critical_layout.setObjectName(u"critical_layout")
        self.critical_layout.setContentsMargins(25, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.frame_16)


        self.horizontalLayout_3.addWidget(self.frame_13)


        self.verticalLayout_mn.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.main_apge)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(16777215, 200))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_10)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.frame_10)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 30))
        self.frame_14.setMaximumSize(QSize(16777215, 30))
        self.frame_14.setSizeIncrement(QSize(0, 0))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_14)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_6.addWidget(self.label_11)


        self.verticalLayout_6.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_10)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_15)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.chartWidget = QStackedWidget(self.frame_15)
        self.chartWidget.setObjectName(u"chartWidget")
        self.line_bar_page = QWidget()
        self.line_bar_page.setObjectName(u"line_bar_page")
        self.lbar_chart = QGridLayout(self.line_bar_page)
        self.lbar_chart.setSpacing(10)
        self.lbar_chart.setObjectName(u"lbar_chart")
        self.lbar_chart.setContentsMargins(0, 0, 0, 0)
        self.chartWidget.addWidget(self.line_bar_page)

        self.verticalLayout_7.addWidget(self.chartWidget)


        self.verticalLayout_6.addWidget(self.frame_15)


        self.verticalLayout_mn.addWidget(self.frame_10)

        self.scrollArea.setWidget(self.main_apge)

        self.page_1_layout.addWidget(self.scrollArea)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.scroll_area = QScrollArea(self.page_2)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet(u"background: transparent;")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 98, 92))
        self.contents.setStyleSheet(u"background: transparent;")
        self.verticalLayout = QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.frame = QFrame(self.contents)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 160))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 65))
        self.frame_2.setMaximumSize(QSize(16777215, 80))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setMaximumSize(QSize(16777215, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 80))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 1, 0, 0)

        self.verticalLayout_2.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame)

        self.scroll_area.setWidget(self.contents)

        self.page_2_layout.addWidget(self.scroll_area)

        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"QFrame {\n"
"	font-size: 10pt;\n"
"}")
        self.page_3_layout = QVBoxLayout(self.page_3)
        self.page_3_layout.setSpacing(0)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.page_3_layout.setContentsMargins(5, 5, 5, 5)
        self.frame_4 = QFrame(self.page_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 40))
        self.frame_4.setMaximumSize(QSize(16777215, 55))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.page_3_layout.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.page_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_6)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.sales_widget = QStackedWidget(self.frame_6)
        self.sales_widget.setObjectName(u"sales_widget")
        self.sales = QWidget()
        self.sales.setObjectName(u"sales")
        self.verticalLayout_sales = QVBoxLayout(self.sales)
        self.verticalLayout_sales.setSpacing(0)
        self.verticalLayout_sales.setObjectName(u"verticalLayout_sales")
        self.verticalLayout_sales.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.sales)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_sales.addWidget(self.label_6)

        self.sales_widget.addWidget(self.sales)
        self.combined = QWidget()
        self.combined.setObjectName(u"combined")
        self.verticalLayout_cc = QVBoxLayout(self.combined)
        self.verticalLayout_cc.setSpacing(0)
        self.verticalLayout_cc.setObjectName(u"verticalLayout_cc")
        self.verticalLayout_cc.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.combined)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_c1 = QVBoxLayout(self.frame_7)
        self.verticalLayout_c1.setSpacing(0)
        self.verticalLayout_c1.setObjectName(u"verticalLayout_c1")
        self.verticalLayout_c1.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_c1.addWidget(self.label_4)


        self.verticalLayout_cc.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.combined)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_c2 = QVBoxLayout(self.frame_8)
        self.verticalLayout_c2.setSpacing(0)
        self.verticalLayout_c2.setObjectName(u"verticalLayout_c2")
        self.verticalLayout_c2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_cc.addWidget(self.frame_8)

        self.sales_widget.addWidget(self.combined)

        self.gridLayout.addWidget(self.sales_widget, 0, 0, 1, 1)


        self.page_3_layout.addWidget(self.frame_6)

        self.pages.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_customers = QVBoxLayout(self.page_4)
        self.verticalLayout_customers.setSpacing(5)
        self.verticalLayout_customers.setObjectName(u"verticalLayout_customers")
        self.verticalLayout_customers.setContentsMargins(5, 5, 5, 5)
        self.label_8 = QLabel(self.page_4)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_customers.addWidget(self.label_8)

        self.pages.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_4 = QVBoxLayout(self.page_5)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.label_12 = QLabel(self.page_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_4.addWidget(self.label_12)

        self.frame_19 = QFrame(self.page_5)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(16777215, 80))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.OutCome_layout_1 = QHBoxLayout(self.frame_19)
        self.OutCome_layout_1.setObjectName(u"OutCome_layout_1")

        self.verticalLayout_4.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.page_5)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.OutCome_layout_2 = QVBoxLayout(self.frame_20)
        self.OutCome_layout_2.setSpacing(0)
        self.OutCome_layout_2.setObjectName(u"OutCome_layout_2")
        self.OutCome_layout_2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_4.addWidget(self.frame_20)

        self.pages.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_8 = QVBoxLayout(self.page_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.frame_29 = QFrame(self.page_6)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(0, 60))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.stat_emplo_layout = QHBoxLayout(self.frame_29)
        self.stat_emplo_layout.setObjectName(u"stat_emplo_layout")
        self.stat_emplo_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_8.addWidget(self.frame_29)

        self.frame_22 = QFrame(self.page_6)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.archieve_layout = QVBoxLayout(self.frame_22)
        self.archieve_layout.setSpacing(0)
        self.archieve_layout.setObjectName(u"archieve_layout")
        self.archieve_layout.setContentsMargins(0, 0, 0, 0)
        self.Archive = QStackedWidget(self.frame_22)
        self.Archive.setObjectName(u"Archive")
        self.emloe_page = QWidget()
        self.emloe_page.setObjectName(u"emloe_page")
        self.emplo_layout = QVBoxLayout(self.emloe_page)
        self.emplo_layout.setObjectName(u"emplo_layout")
        self.emplo_layout.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.emloe_page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 25))

        self.emplo_layout.addWidget(self.label_10)

        self.frame_21 = QFrame(self.emloe_page)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(16777215, 100))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.add_emplo_layut = QHBoxLayout(self.frame_21)
        self.add_emplo_layut.setSpacing(0)
        self.add_emplo_layut.setObjectName(u"add_emplo_layut")
        self.add_emplo_layut.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.frame_21)
        self.label_14.setObjectName(u"label_14")

        self.add_emplo_layut.addWidget(self.label_14)


        self.emplo_layout.addWidget(self.frame_21)

        self.Archive.addWidget(self.emloe_page)
        self.statics_page = QWidget()
        self.statics_page.setObjectName(u"statics_page")
        self.verticalLayout_13 = QVBoxLayout(self.statics_page)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.scroll_area_2 = QScrollArea(self.statics_page)
        self.scroll_area_2.setObjectName(u"scroll_area_2")
        self.scroll_area_2.setStyleSheet(u"background: transparent;")
        self.scroll_area_2.setFrameShape(QFrame.NoFrame)
        self.scroll_area_2.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scroll_area_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scroll_area_2.setWidgetResizable(True)
        self.contents_2 = QWidget()
        self.contents_2.setObjectName(u"contents_2")
        self.contents_2.setGeometry(QRect(0, 0, 100, 30))
        self.contents_2.setStyleSheet(u"background: transparent;")
        self.statics_layut = QVBoxLayout(self.contents_2)
        self.statics_layut.setObjectName(u"statics_layut")
        self.statics_layut.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.contents_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 25))
        self.label_15.setStyleSheet(u"")

        self.statics_layut.addWidget(self.label_15)

        self.scroll_area_2.setWidget(self.contents_2)

        self.verticalLayout_13.addWidget(self.scroll_area_2)

        self.Archive.addWidget(self.statics_page)

        self.archieve_layout.addWidget(self.Archive)


        self.verticalLayout_8.addWidget(self.frame_22)

        self.pages.addWidget(self.page_6)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(0)
        self.chartWidget.setCurrentIndex(0)
        self.sales_widget.setCurrentIndex(0)
        self.Archive.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label_7.setText(QCoreApplication.translate("MainPages", u"Sales", None))
        self.label_11.setText(QCoreApplication.translate("MainPages", u"STATICS", None))
        self.label_6.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainPages", u"Combined", None))
        self.label_8.setText(QCoreApplication.translate("MainPages", u"Customers", None))
        self.label_12.setText(QCoreApplication.translate("MainPages", u"OutCome", None))
        self.label_10.setText(QCoreApplication.translate("MainPages", u"EMPLOYEES", None))
        self.label_14.setText(QCoreApplication.translate("MainPages", u"ADD EMPLOYEE", None))
        self.label_15.setText(QCoreApplication.translate("MainPages", u"STATICS", None))
    # retranslateUi

