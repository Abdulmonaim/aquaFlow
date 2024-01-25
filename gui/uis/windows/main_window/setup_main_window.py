#IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
from . functions_main_window import *
import sys
import os
import sqlite3
from datetime import datetime
# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import json
# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *
# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings
# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes
# IMPORT THEME LANGUAGE
# ///////////////////////////////////////////////////////////////
from gui.core.json_language import Language
# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *
# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from . ui_main import *

# MAIN FUNCTIONS
# ///////////////////////////////////////////////////////////////
from . functions_main_window import *
#from functions_main_window import *
# PY WINDOW
# ///////////////////////////////////////////////////////////////

#############################DATABASE##########################################
db = sqlite3.connect('plumbing.db')
control = db.cursor()
###############################################################################

class SetupMainWindow:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    # LOAD SETTINGS
    # ///////////////////////////////////////////////////////////////
    settings = Settings()
    settings = settings.items
    # ADD LEFT MENUS
    # ///////////////////////////////////////////////////////////////
    add_left_menus = [
        {
            "btn_icon": "icon_home.svg",
            "btn_id": "btn_home",
            "btn_text": "Home",
            "btn_tooltip": "Home Page",
            "show_top": True,
            "is_active": True
        },
        {
            "btn_icon": "icon_file.svg",
            "btn_id": "btn_page_2",
            "btn_text": "Catugary",
            "btn_tooltip": "Catugary page",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_info.svg",
            "btn_id": "btn_page_3",
            "btn_text": "Sales",
            "btn_tooltip": "Sales page",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_add_user.svg",
            "btn_id": "btn_page_4",
            "btn_text": "Customer",
            "btn_tooltip": "Customer page",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_attachment.svg",
            "btn_id": "btn_page_5",
            "btn_text": "OutCome",
            "btn_tooltip": "OutCome page",
            "show_top": True,
            "is_active": False
        },
        {
            #"btn_icon": "icon_send.svg",
            "btn_icon": "icon_folder2.svg",
            "btn_id": "btn_page_6",
            "btn_text": "Archieve",
            "btn_tooltip": "Archieve page",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon" : "icon_info.svg",
            "btn_id" : "btn_info",
            "btn_text" : "Information",
            "btn_tooltip" : "Open Daily",
            "show_top" : False,
            "is_active" : False
        },
    ]

    # ADD TITLE BAR MENUS
    # ///////////////////////////////////////////////////////////////
    
    if settings["language"] == "english":
        add_title_bar_menus = [
            {
                "btn_icon": "icon_search.svg",
                "btn_id": "btn_search",
                "btn_tooltip": "Search",
                "is_active": False
            },
            {
                "btn_icon": "icon_settings.svg",
                "btn_id": "btn_top_settings",
                "btn_tooltip": "Top settings",
                "is_active": False
            }
        ]
    else:
        add_title_bar_menus = [
            {
                "btn_icon": "icon_settings.svg",
                "btn_id": "btn_top_settings",
                "btn_tooltip": "Top settings",
                "is_active": False
            },
            {
                "btn_icon": "icon_search.svg",
                "btn_id": "btn_search",
                "btn_tooltip": "Search",
                "is_active": False
            }
        ]

    # SETUP CUSTOM BTNs OF CUSTOM WIDGETS
    # Get sender() function when Btn is clicked
    # ///////////////////////////////////////////////////////////////
    
    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()

    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        # APP TITLE
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(self.settings["app_name"])
        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # LOAD THEME Language
        # ///////////////////////////////////////////////////////////////
        language = Language()
        self.language = language.items

        #json
        self.items = {}
        json_file = "fabData.json"
        app_path = os.path.abspath(os.getcwd())
        self.settings_path = os.path.normpath(os.path.join(app_path, json_file))
        with open(self.settings_path, "r", encoding='utf-8') as reader:
            dataw = json.loads(reader.read())
            self.items = dataw
        #########################################remve
        mydt = self.items["cat1"]["firstCat"]["subcat1"]
        ###########################################    

    #SPECIFIED VALUES VALIDATION FOR INPUTS
    #//////////////////////////////////////////////////////////////
       

        money_specify  = QRegularExpression("[0-9]{6}")
        money_val = QRegularExpressionValidator(money_specify)

        #WITH NO NUM AT THE BEGAIN
        #name_specify  = QRegularExpression("[A-Za-z_]+([A-Za-z_0-9]*)")
        #name_val = QRegularExpressionValidator(name_specify)

    # RIGHT COLUMN
        # ///////////////////////////////////////////////////////////////
        #ARABIC BTN 
        self.arabic = PyPushButton(
            text= self.language["main_app"]["arabic"],
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["bg_three"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.arabic.setMaximumHeight(33)
        self.arabic.setMinimumHeight(33)
        self.arabic.setMaximumWidth(120)
        self.ui.right_column.btn_lang_lay.addWidget(self.arabic,alignment=Qt.AlignTop)
        #ENGLISH BTN 
        self.english = PyPushButton(
            text= self.language["main_app"]["english"],
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["bg_three"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.english.setMaximumHeight(33)
        self.english.setMinimumHeight(33)
        self.english.setMaximumWidth(120)
        self.ui.right_column.btn_lang_lay.addWidget(self.english,alignment=Qt.AlignTop)
        #//////////////////////////////////////
        #BRIGHTC BTN 
        self.bright = PyPushButton(
            text=  "LIGHT",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["context_color"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.bright.setMaximumHeight(33)
        
        #CUSTOMIZED BTN 
        self.customized = PyPushButton(
            text=  "DARK",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["context_color"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.customized.setMaximumHeight(33)

        self.ui.right_column.btn_theme_lay.addWidget(self.bright,1,1)
        self.ui.right_column.btn_theme_lay.addWidget(self.customized,1,0)
        #CONFIRM SETINGS BTN
        self.ConfirmSettings = PyPushButton(
            text= self.language["main_app"]["sale_confirm"],
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.ConfirmSettings.setMaximumHeight(33)
        self.ConfirmSettings.setMinimumHeight(33)
        self.ConfirmSettings.setMaximumWidth(120)
        self.ui.right_column.cnfrm_stngBtn.addWidget(self.ConfirmSettings,alignment=Qt.AlignTop)
        #start edit 
        self.upload = PyPushButton(
            text= "upload",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.upload.setMaximumHeight(33)
        self.upload.setMinimumHeight(33)
        self.upload.setMaximumWidth(120)
        self.ui.right_column.right_lay_1.addWidget(self.upload)

        self.editcat = PyToggle(
            width = 50,
            bg_color =  self.themes["app_color"]["bg_two"], 
            circle_color = "#DDD",
            active_color =self.themes["app_color"]["icon_hover"],
            animation_curve = QEasingCurve.OutBounce
            ) 
        self.editcat.setMinimumHeight(33)
        self.editcat.setMaximumWidth(35)
        #self.ui.right_column.right_lay_1.addWidget(self.editcat)

        self.categery_combo_edit = PyCombo(
            radius = 8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color = self.themes["app_color"]["dark_one"],
            combo_theme=[],
        )
        #self.categery_combo_edit.setMinimumWidth(400)
        self.categery_combo_edit.setMinimumHeight(33)
        #self.ui.right_column.right_lay_1.addWidget(self.categery_combo_edit)



        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

    # LEFT COLUMN DAILY
        #self.ui.load_pages.label_9.setText(self.language["main_app"]["daliy"])

        self.table_widget_dialy = PyTableWidget(
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["bg_one"],
            bg_color = self.themes["app_color"]["bg_two"],
            header_horizontal_color = self.themes["app_color"]["dark_two"],
            header_vertical_color = self.themes["app_color"]["bg_three"],
            bottom_line_color = self.themes["app_color"]["bg_three"],
            grid_line_color = self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"]
        )
        
        self.table_widget_dialy.setColumnCount(3)
        #self.table_widget_dialy.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget_dialy.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_widget_dialy.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_widget_dialy.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table_widget_dialy.setMinimumHeight(400)
        self.table_widget_dialy.setMaximumHeight(55500)
        self.table_widget_dialy.verticalHeader().hide()
        # Columns / Header
        self.column_1 = QTableWidgetItem()
        self.column_1.setTextAlignment(Qt.AlignCenter)
        self.column_1.setText(self.language["main_app"]["daliy_sourese"])

        self.column_2 = QTableWidgetItem()
        self.column_2.setTextAlignment(Qt.AlignCenter)
        self.column_2.setText(self.language["main_app"]["daliy_detail"])

        self.column_3 = QTableWidgetItem()
        self.column_3.setTextAlignment(Qt.AlignCenter)
        self.column_3.setText(self.language["main_app"]["daliy_price"])

        # Set column
        self.table_widget_dialy.setHorizontalHeaderItem(0, self.column_1)
        self.table_widget_dialy.setHorizontalHeaderItem(1, self.column_2)
        self.table_widget_dialy.setHorizontalHeaderItem(2, self.column_3)
        self.totalIncomeValue = 0
        
        
        self.ui.left_column.menus.verticalLayout.addWidget(self.table_widget_dialy)

        #TOTAL DAILY INCOME VALUE
        self.total_income = PyLabel(
            #text = str(self.critical_iteams[i]),
            text = str(self.totalIncomeValue),
            color=self.themes["app_color"]["text_foreground"],
            )
        self.total_income.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.ui.left_column.menus.verticalLayout.addWidget(self.total_income)
        #TOTAL DAILY INCOME BUTTON
        self.total_income_button = PyPushButton(
            text=str(self.language["main_app"]["daliy_btn"]),
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["red"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
            )
        self.total_income_button.setMinimumHeight(33)
        self.total_income_button.setMaximumWidth(120)
        self.total_income_button.setMinimumWidth(120)
        self.ui.left_column.menus.verticalLayout.addWidget(self.total_income_button,alignment=Qt.AlignCenter)

    #HOME PAGE
    #///////////////////////////////////////////////////////////////
        #ADD CRITICAL ITEAMS
        self.ui.load_pages.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.updateCriticalItems = PyPushButton(
            text=self.language["main_app"]["critical_iteams"],
            radius=4,
            color=self.themes["app_color"]["red"],
            bg_color=self.themes["app_color"]["trans"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.updateCriticalItems.setMinimumHeight(33)
        self.updateCriticalItems.setMinimumWidth(120)
        self.ui.load_pages.verticalLayout_11.addWidget(self.updateCriticalItems)
        #self.ui.load_pages.label.setText(self.language["main_app"]["critical_iteams"])

        sql = "SELECT COUNT(item) FROM item"
        control.execute(sql)
        h = control.fetchone()

        sql = "SELECT quantity, critQuan, item FROM item"
        control.execute(sql)
        f = control.fetchall()
        
        self.critical_iteams = QListWidget()
        self.critical_iteams.setStyleSheet("border:none")
        self.critical_iteams.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.critical_iteams.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        for i in range(h[0]):
            if f[i][1] >= f[i][0]:
                item = QListWidgetItem(str(f[i][2]))
                self.critical_iteams.addItem(item)
        self.ui.load_pages.critical_layout.addWidget(self.critical_iteams)
        #space frame
        self.spaceFrame_critical= PyFrame()
        self.spaceFrame_critical.setMinimumHeight(0)
        self.ui.load_pages.critical_layout.addWidget(self.spaceFrame_critical)
        #///////////////////////////// SALES AREA

        #TOGGLE to check if it's combined or not
        self.salesOrCombined = PyToggle(
            width = 50,
            bg_color =  self.themes["app_color"]["bg_two"], 
            circle_color = "#DDD",
            active_color =self.themes["app_color"]["icon_hover"],
            animation_curve = QEasingCurve.OutBounce
            ) 
        self.salesOrCombined.setMinimumHeight(33)
        self.salesOrCombined.setMaximumWidth(35)
        self.ui.load_pages.HomesalesName.addWidget(self.salesOrCombined)
        self.ui.load_pages.HomesalesName.setContentsMargins(0, 0,30,0)
        #1
        
        #ITEMS
        self.ui.load_pages.label_7.setText(self.language["main_app"]["sale"])
        #inputs
        self.inputs = PyInputs(
            color = self.themes["app_color"]["text_foreground"],
            bg_color = self.themes["app_color"]["bg_two"],
            )
        self.inputs.line_edit_widget.setMinimumWidth(300)
        self.ui.load_pages.Homesales1.addWidget(self.inputs,alignment=Qt.AlignLeft)

        #PAID
        self.HomeSalePaid = PyLineEdit(
            text = "",
            place_holder_text = self.language["main_app"]["sale_paid"],
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.HomeSalePaid.setMinimumHeight(33)
        self.HomeSalePaid.setMaximumWidth(80)
        self.HomeSalePaid.setValidator(money_val)
        self.ui.load_pages.Homesales1.addWidget(self.HomeSalePaid)
        
        #LEFT
        self.HomeSaleLeft = PyLineEdit(
            text = "",
            place_holder_text = self.language["main_app"]["sale_left"],
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.HomeSaleLeft.setMinimumHeight(33)
        self.HomeSaleLeft.setMaximumWidth(80)
        self.HomeSaleLeft.setValidator(money_val)
        self.ui.load_pages.Homesales1.addWidget(self.HomeSaleLeft)        


        #SPACE
        self.Homesales1Space = PyFrame()
        self.Homesales1Space.setMaximumWidth(222222)
        self.Homesales1Space.setMinimumWidth(100)
        self.ui.load_pages.Homesales1.addWidget(self.Homesales1Space)
        
        #TOGGLE to check if it's combined or not
        self.newOrExist = PyToggle(
            width = 50,
            bg_color =  self.themes["app_color"]["bg_two"], 
            circle_color = "#DDD",
            active_color =self.themes["app_color"]["dark_one"],
            animation_curve = QEasingCurve.OutBounce
            ) 
        self.newOrExist.setMinimumHeight(33)
        self.newOrExist.setMaximumWidth(35)


        #NAME
        self.selsOrCombo = QCheckBox()
        self.selsOrCombo.setText(self.language["main_app"]["combined_mode"])
        self.ui.load_pages.Homesales1.addWidget(self.selsOrCombo)

        self.HomeSaleName = PyLineEdit(
            text = "",
            place_holder_text = self.language["main_app"]["sale_name_ord"],
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.HomeSaleName.setMinimumHeight(33)
        self.HomeSaleName.setMaximumWidth(300)
        #self.HomeSaleName.setValidator(name_val)
        self.ui.load_pages.Homesales1.addWidget(self.HomeSaleName)
        
        #SALES_OP TABLE
        
        self.salesOpTable = PyTableWidget(
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["bg_one"],
            bg_color = self.themes["app_color"]["bg_two"],
            header_horizontal_color = self.themes["app_color"]["dark_two"],
            header_vertical_color = self.themes["app_color"]["bg_three"],
            bottom_line_color = self.themes["app_color"]["bg_three"],
            grid_line_color = self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"]
            )
        
        self.salesOpTable.setColumnCount(3)
        self.salesOpTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.salesOpTable.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.salesOpTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.salesOpTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.salesOpTable.setMaximumHeight(2000)
        # Columns / Header

        self.column_1 = QTableWidgetItem()
        self.column_1.setTextAlignment(Qt.AlignCenter)
        self.column_1.setText(self.language["main_app"]["sale_item"])

        self.column_2 = QTableWidgetItem()
        #self.column_2.setModelData(money_val)
        self.column_2.setTextAlignment(Qt.AlignCenter)
        self.column_2.setText(self.language["main_app"]["sale_price"])

        self.column_3 = QTableWidgetItem()
        #self.column_3.setModelData(money_val)
        self.column_3.setText(self.language["main_app"]["sale_quantity"])

        # Set column
        self.salesOpTable.setHorizontalHeaderItem(0, self.column_1)
        self.salesOpTable.setHorizontalHeaderItem(1, self.column_2)
        self.salesOpTable.setHorizontalHeaderItem(2, self.column_3)
       
        #add to page
        self.ui.load_pages.Homesales2.addWidget(self.salesOpTable,0,0)
       
        #PAYMENTS_LAYOUT
        self.payFrame = PyFrame()
        self.payFrame.setMaximumWidth(300)
        self.HomesalesPay = QGridLayout(self.payFrame)
        self.HomesalesPay.setSpacing(6)
        self.HomesalesPay.setObjectName(u"HomesalesPay")
        self.HomesalesPay.setContentsMargins(0, 0, 0, 0)
        
        #PAYMENTS_LAYOUT_top
        self.payFrameTop = PyFrame()
        self.payFrameTop.setMaximumHeight(100)
        self.HomesalesPayTop = QGridLayout(self.payFrameTop)
        self.HomesalesPayTop.setSpacing(0)
        self.HomesalesPayTop.setObjectName(u"HomesalesPayTop")
        self.HomesalesPayTop.setContentsMargins(0, 0, 0, 0)

        #DATES
        self.date_payment = PyDate(
            color = self.themes["app_color"]["text_foreground"],
        )
        self.date_payment.setMinimumHeight(33)
        self.date_payment.setMaximumWidth(80)


        #inputs_dates_payments
        self.inputs_payments = PyInputs(
            color = self.themes["app_color"]["text_foreground"],
            bg_color = self.themes["app_color"]["bg_two"],
            )
        self.inputs_payments.line_edit_widget.setMaximumWidth(100)
        #a validation and click problem
        #self.inputs_payments.line_edit_widget.setPlaceholderText("Money")
        #self.inputs_payments.line_edit_widget.setValidator(money_val)
        #add to the top dates layout
        self.HomesalesPayTop.addWidget(self.date_payment,0,0)
        self.HomesalesPayTop.addWidget(self.inputs_payments,0,2,alignment=Qt.AlignRight)

        #SALES_OP TABLE PAYMENTS
        self.salesOpTablePayments = PyTableWidget(
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["bg_one"],
            bg_color = self.themes["app_color"]["bg_two"],
            header_horizontal_color = self.themes["app_color"]["dark_two"],
            header_vertical_color = self.themes["app_color"]["bg_three"],
            bottom_line_color = self.themes["app_color"]["bg_three"],
            grid_line_color = self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"]
            )
        self.salesOpTablePayments.setColumnCount(2)
        self.salesOpTablePayments.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.salesOpTablePayments.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.salesOpTablePayments.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.salesOpTablePayments.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.salesOpTablePayments.setMaximumHeight(2000)
        # Columns / Header
        self.column_1 = QTableWidgetItem()
        self.column_1.setTextAlignment(Qt.AlignCenter)
        self.column_1.setText(self.language["main_app"]["sale_item"])
        self.column_2 = QTableWidgetItem()
        self.column_2.setTextAlignment(Qt.AlignCenter)
        self.column_2.setText(self.language["main_app"]["combined_payments"])
        # Set column
        self.salesOpTablePayments.setHorizontalHeaderItem(0, self.column_1)
        self.salesOpTablePayments.setHorizontalHeaderItem(1, self.column_2)
        #max width
        self.salesOpTablePayments.setMaximumWidth(250)

        #PAYMENTS_LAYOUT_BUTTOM
        self.payFrameBTM = PyFrame()
        self.payFrameBTM.setMaximumHeight(100)
        self.HomesalesPayBTM = QGridLayout(self.payFrameBTM)
        self.HomesalesPayBTM.setSpacing(0)
        self.HomesalesPayBTM.setObjectName(u"HomesalesPayBTM")
        self.HomesalesPayBTM.setContentsMargins(0, 0, 0, 0)

        #DELET ROW
        self.deletNewRowPayment = PyPushButton(
            text=self.language["main_app"]["sale_delete_row"],
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["bg_three"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.deletNewRowPayment.setMaximumHeight(50)
        self.deletNewRowPayment.setMinimumHeight(33)
        self.deletNewRowPayment.setMaximumWidth(150)
        self.deletNewRowPayment.setMinimumWidth(120)
        self.HomesalesPayBTM.addWidget(self.deletNewRowPayment)

        #add to page
        self.HomesalesPay.addWidget(self.payFrameTop)
        self.HomesalesPay.addWidget(self.salesOpTablePayments)
        self.HomesalesPay.addWidget(self.payFrameBTM)

        #3
        #DELET ROW
        self.deletNewRow = PyPushButton(
            text=self.language["main_app"]["sale_delete_row"],
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["bg_three"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.deletNewRow.setMaximumHeight(50)
        self.deletNewRow.setMinimumHeight(33)
        self.deletNewRow.setMaximumWidth(150)
        self.deletNewRow.setMinimumWidth(120)
        self.ui.load_pages.Homesales3.addWidget(self.deletNewRow,alignment=Qt.AlignLeft)

        #totla price
        self.total_Op_price = PyLabel(
            text = str(500),
            color=self.themes["app_color"]["red"],
            )
        self.total_Op_price.setMaximumWidth(50)
        self.ui.load_pages.Homesales3.addWidget(self.total_Op_price)
        
        self.spaceFramecnfrm= PyFrame()
        self.spaceFramecnfrm.setMinimumHeight(33)
        self.spaceFramecnfrm.setMaximumWidth(200)
        self.ui.load_pages.Homesales3.addWidget(self.spaceFramecnfrm,alignment=Qt.AlignRight)
        #CHECOUT 
        self.checkOut = PyPushButton(
            text=self.language["main_app"]["sale_checkOut"],
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.checkOut.setMaximumHeight(50)
        self.checkOut.setMinimumHeight(33)
        self.checkOut.setMaximumWidth(150)
        self.checkOut.setMinimumWidth(120)
        self.ui.load_pages.Homesales3.addWidget(self.checkOut,alignment=Qt.AlignRight)
        
        #CONFIRM
        self.Confirm = PyPushButton(
            text=self.language["main_app"]["sale_confirm"],
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.Confirm.setMaximumHeight(50)
        self.Confirm.setMinimumHeight(33)
        self.Confirm.setMaximumWidth(150)
        self.Confirm.setMinimumWidth(120)
        self.ui.load_pages.Homesales3.addWidget(self.Confirm,alignment=Qt.AlignRight)


        #///////////////////////////// CHARTS
        #ADD COMBO BOX FOR THE TYPE OF THE CHARTS

        # CIRCULAR PROGRESS 1
        self.circular_progress_1 = PyCircularProgress(
            value = 44,
            progress_color = self.themes["app_color"]["context_color"],
            text_color = self.themes["app_color"]["text_title"],
            font_size = 14,
            bg_color = self.themes["app_color"]["dark_four"]
        )
        self.circular_progress_1.setFixedSize(120,120)
        self.ui.load_pages.lbar_chart.addWidget(self.circular_progress_1,0,0)
        self.c1lable = PyLabel(
            text = "    depends on 1",
            color=self.themes["app_color"]["text_foreground"],
        )

        # CIRCULAR PROGRESS 2
        self.circular_progress_2 = PyCircularProgress(
            value = 15,
            progress_color = self.themes["app_color"]["context_color"],
            text_color = self.themes["app_color"]["text_title"],
            font_size = 14,
            bg_color = self.themes["app_color"]["dark_four"]
        )
        self.circular_progress_2.setFixedSize(120,120)
        self.ui.load_pages.lbar_chart.addWidget(self.circular_progress_2,0,1)
        self.c2lable = PyLabel(
            text = "    depends on 2",
            color=self.themes["app_color"]["text_foreground"],
        )

        # CIRCULAR PROGRESS 3
        self.circular_progress_3 = PyCircularProgress(
            value = 75,
            progress_color = self.themes["app_color"]["context_color"],
            text_color = self.themes["app_color"]["text_title"],
            font_size = 14,
            bg_color = self.themes["app_color"]["dark_four"]
        )
        self.circular_progress_3.setFixedSize(120,120)
        self.ui.load_pages.lbar_chart.addWidget(self.circular_progress_3,0,2)
        self.c3lable = PyLabel(
            text = "    depends on 3",
            color=self.themes["app_color"]["text_foreground"],
        )

        self.ui.load_pages.lbar_chart.addWidget(self.c1lable,1,0)
        self.ui.load_pages.lbar_chart.addWidget(self.c2lable,1,1)
        self.ui.load_pages.lbar_chart.addWidget(self.c3lable,1,2)

        if self.settings["language"] == "arabic":
            self.ui.load_pages.horizontalLayout_3.addWidget(self.ui.load_pages.frame_13,alignment=Qt.AlignLeft) 
            self.ui.load_pages.horizontalLayout_3.addWidget(self.ui.load_pages.frame_12) 


            self.ui.load_pages.HomesalesName.addWidget(self.salesOrCombined)
            self.ui.load_pages.HomesalesName.addWidget(self.ui.load_pages.label_7)

    #iTEMS PAGE
        #///////////////////////////////////////////////////////////////////////
        #self.ui.load_pages.label_2.setText(self.language["main_app"]["categories"])
        self.categery_label = PyLabel(
            text = self.language["main_app"]["categories"],
            color=self.themes["app_color"]["text_foreground"],
        )
        #### cat 
        sql = "SELECT cat FROM category"
        control.execute(sql)
        catst = control.fetchall()
        cats = []
        for i in catst:
            for j in i:
                cats.append(j)
        self.btnCat = cats

        ### show the categories
        self.categery_combo = PyCombo(
            radius = 8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color = self.themes["app_color"]["dark_one"],
            combo_theme=self.btnCat,
        )
        self.categery_combo.setMinimumWidth(400)
        self.categery_combo.setMinimumHeight(33) 
        #space frame
        self.spaceFramecat= PyFrame()
        self.spaceFramecat.setMinimumHeight(33)
        self.spaceFramecat.setMaximumWidth(200)

        # PY LINE EDIT for Add Category
        self.line_edit_cat = PyLineEdit(
            text = "",
            place_holder_text = self.language["main_app"]["add_category_name"],
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.line_edit_cat.setMinimumHeight(33)
        self.line_edit_cat.setMaximumWidth(200)
        ###
        #PushButton
        self.cat = PyPushButton(
            text= self.language["main_app"]["add_category"],
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.cat.setMaximumHeight(33)
        self.cat.setMaximumWidth(120)
        self.cat.setMinimumWidth(90)
        ##

        self.subCategery_label = PyLabel(
            text = self.language["main_app"]["subCategories"],
            color=self.themes["app_color"]["text_foreground"],
        )
        #add cat and sub cat
        #combo show sub cat
        self.subCatCombo = PyCombo(
            color=self.themes["app_color"]["text_foreground"],
            bg_color = self.themes["app_color"]["bg_two"],
            radius = 8,
            combo_theme=[],
        )
        self.subCatCombo.setMaximumHeight(0)
        self.subCatCombo.setMaximumWidth(220)
        self.subCatCombo.setMinimumWidth(150)
        # PY LINE EDIT for Add SUB Category
        self.line_edit_sub_cat = PyLineEdit(
            text = "",
            place_holder_text = self.language["main_app"]["add_category_name"],
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.line_edit_sub_cat.setMaximumHeight(0)
        self.line_edit_sub_cat.setMaximumWidth(200)
        #PushButton add sub cat
        self.subCatbtn = PyPushButton(
            text= self.language["main_app"]["add_category"],
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.subCatbtn.setMaximumHeight(0)
        self.subCatbtn.setMaximumWidth(120)
        self.subCatbtn.setMinimumWidth(90)
        ##
        if self.settings["language"] == "english":
            self.ui.load_pages.horizontalLayout.addWidget(self.categery_label)
            self.ui.load_pages.horizontalLayout.addWidget(self.categery_combo,alignment=Qt.AlignLeft)
            self.ui.load_pages.horizontalLayout.addWidget(self.spaceFramecat)
            self.ui.load_pages.horizontalLayout.addWidget(self.line_edit_cat)
            self.ui.load_pages.horizontalLayout.addWidget(self.cat)
            self.ui.load_pages.horizontalLayout_2.addWidget(self.subCategery_label)
            self.ui.load_pages.horizontalLayout_2.addWidget(self.subCatCombo,alignment=Qt.AlignLeft) 
            self.ui.load_pages.horizontalLayout_2.addWidget(self.line_edit_sub_cat)
            self.ui.load_pages.horizontalLayout_2.addWidget(self.subCatbtn)
        else:
            self.ui.load_pages.horizontalLayout_2.addWidget(self.subCatbtn)
            self.ui.load_pages.horizontalLayout_2.addWidget(self.line_edit_sub_cat)
            self.ui.load_pages.horizontalLayout.addWidget(self.spaceFramecat)
            self.ui.load_pages.horizontalLayout_2.addWidget(self.subCatCombo,alignment=Qt.AlignRight) 
            self.ui.load_pages.horizontalLayout_2.addWidget(self.subCategery_label)
            self.ui.load_pages.horizontalLayout.addWidget(self.cat)
            self.ui.load_pages.horizontalLayout.addWidget(self.line_edit_cat)
            self.ui.load_pages.horizontalLayout.addWidget(self.spaceFramecat)
            self.ui.load_pages.horizontalLayout.addWidget(self.categery_combo,alignment=Qt.AlignLeft)
            self.ui.load_pages.horizontalLayout.addWidget(self.categery_label)
    ###########################Add Item
        #self.ui.load_pages.label_5.setText(self.language["main_app"]["add_item"])
        self.add_item_label = PyLabel(
            text = self.language["main_app"]["add_item"],
            color=self.themes["app_color"]["text_foreground"],
            )
        #item name
        self.Item_Name = PyLineEdit(
            text = "",
            place_holder_text =  self.language["main_app"]["add_item_name"],
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.Item_Name.setMinimumHeight(33)
        self.Item_Name.setMaximumWidth(220)

        #item price In
        self.price_in = PyLineEdit(
            text = "",
            place_holder_text = self.language["main_app"]["add_item_price_in"],
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.price_in.setMinimumHeight(33)
        self.price_in.setMaximumWidth(100)
        self.price_in.setValidator(money_val)

        #item Quantity
        self.QUantity = PyLineEdit(
            text = "",
            place_holder_text =  self.language["main_app"]["add_item_quantity"],
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.QUantity.setMinimumHeight(33)
        self.QUantity.setMaximumWidth(100)
        self.QUantity.setValidator(money_val)

        #item Price_Out
        self.Price_Out = PyLineEdit(
            text = "",
            place_holder_text =  self.language["main_app"]["add_item_price_out"],
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.Price_Out.setMinimumHeight(33)
        self.Price_Out.setMaximumWidth(100)
        self.Price_Out.setValidator(money_val)

        #item Critical_Quuantity
        self.Critical_Quuantity = PyLineEdit(
            text = "",
            place_holder_text =  self.language["main_app"]["add_item_critical"],
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.Critical_Quuantity.setMinimumHeight(33)
        self.Critical_Quuantity.setMaximumWidth(100)
        self.Critical_Quuantity.setValidator(money_val)

        #space frame
        self.spaceFrame= PyFrame()
        self.spaceFrame.setMinimumHeight(33)
        self.spaceFrame.setMaximumWidth(400)

        ##add team button
        self.AddIteam = PyPushButton(
            text=self.language["main_app"]["add_category"],
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["bg_three"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.AddIteam.setMaximumHeight(33)
        self.AddIteam.setMaximumWidth(120)
        self.AddIteam.setMinimumWidth(90)
        if self.settings["language"] == "english":
            self.ui.load_pages.horizontalLayout_4.addWidget(self.add_item_label)
            self.ui.load_pages.horizontalLayout_4.addWidget(self.Item_Name)
            self.ui.load_pages.horizontalLayout_4.addWidget(self.price_in)
            self.ui.load_pages.horizontalLayout_4.addWidget(self.QUantity)
            self.ui.load_pages.horizontalLayout_4.addWidget(self.Price_Out)
            self.ui.load_pages.horizontalLayout_4.addWidget(self.Critical_Quuantity)
            self.ui.load_pages.horizontalLayout_4.addWidget(self.spaceFrame)
            self.ui.load_pages.horizontalLayout_4.addWidget(self.AddIteam)    
        else:
            self.ui.load_pages.horizontalLayout_4.addWidget(self.AddIteam)
            self.ui.load_pages.horizontalLayout_4.addWidget(self.spaceFrame)
            self.ui.load_pages.horizontalLayout_4.addWidget(self.Critical_Quuantity) 
            self.ui.load_pages.horizontalLayout_4.addWidget(self.Price_Out)   
            self.ui.load_pages.horizontalLayout_4.addWidget(self.QUantity)
            self.ui.load_pages.horizontalLayout_4.addWidget(self.price_in)
            self.ui.load_pages.horizontalLayout_4.addWidget(self.Item_Name)
            self.ui.load_pages.horizontalLayout_4.addWidget(self.add_item_label)


        ############################################
    # TABLE WIDGETS
        self.table_widget = PyTableWidget(
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["bg_one"],
            bg_color = self.themes["app_color"]["bg_two"],
            header_horizontal_color = self.themes["app_color"]["dark_two"],
            header_vertical_color = self.themes["app_color"]["bg_three"],
            bottom_line_color = self.themes["app_color"]["bg_three"],
            grid_line_color = self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"]
        )
        
        self.table_widget.setColumnCount(6)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table_widget.setMinimumHeight(300)
        self.table_widget.setMaximumHeight(55500)
        # Columns / Header
        self.column_1 = QTableWidgetItem()
        self.column_1.setTextAlignment(Qt.AlignCenter)
        self.column_1.setText( self.language["main_app"]["show_item_name"])

        self.column_2 = QTableWidgetItem()
        self.column_2.setTextAlignment(Qt.AlignCenter)
        self.column_2.setText( self.language["main_app"]["show_item_quantity"])

        self.column_3 = QTableWidgetItem()
        self.column_3.setTextAlignment(Qt.AlignCenter)
        self.column_3.setText( self.language["main_app"]["show_item_date_in"])

        self.column_4 = QTableWidgetItem()
        self.column_4.setTextAlignment(Qt.AlignCenter)
        self.column_4.setText( self.language["main_app"]["show_item_price_in"])

        self.column_5 = QTableWidgetItem()
        self.column_5.setTextAlignment(Qt.AlignCenter)
        self.column_5.setText( self.language["main_app"]["show_item_price_out"])

        self.column_6 = QTableWidgetItem()
        self.column_6.setTextAlignment(Qt.AlignCenter)
        self.column_6.setText( self.language["main_app"]["show_item_critical"])

        # Set column
        self.table_widget.setHorizontalHeaderItem(0, self.column_1)
        self.table_widget.setHorizontalHeaderItem(1, self.column_2)
        self.table_widget.setHorizontalHeaderItem(2, self.column_3)
        self.table_widget.setHorizontalHeaderItem(3, self.column_4)
        self.table_widget.setHorizontalHeaderItem(4, self.column_5)
        self.table_widget.setHorizontalHeaderItem(5, self.column_6)

        # Add name 
        self.ui.load_pages.verticalLayout.addWidget(self.table_widget)
        self.table_widget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table_widget.sortItems(0, Qt.AscendingOrder)#AA--ZZ
        #self.table_widget.setTextAlignment(Qt.AlignHCenter) 

        #PAYMENTS_LAYOUT
        self.CntrlFrameitem = PyFrame()
        self.CntrlFrameitem.setMaximumHeight(50)
        self.itemLayCntrl = QGridLayout(self.CntrlFrameitem)
        self.itemLayCntrl.setSpacing(6)
        self.itemLayCntrl.setObjectName(u"itemLayCntrl")
        self.itemLayCntrl.setContentsMargins(0, 0, 0, 0)

        #button
        self.DeleteItem = PyPushButton(
            text=self.language["main_app"]["delete"],
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["red"],
            bg_color_hover=self.themes["app_color"]["bg_one"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
            )
        self.DeleteItem.setMaximumWidth(200)
        self.DeleteItem.setMinimumHeight(33)

        self.selectItem = PyPushButton(
            text=self.language["main_app"]["ready"],
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["bg_one"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
            )
        self.selectItem.setMaximumWidth(200)
        self.selectItem.setMinimumHeight(33)

        self.updateItem = PyPushButton(
            text=self.language["main_app"]["update"],
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["bg_one"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
            )
        self.updateItem.setMaximumWidth(200)
        self.updateItem.setMinimumHeight(33)

        self.itemLayCntrl.addWidget(self.DeleteItem,0,0)
        self.itemLayCntrl.addWidget(self.selectItem,0,1)

        self.ui.load_pages.verticalLayout.addWidget(self.CntrlFrameitem)

    #SALES PAGE
        #////////////////////////////////////////////////////////////////
        ############################################
        self.ui.load_pages.label_6.setText(self.language["main_app"]["sales_title"])
         #sales btn
        self.salesbtn = PyPushButton(
            text=self.language["main_app"]["sales"],
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["bg_three"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.salesbtn.setMaximumHeight(33)
        self.salesbtn.setMaximumWidth(120)
        self.ui.load_pages.horizontalLayout_5.addWidget(self.salesbtn)
        #combined btn
        self.combinedbtn = PyPushButton(
            text=self.language["main_app"]["combined"],
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["bg_three"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.combinedbtn.setMaximumHeight(33)
        self.combinedbtn.setMaximumWidth(120)
        self.ui.load_pages.horizontalLayout_5.addWidget(self.combinedbtn)


        sql = "SELECT cust_name FROM combined"
        control.execute(sql)
        itemcom = control.fetchall()
        itemscom = []
        for i in itemcom:
            itemscom.append(i[0])
        completecom = itemscom
        completercom = QCompleter(completecom)

        #PAYMENTS_LAYOUT
        self.payFrameCom = PyFrame()
        self.payFrameCom.setMaximumHeight(50 )
        self.comLay = QGridLayout(self.payFrameCom)
        self.comLay.setSpacing(6)
        self.comLay.setObjectName(u"comLay")
        self.comLay.setContentsMargins(0, 0, 0, 0)

        self.inputs_com = PyInputs(
            color = self.themes["app_color"]["text_foreground"],
            bg_color = self.themes["app_color"]["bg_two"],
            )
        self.inputs_com.line_edit_widget.setMaximumWidth(350)
        self.inputs_com.line_edit_widget.setPlaceholderText("NAME")
        self.inputs_com.line_edit_widget.setCompleter(completercom)
        
        self.customer_Name_com = PyLineEdit(
            text = "",
            place_holder_text = self.language["main_app"]["customer_left"],
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
            )
        self.customer_Name_com.setMaximumWidth(150)
        #button
        self.add_pay_com = PyPushButton(
            text=self.language["main_app"]["pay"],
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["bg_one"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
            )
        self.add_pay_com.setMinimumWidth(100)
        self.add_pay_com.setMinimumHeight(30)
        self.comLay.addWidget(self.inputs_com,0,1)
        self.comLay.addWidget(self.customer_Name_com,0,2)
        self.comLay.addWidget(self.add_pay_com,0,3)

        self.ui.load_pages.verticalLayout_c1.addWidget(self.payFrameCom)
    # TABLE WIDGETS SALES
        self.payFrameSalesTabes = PyFrame()
        self.payFrameSalesTabes.setMaximumHeight(50000)
        self.salesLayTables = QGridLayout(self.payFrameSalesTabes)
        self.salesLayTables.setSpacing(6)
        self.salesLayTables.setObjectName(u"salesLayTables")
        self.salesLayTables.setContentsMargins(0, 0, 0, 0)
        self.ui.load_pages.verticalLayout_sales.addWidget(self.payFrameSalesTabes)

        self.table_widget_Sales = PyTableWidget(
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["bg_one"],
            bg_color = self.themes["app_color"]["bg_two"],
            header_horizontal_color = self.themes["app_color"]["dark_two"],
            header_vertical_color = self.themes["app_color"]["bg_three"],
            bottom_line_color = self.themes["app_color"]["bg_three"],
            grid_line_color = self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.table_widget_Sales.setColumnCount(8)
        self.table_widget_Sales.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget_Sales.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_widget_Sales.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table_widget_Sales.setSelectionBehavior(QAbstractItemView.SelectRows)
        #self.table_widget_Sales.setMinimumHeight(400)
        self.table_widget_Sales.setMaximumHeight(22200)
        # Columns / Header
        self.column_1 = QTableWidgetItem()
        self.column_1.setTextAlignment(Qt.AlignCenter)
        self.column_1.setText(self.language["main_app"]["sales_id"])

        self.column_2 = QTableWidgetItem()
        self.column_2.setTextAlignment(Qt.AlignCenter)
        self.column_2.setText(self.language["main_app"]["sales_customer"])

        self.column_3 = QTableWidgetItem()
        self.column_3.setTextAlignment(Qt.AlignCenter)
        self.column_3.setText(self.language["main_app"]["sales_total_price"])

        self.column_4 = QTableWidgetItem()
        self.column_4.setTextAlignment(Qt.AlignCenter)
        self.column_4.setText(self.language["main_app"]["sales_paid"])

        self.column_5 = QTableWidgetItem()
        self.column_5.setTextAlignment(Qt.AlignCenter)
        self.column_5.setText(self.language["main_app"]["sales_left"])

        self.column_6 = QTableWidgetItem()
        self.column_6.setTextAlignment(Qt.AlignCenter)
        self.column_6.setText(self.language["main_app"]["sales_date"])

        self.column_7 = QTableWidgetItem()
        self.column_7.setTextAlignment(Qt.AlignCenter)
        self.column_7.setText(self.language["main_app"]["sales_date"])

        self.column_8 = QTableWidgetItem()
        self.column_8.setTextAlignment(Qt.AlignCenter)
        self.column_8.setText(self.language["main_app"]["sales_seller"])

        # Set column
        self.table_widget_Sales.setHorizontalHeaderItem(0, self.column_1)
        self.table_widget_Sales.setHorizontalHeaderItem(1, self.column_2)
        self.table_widget_Sales.setHorizontalHeaderItem(2, self.column_3)
        self.table_widget_Sales.setHorizontalHeaderItem(3, self.column_4)
        self.table_widget_Sales.setHorizontalHeaderItem(4, self.column_5)
        self.table_widget_Sales.setHorizontalHeaderItem(5, self.column_6)
        self.table_widget_Sales.setHorizontalHeaderItem(6, self.column_7)
        self.table_widget_Sales.setHorizontalHeaderItem(9, self.column_8)
        #//////
        #replace the crnt_subcat by the first subacat in the first cat
        #/////
       
        sql = "SELECT COUNT(op_date) FROM sales"
        control.execute(sql)
        h = control.fetchone()
        sql = "SELECT op_id, cust_name, cartTotal, money_paid, money_left, op_date, op_time, emp_name FROM sales"
        control.execute(sql)
        f = control.fetchall()

        for x in range(h[0]):
            row_number = self.table_widget_Sales.rowCount()
            self.table_widget_Sales.insertRow(row_number) 
            # Insert row
            for i in range(7):
                self.table_widget_Sales.setItem(row_number, i, QTableWidgetItem(str(f[x][i])))
        #self.ui.load_pages.verticalLayout_sales.addWidget(self.table_widget_Sales)
        self.salesLayTables.addWidget(self.table_widget_Sales,0,0)


        # TABLE WIDGETS CUSTOMERS WHO HAS MONEY LEFT
        self.table_Sales_cart = PyTableWidget(
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["bg_one"],
            bg_color = self.themes["app_color"]["bg_two"],
            header_horizontal_color = self.themes["app_color"]["dark_two"],
            header_vertical_color = self.themes["app_color"]["bg_three"],
            bottom_line_color = self.themes["app_color"]["bg_three"],
            grid_line_color = self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.table_Sales_cart.setColumnCount(3)
        self.table_Sales_cart.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_Sales_cart.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_Sales_cart.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table_Sales_cart.setSelectionBehavior(QAbstractItemView.SelectRows)
        #self.table_Sales_cart.setMinimumHeight(400)
        self.table_Sales_cart.setMaximumHeight(2000)
        self.table_Sales_cart.setMaximumWidth(300)
        self.table_Sales_cart.setObjectName(u"table_Sales_cart")
        # Columns / Header

        self.column_1 = QTableWidgetItem()
        self.column_1.setTextAlignment(Qt.AlignCenter)
        self.column_1.setText(self.language["main_app"]["combined_items"])

        self.column_2 = QTableWidgetItem()
        self.column_2.setTextAlignment(Qt.AlignCenter)
        self.column_2.setText(self.language["main_app"]["sale_price"])

        self.column_3 = QTableWidgetItem()
        self.column_3.setTextAlignment(Qt.AlignCenter)
        self.column_3.setText(self.language["main_app"]["sale_quantity"])

        # Set column
        self.table_Sales_cart.setHorizontalHeaderItem(0, self.column_1)
        self.table_Sales_cart.setHorizontalHeaderItem(1, self.column_2)
        self.table_Sales_cart.setHorizontalHeaderItem(2, self.column_3)
        #BTNS
        self.CntrlFrameSales = PyFrame()
        self.CntrlFrameSales.setMaximumHeight(50)
        self.SalesLayCntrl = QGridLayout(self.CntrlFrameSales)
        self.SalesLayCntrl.setSpacing(6)
        self.SalesLayCntrl.setObjectName(u"SalesLayCntrl")
        self.SalesLayCntrl.setContentsMargins(0, 0, 0, 0)

        #button
        self.showdtlsSales = PyPushButton(
            text=self.language["main_app"]["combined_details"],
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["bg_one"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
            )
        #button
        
        self.showdtlsSales.setMaximumWidth(200)
        self.showdtlsSales.setMinimumHeight(33)
       
        self.SalesLayCntrl.addWidget(self.showdtlsSales,0,0)

        self.ui.load_pages.verticalLayout_sales.addWidget(self.CntrlFrameSales)
    #//////////////////##############################################
    # TABLE WIDGETS combined//
        ############################################
        self.ui.load_pages.label_4.setText(self.language["main_app"]["combined_title"])
        self.table_combined = PyTableWidget(
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["bg_one"],
            bg_color = self.themes["app_color"]["bg_two"],
            header_horizontal_color = self.themes["app_color"]["dark_two"],
            header_vertical_color = self.themes["app_color"]["bg_three"],
            bottom_line_color = self.themes["app_color"]["bg_three"],
            grid_line_color = self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"]
        )
        
        self.table_combined.setColumnCount(8)
        self.table_combined.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_combined.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table_combined.setSelectionBehavior(QAbstractItemView.SelectRows)
        #self.table_combined.setMinimumHeight(400)
        #self.table_combined.setMaximumHeight(2000)
        # Columns / Header
        self.column_1 = QTableWidgetItem()
        self.column_1.setTextAlignment(Qt.AlignCenter)
        self.column_1.setText(self.language["main_app"]["sales_id"])

        self.column_2 = QTableWidgetItem()
        self.column_2.setTextAlignment(Qt.AlignCenter)
        self.column_2.setText(self.language["main_app"]["sales_customer"])

        self.column_3 = QTableWidgetItem()
        self.column_3.setTextAlignment(Qt.AlignCenter)
        self.column_3.setText(self.language["main_app"]["sales_total_price"])

        self.column_4 = QTableWidgetItem()
        self.column_4.setTextAlignment(Qt.AlignCenter)
        self.column_4.setText(self.language["main_app"]["sales_paid"])

        self.column_5 = QTableWidgetItem()
        self.column_5.setTextAlignment(Qt.AlignCenter)
        self.column_5.setText(self.language["main_app"]["sales_left"])

        self.column_6 = QTableWidgetItem()
        self.column_6.setTextAlignment(Qt.AlignCenter)
        self.column_6.setText(self.language["main_app"]["sales_date"])

        self.column_7 = QTableWidgetItem()
        self.column_7.setTextAlignment(Qt.AlignCenter)
        self.column_7.setText(self.language["main_app"]["sales_date"])

        self.column_8 = QTableWidgetItem()
        self.column_8.setTextAlignment(Qt.AlignCenter)
        self.column_8.setText(self.language["main_app"]["sales_seller"])

        # Set column
        self.table_combined.setHorizontalHeaderItem(0, self.column_1)
        self.table_combined.setHorizontalHeaderItem(1, self.column_2)
        self.table_combined.setHorizontalHeaderItem(2, self.column_3)
        self.table_combined.setHorizontalHeaderItem(3, self.column_4)
        self.table_combined.setHorizontalHeaderItem(4, self.column_5)
        self.table_combined.setHorizontalHeaderItem(5, self.column_6)
        self.table_combined.setHorizontalHeaderItem(6, self.column_7)
        self.table_combined.setHorizontalHeaderItem(9, self.column_8)
            
       
        sql = "SELECT COUNT(op_date) FROM combined"
        control.execute(sql)
        h = control.fetchone()
        sql = "SELECT op_id, cust_name, cartTotal, money_paid, money_left, op_date, op_time, emp_name FROM combined"
        control.execute(sql)
        f = control.fetchall()

        for x in range(h[0]):
            row_number = self.table_combined.rowCount()
            self.table_combined.insertRow(row_number) 
            # Insert row
            for i in range(7):
                self.table_combined.setItem(row_number, i, QTableWidgetItem(str(f[x][i])))

        self.customer_Name = PyLabel(
            text = self.language["main_app"]["combined_customer"],
            color=self.themes["app_color"]["text_foreground"],
            )
        self.ui.load_pages.verticalLayout_c1.addWidget(self.table_combined)
        self.table_combined.setEditTriggers(QTableWidget.NoEditTriggers)

        ############################################
        # TABLE WIDGETS COMBINED_detiled
        self.payFrameCombinedShowdtlsS = PyFrame()
        self.payFrameCombinedShowdtlsS.setMaximumHeight(40)
        self.cominedShowdtlsLay = QGridLayout(self.payFrameCombinedShowdtlsS)
        self.cominedShowdtlsLay.setSpacing(6)
        self.cominedShowdtlsLay.setObjectName(u"cominedShowdtlsLay")
        self.cominedShowdtlsLay.setContentsMargins(0, 5, 0, 5)

        self.customer_Name_combined = PyLabel(
            text = self.language["main_app"]["customer_Name"],
            color=self.themes["app_color"]["text_foreground"],
            )
        self.showCombinedDetails = PyPushButton(
            text=self.language["main_app"]["combined_details"],
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["bg_one"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
            )
        self.showCombinedDetails.setMinimumHeight(30)
        self.showCombinedDetails.setMaximumWidth(250)
        self.readyCombined = PyPushButton(
            text=self.language["main_app"]["ready"],
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["bg_one"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
            )
        self.readyCombined.setMinimumHeight(30)
        self.readyCombined.setMaximumWidth(250)
        self.cominedShowdtlsLay.addWidget(self.customer_Name_combined,0,0)
        self.cominedShowdtlsLay.addWidget(self.showCombinedDetails,0,2)
        self.cominedShowdtlsLay.addWidget(self.readyCombined,0,1)


        self.ui.load_pages.verticalLayout_c2.addWidget(self.payFrameCombinedShowdtlsS)

        ############################################
        # TABLE WIDGETS COMBINED_detiled
        self.payFrameCombineddtls = PyFrame()
        #self.payFrameCombineddtls.setMaximumHeight(300)
        self.comineddtlsLay = QGridLayout(self.payFrameCombineddtls)
        self.comineddtlsLay.setSpacing(6)
        self.comineddtlsLay.setObjectName(u"comineddtlsLay")
        self.comineddtlsLay.setContentsMargins(0, 0, 0, 0)

        #self.ui.load_pages.verticalLayout_c2.addWidget(self.payFrameCombineddtls)
        self.table_widget_Combined = PyTableWidget(
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["bg_one"],
            bg_color = self.themes["app_color"]["bg_two"],
            header_horizontal_color = self.themes["app_color"]["dark_two"],
            header_vertical_color = self.themes["app_color"]["bg_three"],
            bottom_line_color = self.themes["app_color"]["bg_three"],
            grid_line_color = self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"]
        )
        
        self.table_widget_Combined.setColumnCount(3)
        self.table_widget_Combined.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget_Combined.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_widget_Combined.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table_widget_Combined.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_widget_Combined.setMaximumHeight(2000)
        
        # Columns / Header=

        self.column_1 = QTableWidgetItem()
        self.column_1.setTextAlignment(Qt.AlignCenter)
        self.column_1.setText(self.language["main_app"]["combined_items"])

        self.column_2 = QTableWidgetItem()
        self.column_2.setTextAlignment(Qt.AlignCenter)
        self.column_2.setText(self.language["main_app"]["combined_price"])

        self.column_3 = QTableWidgetItem()
        self.column_3.setTextAlignment(Qt.AlignCenter)
        self.column_3.setText(self.language["main_app"]["combined_quantity"])

        # Set column
        self.table_widget_Combined.setHorizontalHeaderItem(0, self.column_1)
        self.table_widget_Combined.setHorizontalHeaderItem(1, self.column_2)
        self.table_widget_Combined.setHorizontalHeaderItem(2, self.column_3)
        

        # TABLE WIDGETS COMBINED_Payments
        self.table_widget_Combined_payment = PyTableWidget(
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["bg_one"],
            bg_color = self.themes["app_color"]["bg_two"],
            header_horizontal_color = self.themes["app_color"]["dark_two"],
            header_vertical_color = self.themes["app_color"]["bg_three"],
            bottom_line_color = self.themes["app_color"]["bg_three"],
            grid_line_color = self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"]
        )
        
        self.table_widget_Combined_payment.setColumnCount(6)
        self.table_widget_Combined_payment.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget_Combined_payment.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_widget_Combined_payment.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_widget_Combined_payment.setMaximumHeight(2000)
        
        # Columns / Header
        self.column_1 = QTableWidgetItem()
        self.column_1.setTextAlignment(Qt.AlignCenter)
        self.column_1.setText(self.language["main_app"]["Payment"])

        self.column_2 = QTableWidgetItem()
        self.column_2.setTextAlignment(Qt.AlignCenter)
        self.column_2.setText(self.language["main_app"]["Payment_date"])

        self.column_3 = QTableWidgetItem()
        self.column_3.setTextAlignment(Qt.AlignCenter)
        self.column_3.setText(self.language["main_app"]["sales_paid"])

        self.column_4 = QTableWidgetItem()
        self.column_4.setTextAlignment(Qt.AlignCenter)
        self.column_4.setText(self.language["main_app"]["sales_date"])

        self.column_5 = QTableWidgetItem()
        self.column_5.setTextAlignment(Qt.AlignCenter)
        self.column_5.setText(self.language["main_app"]["customer_time"])

        self.column_6 = QTableWidgetItem()
        self.column_6.setTextAlignment(Qt.AlignCenter)
        self.column_6.setText(self.language["main_app"]["combined_seller"])

        # Set column
        self.table_widget_Combined_payment.setHorizontalHeaderItem(0, self.column_1)
        self.table_widget_Combined_payment.setHorizontalHeaderItem(1, self.column_2)
        self.table_widget_Combined_payment.setHorizontalHeaderItem(2, self.column_3)
        self.table_widget_Combined_payment.setHorizontalHeaderItem(3, self.column_4)
        self.table_widget_Combined_payment.setHorizontalHeaderItem(4, self.column_5)
        self.table_widget_Combined_payment.setHorizontalHeaderItem(5, self.column_6)
        self.ConfirmUpdatecart = PyPushButton(
            text= self.language["main_app"]["sale_confirm"],
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.ConfirmUpdatecart.setMaximumHeight(33)
        self.ConfirmUpdatecart.setMinimumHeight(33)
        self.ConfirmUpdatecart.setMaximumWidth(120)        
        self.ConfirmupdatePayments = PyPushButton(
            text= self.language["main_app"]["sale_confirm"],
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.ConfirmupdatePayments.setMaximumHeight(33)
        self.ConfirmupdatePayments.setMinimumHeight(33)
        self.ConfirmupdatePayments.setMaximumWidth(120)
        self.comineddtlsLay.addWidget(self.table_widget_Combined,0,0)
        self.comineddtlsLay.addWidget(self.table_widget_Combined_payment,0,1)
        self.comineddtlsLay.addWidget(self.ConfirmUpdatecart,1,0)
        self.comineddtlsLay.addWidget(self.ConfirmupdatePayments,1,1)
    #CUSTOMERS
    #//////////////////##############################################
        self.ui.load_pages.label_8.setText(self.language["main_app"]["customer"])
        sql = "SELECT cust_name FROM sales"
        control.execute(sql)
        item = control.fetchall()
        items = []
        for i in item:
            items.append(i[0])
        complete = items
        completer = QCompleter(complete)

        #PAYMENTS_LAYOUT
        self.payFrameCust = PyFrame()
        self.payFrameCust.setMaximumHeight(50 )
        self.custLay = QGridLayout(self.payFrameCust)
        self.custLay.setSpacing(6)
        self.custLay.setObjectName(u"custLay")
        self.custLay.setContentsMargins(0, 0, 0, 0)

        self.inputs_cust = PyInputs(
            color = self.themes["app_color"]["text_foreground"],
            bg_color = self.themes["app_color"]["bg_two"],
            )
        self.inputs_cust.line_edit_widget.setMaximumWidth(350)
        self.inputs_cust.line_edit_widget.setPlaceholderText("NAME")
        self.inputs_cust.line_edit_widget.setCompleter(completer)
        
        self.customer_Name_sale = PyLineEdit(
            text = "",
            place_holder_text = self.language["main_app"]["customer_left"],
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
            )
        self.customer_Name_sale.setMaximumWidth(150)
        #button
        self.add_pay_cust = PyPushButton(
            text=self.language["main_app"]["pay"],
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["bg_one"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
            )
        self.add_pay_cust.setMinimumWidth(100)
        self.add_pay_cust.setMinimumHeight(30)
        self.custLay.addWidget(self.inputs_cust,0,1)
        self.custLay.addWidget(self.customer_Name_sale,0,2)
        self.custLay.addWidget(self.add_pay_cust,0,3)

        self.ui.load_pages.verticalLayout_customers.addWidget(self.payFrameCust)

        # TABLE WIDGETS CUSTOMERS WHO HAS MONEY LEFT
        self.payFrameCustTabes = PyFrame()
        self.payFrameCustTabes.setMaximumHeight(50000)

        self.custLayTables = QGridLayout(self.payFrameCustTabes)
        self.custLayTables.setSpacing(6)
        self.custLayTables.setObjectName(u"custLayTables")
        self.custLayTables.setContentsMargins(0, 0, 0, 0)
        self.ui.load_pages.verticalLayout_customers.addWidget(self.payFrameCustTabes)

        self.table_Customers = PyTableWidget(
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["bg_one"],
            bg_color = self.themes["app_color"]["bg_two"],
            header_horizontal_color = self.themes["app_color"]["dark_two"],
            header_vertical_color = self.themes["app_color"]["bg_three"],
            bottom_line_color = self.themes["app_color"]["bg_three"],
            grid_line_color = self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.table_Customers.setColumnCount(7)
        self.table_Customers.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_Customers.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_Customers.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table_Customers.setSelectionBehavior(QAbstractItemView.SelectRows)
        #self.table_Customers.setMinimumHeight(400)
        self.table_Customers.setMaximumHeight(2000)
        # Columns / Header

        self.column_1 = QTableWidgetItem()
        self.column_1.setTextAlignment(Qt.AlignCenter)
        self.column_1.setText(self.language["main_app"]["customer_Name"])

        self.column_2 = QTableWidgetItem()
        self.column_2.setTextAlignment(Qt.AlignCenter)
        self.column_2.setText(self.language["main_app"]["customer_operation"])

        self.column_3 = QTableWidgetItem()
        self.column_3.setTextAlignment(Qt.AlignCenter)
        self.column_3.setText(self.language["main_app"]["customer_date"])

        self.column_4 = QTableWidgetItem()
        self.column_4.setTextAlignment(Qt.AlignCenter)
        self.column_4.setText(self.language["main_app"]["customer_time"])

        self.column_5 = QTableWidgetItem()
        self.column_5.setTextAlignment(Qt.AlignCenter)
        self.column_5.setText(self.language["main_app"]["customer_paid"])

        self.column_6 = QTableWidgetItem()
        self.column_6.setTextAlignment(Qt.AlignCenter)
        self.column_6.setText(self.language["main_app"]["customer_left"])

        self.column_7 = QTableWidgetItem()
        self.column_7.setTextAlignment(Qt.AlignCenter)
        self.column_7.setText(self.language["main_app"]["customer_seller"])

        # Set column
        self.table_Customers.setHorizontalHeaderItem(0, self.column_1)
        self.table_Customers.setHorizontalHeaderItem(1, self.column_2)
        self.table_Customers.setHorizontalHeaderItem(2, self.column_3)
        self.table_Customers.setHorizontalHeaderItem(3, self.column_4)
        self.table_Customers.setHorizontalHeaderItem(4, self.column_5)
        self.table_Customers.setHorizontalHeaderItem(5, self.column_6)
        self.table_Customers.setHorizontalHeaderItem(6, self.column_7)
       
        sql = "SELECT COUNT(op_date) FROM sales"
        control.execute(sql)
        h = control.fetchone()
        sql = "SELECT cust_name, op_id, op_date, op_time, money_paid, money_left, emp_name FROM sales"
        control.execute(sql)
        f = control.fetchall()

        for x in range(h[0]):
            if f[x][5] != 0 and f[x][5] != "" and  f[x][5] != "0" and  f[x][5] != None:
                row_number = self.table_Customers.rowCount()
                self.table_Customers.insertRow(row_number) 
                # Insert row
                for i in range(7):
                    self.table_Customers.setItem(row_number, i, QTableWidgetItem(str(f[x][i])))

        self.custLayTables.addWidget(self.table_Customers,0,0,1,2)
        self.table_Customers.setEditTriggers(QTableWidget.NoEditTriggers)
        


        # TABLE WIDGETS CUSTOMERS WHO HAS MONEY LEFT
        self.table_Customers_cart = PyTableWidget(
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["bg_one"],
            bg_color = self.themes["app_color"]["bg_two"],
            header_horizontal_color = self.themes["app_color"]["dark_two"],
            header_vertical_color = self.themes["app_color"]["bg_three"],
            bottom_line_color = self.themes["app_color"]["bg_three"],
            grid_line_color = self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.table_Customers_cart.setColumnCount(3)
        self.table_Customers_cart.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_Customers_cart.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_Customers_cart.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table_Customers_cart.setSelectionBehavior(QAbstractItemView.SelectRows)
        #self.table_Customers_cart.setMinimumHeight(400)
        self.table_Customers_cart.setMaximumHeight(2000)
        #self.table_Customers_cart.setMaximumWidth(300)
        self.table_Customers_cart.setObjectName(u"table_Customers_cart")
        # Columns / Header

        self.column_1 = QTableWidgetItem()
        self.column_1.setTextAlignment(Qt.AlignCenter)
        self.column_1.setText(self.language["main_app"]["combined_items"])

        self.column_2 = QTableWidgetItem()
        self.column_2.setTextAlignment(Qt.AlignCenter)
        self.column_2.setText(self.language["main_app"]["sale_price"])

        self.column_3 = QTableWidgetItem()
        self.column_3.setTextAlignment(Qt.AlignCenter)
        self.column_3.setText(self.language["main_app"]["sale_quantity"])

        # Set column
        self.table_Customers_cart.setHorizontalHeaderItem(0, self.column_1)
        self.table_Customers_cart.setHorizontalHeaderItem(1, self.column_2)
        self.table_Customers_cart.setHorizontalHeaderItem(2, self.column_3)

        #self.custLayTables.addWidget(self.table_Customers_cart,0,1)
        #payment
        self.table_Customers_payments = PyTableWidget(
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["bg_one"],
            bg_color = self.themes["app_color"]["bg_two"],
            header_horizontal_color = self.themes["app_color"]["dark_two"],
            header_vertical_color = self.themes["app_color"]["bg_three"],
            bottom_line_color = self.themes["app_color"]["bg_three"],
            grid_line_color = self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.table_Customers_payments.setColumnCount(4)
        self.table_Customers_payments.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_Customers_payments.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_Customers_payments.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table_Customers_payments.setSelectionBehavior(QAbstractItemView.SelectRows)
        #self.table_Customers_payments.setMinimumHeight(400)
        self.table_Customers_payments.setMaximumHeight(2000)
        #self.table_Customers_payments.setMaximumWidth(300)
        self.table_Customers_payments.setObjectName(u"table_Customers_payments")
        # Columns / Header

        self.column_1 = QTableWidgetItem()
        self.column_1.setTextAlignment(Qt.AlignCenter)
        self.column_1.setText(self.language["main_app"]["sale_paid"])

        self.column_2 = QTableWidgetItem()
        self.column_2.setTextAlignment(Qt.AlignCenter)
        self.column_2.setText(self.language["main_app"]["sales_date"])

        self.column_3 = QTableWidgetItem()
        self.column_3.setTextAlignment(Qt.AlignCenter)
        self.column_3.setText(self.language["main_app"]["customer_time"])

        self.column_4 = QTableWidgetItem()
        self.column_4.setTextAlignment(Qt.AlignCenter)
        self.column_4.setText(self.language["main_app"]["sales_seller"])

        # Set column
        self.table_Customers_payments.setHorizontalHeaderItem(0, self.column_1)
        self.table_Customers_payments.setHorizontalHeaderItem(1, self.column_2)
        self.table_Customers_payments.setHorizontalHeaderItem(2, self.column_3)
        self.table_Customers_payments.setHorizontalHeaderItem(3, self.column_4)
        ###//////

        #PAYMENTS_LAYOUT
        self.CntrlFrameCust = PyFrame()
        self.CntrlFrameCust.setMaximumHeight(50)
        self.custLayCntrl = QGridLayout(self.CntrlFrameCust)
        self.custLayCntrl.setSpacing(6)
        self.custLayCntrl.setObjectName(u"custLayCntrl")
        self.custLayCntrl.setContentsMargins(0, 0, 0, 0)

        #button
        self.showdtls_cust = PyPushButton(
            text=self.language["main_app"]["combined_details"],
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["bg_one"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
            )
        self.showdtls_cust.setMaximumWidth(200)
        self.showdtls_cust.setMinimumHeight(33)

        self.ReadyForPay = PyPushButton(
            text=self.language["main_app"]["ready"],
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["bg_one"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
            )
        self.ReadyForPay.setMaximumWidth(200)
        self.ReadyForPay.setMinimumHeight(33)

        self.custLayCntrl.addWidget(self.showdtls_cust,0,0)
        self.custLayCntrl.addWidget(self.ReadyForPay,0,1)

        self.ui.load_pages.verticalLayout_customers.addWidget(self.CntrlFrameCust)
    #OUTCOME
    #//////////////////##############################################
        self.ui.load_pages.label_12.setText(self.language["main_app"]["outcome"])
        #frame as a space
        self.outCome_frame_0 = PyFrame()
        #line edit
        self.line_edit_OutCome_Dics = PyLineEdit(
            text = "",
            place_holder_text = self.language["main_app"]["outcome_disc"],
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        #line edit
        self.line_edit_OutCome = PyLineEdit(
            text = "",
            place_holder_text = self.language["main_app"]["outcome_Price"],
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        #frame as a space
        self.outCome_frame = PyFrame()
        #button
        self.Add_Outcome = PyPushButton(
            text=self.language["main_app"]["outcome_btn"],
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["bg_one"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
            )

        self.outCome_frame_2 = PyFrame()
        #set size
        self.outCome_frame_2.setMinimumHeight(33)
        self.outCome_frame_2.setMaximumWidth(400)
        #self.line_edit_OutCome_Dics.setMaximumWidth(400)
        self.line_edit_OutCome_Dics.setMinimumHeight(33)
        self.line_edit_OutCome.setMaximumWidth(111)
        self.line_edit_OutCome.setMinimumHeight(33)
        self.line_edit_OutCome.setValidator(money_val)
        self.Add_Outcome.setMinimumHeight(33)
        self.outCome_frame.setMinimumHeight(33)
        self.outCome_frame.setMaximumWidth(200)
        self.Add_Outcome.setMaximumWidth(90)
        self.outCome_frame_2.setMinimumHeight(33)
        self.outCome_frame_2.setMaximumWidth(400)
        #add to layout
        if self.settings["language"] == "english":
            self.ui.load_pages.OutCome_layout_1.addWidget(self.outCome_frame_0)
            self.ui.load_pages.OutCome_layout_1.addWidget(self.line_edit_OutCome_Dics)
            self.ui.load_pages.OutCome_layout_1.addWidget(self.line_edit_OutCome)
            self.ui.load_pages.OutCome_layout_1.addWidget(self.outCome_frame)
            self.ui.load_pages.OutCome_layout_1.addWidget(self.Add_Outcome)
            self.ui.load_pages.OutCome_layout_1.addWidget(self.outCome_frame_2)
        else:
            self.ui.load_pages.OutCome_layout_1.addWidget(self.outCome_frame_0)
            self.ui.load_pages.OutCome_layout_1.addWidget(self.Add_Outcome)
            self.ui.load_pages.OutCome_layout_1.addWidget(self.outCome_frame)
            self.ui.load_pages.OutCome_layout_1.addWidget(self.line_edit_OutCome)
            self.ui.load_pages.OutCome_layout_1.addWidget(self.line_edit_OutCome_Dics)
            self.ui.load_pages.OutCome_layout_1.addWidget(self.outCome_frame_2)

        # OUTCOME TABLE
        self.OutCome_table_widget = PyTableWidget(
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["bg_one"],
            bg_color = self.themes["app_color"]["bg_two"],
            header_horizontal_color = self.themes["app_color"]["dark_two"],
            header_vertical_color = self.themes["app_color"]["bg_three"],
            bottom_line_color = self.themes["app_color"]["bg_three"],
            grid_line_color = self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"]
        )
        
        self.OutCome_table_widget.setColumnCount(3)
        #self.OutCome_table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.OutCome_table_widget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.OutCome_table_widget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.OutCome_table_widget.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.OutCome_table_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.OutCome_table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.OutCome_table_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.OutCome_table_widget.setMinimumHeight(400)
        self.OutCome_table_widget.setMaximumHeight(55500)
        # Columns / Header
        self.column_1 = QTableWidgetItem()
        self.column_1.setTextAlignment(Qt.AlignCenter)
        self.column_1.setText(self.language["main_app"]["outcome_details"])

        self.column_2 = QTableWidgetItem()
        self.column_2.setTextAlignment(Qt.AlignCenter)
        self.column_2.setText(self.language["main_app"]["outcome_date"])

        self.column_3 = QTableWidgetItem()
        self.column_3.setTextAlignment(Qt.AlignCenter)
        self.column_3.setText(self.language["main_app"]["outcome_Price"])

        # Set column
        self.OutCome_table_widget.setHorizontalHeaderItem(0, self.column_1)
        self.OutCome_table_widget.setHorizontalHeaderItem(2, self.column_2)
        self.OutCome_table_widget.setHorizontalHeaderItem(1, self.column_3)
        self.totalIncomeValue = 0
        sql = "SELECT COUNT(descrip) FROM outCome"
        control.execute(sql)
        h = control.fetchone()

        sql = "SELECT * FROM outCome"
        control.execute(sql)
        f = control.fetchall()
        for x in range(h[0]):
            row_number = self.OutCome_table_widget.rowCount()
            self.OutCome_table_widget.insertRow(row_number) 
            # Insert row
            for i in range(3):
                self.OutCome_table_widget.setItem(row_number, i, QTableWidgetItem(str(f[x][i])))
                if i == 2: 
                    self.OutCome_table_widget.setItem(row_number, i, QTableWidgetItem(str(f[x][2]) + "      " + str(f[x][3])))

        # Add name 
        self.ui.load_pages.OutCome_layout_2.addWidget(self.OutCome_table_widget)
        self.OutCome_table_widget.setEditTriggers(QTableWidget.NoEditTriggers)

        #self.OutCome_table_widget.sortItems(1, Qt.DescendingOrder)zz--AA
        #self.OutCome_table_widget.sortItems(1, Qt.AscendingOrder)AA--ZZ

    #ARCHIVE
    #//////////////////##############################################
        #STATIC BTN
        self.staticBtn = PyPushButton(
            text=self.language["main_app"]["statics"],
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["bg_three"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.staticBtn.setMaximumHeight(33)
        self.staticBtn.setMaximumWidth(120)
        self.ui.load_pages.stat_emplo_layout.addWidget(self.staticBtn)
        #EMPLOYEE 
        self.emploeBtn = PyPushButton(
            text=self.language["main_app"]["emploe"],
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["bg_three"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.emploeBtn.setMaximumHeight(33)
        self.emploeBtn.setMaximumWidth(120)
        self.ui.load_pages.stat_emplo_layout.addWidget(self.emploeBtn)     
        #EMPLOYEE
        self.outCome_frame_0 = PyFrame()
        #line edit
        self.line_edit_emploe_pas = PyLineEdit(
            text = "",
            place_holder_text = self.language["main_app"]["emploe_pass"],
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        #line edit
        self.line_edit_emploe = PyLineEdit(
            text = "",
            place_holder_text = self.language["main_app"]["emploe_name"],
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        #frame as a space
        self.outCome_frame = PyFrame()
        #button
        self.Add_emmloe = PyPushButton(
            text=self.language["main_app"]["outcome_btn"],
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["bg_one"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
            )

        self.archive_frame_2 = PyFrame()

        self.emploe_type = PyCombo(
            color=self.themes["app_color"]["text_foreground"],
            bg_color = self.themes["app_color"]["bg_two"],
            radius = 8,
            combo_theme=["employee","admin"],
        ) 
        #set size
        self.archive_frame_2.setMinimumHeight(33)
        self.archive_frame_2.setMaximumWidth(400)
        self.line_edit_emploe.setMaximumWidth(400)
        self.line_edit_emploe_pas.setMaximumWidth(120)
        self.line_edit_emploe_pas.setMinimumHeight(33)
        self.line_edit_emploe_pas.setValidator(money_val)
        self.Add_emmloe.setMinimumHeight(33)
        self.line_edit_emploe.setMinimumHeight(33)
        self.outCome_frame.setMinimumHeight(33)
        self.outCome_frame.setMaximumWidth(200)
        self.Add_emmloe.setMaximumWidth(90)
        self.archive_frame_2.setMinimumHeight(33)
        self.archive_frame_2.setMaximumWidth(400)
        #add to layout
        if self.settings["language"] == "english":
            self.ui.load_pages.add_emplo_layut.addWidget(self.outCome_frame_0)
            self.ui.load_pages.add_emplo_layut.addWidget(self.line_edit_emploe)
            self.ui.load_pages.add_emplo_layut.addWidget(self.line_edit_emploe_pas)
            self.ui.load_pages.add_emplo_layut.addWidget(self.emploe_type)
            self.ui.load_pages.add_emplo_layut.addWidget(self.outCome_frame)
            self.ui.load_pages.add_emplo_layut.addWidget(self.Add_emmloe)
            self.ui.load_pages.add_emplo_layut.addWidget(self.archive_frame_2)
        else:
            self.ui.load_pages.add_emplo_layut.addWidget(self.archive_frame_2)
            self.ui.load_pages.add_emplo_layut.addWidget(self.Add_emmloe)
            self.ui.load_pages.add_emplo_layut.addWidget(self.outCome_frame)
            self.ui.load_pages.add_emplo_layut.addWidget(self.emploe_type)
            self.ui.load_pages.add_emplo_layut.addWidget(self.line_edit_emploe_pas)
            self.ui.load_pages.add_emplo_layut.addWidget(self.line_edit_emploe)
            self.ui.load_pages.add_emplo_layut.addWidget(self.outCome_frame_0)
        # OUTCOME TABLE
        self.emploe_table_widget = PyTableWidget(
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["context_color"],
            bg_color = self.themes["app_color"]["bg_two"],
            header_horizontal_color = self.themes["app_color"]["dark_two"],
            header_vertical_color = self.themes["app_color"]["bg_three"],
            bottom_line_color = self.themes["app_color"]["bg_three"],
            grid_line_color = self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"]
        )
        
        self.emploe_table_widget.setColumnCount(3)
        self.emploe_table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.emploe_table_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.emploe_table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.emploe_table_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.emploe_table_widget.setMinimumHeight(300)
        self.emploe_table_widget.setMaximumHeight(55500)
        # Columns / Header
        self.column_1 = QTableWidgetItem()
        self.column_1.setTextAlignment(Qt.AlignCenter)
        self.column_1.setText(self.language["main_app"]["emploe_name"])

        self.column_2 = QTableWidgetItem()
        self.column_2.setTextAlignment(Qt.AlignCenter)
        self.column_2.setText(self.language["main_app"]["emploe_pass"])

        self.column_3 = QTableWidgetItem()
        self.column_3.setTextAlignment(Qt.AlignCenter)
        self.column_3.setText(self.language["main_app"]["emploe_type"])

        # Set column
        self.emploe_table_widget.setHorizontalHeaderItem(0, self.column_1)
        self.emploe_table_widget.setHorizontalHeaderItem(1, self.column_2)
        self.emploe_table_widget.setHorizontalHeaderItem(2, self.column_3)

        sql = "SELECT COUNT(emp_name) FROM employee"
        control.execute(sql)
        h = control.fetchone()
        sql = "SELECT * FROM employee"
        control.execute(sql)
        f = control.fetchall()
        for x in range(h[0]):
            row_number = self.emploe_table_widget.rowCount()
            self.emploe_table_widget.insertRow(row_number) 
            # Insert row
            for i in range(3):
                self.emploe_table_widget.setItem(row_number, i, QTableWidgetItem(str(f[x][i])))
        # Add name 
        self.ui.load_pages.emplo_layout.addWidget(self.emploe_table_widget)
        self.emploe_table_widget.setEditTriggers(QTableWidget.NoEditTriggers)

        #STATIC
        self.ui.load_pages.scroll_area_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # ADD CHART
        self.chartBar = PyChartBar(
            color=self.themes["app_color"]["text_foreground"],
        )
        self.ui.load_pages.statics_layut.addWidget(self.chartBar)
        self.chartLine = PyLineChart(
            color = self.themes["app_color"]["text_foreground"],
            bg_color = self.themes["app_color"]["bg_two"],
            line_color = self.themes["app_color"]["context_color"],
        )
        self.ui.load_pages.statics_layut.addWidget(self.chartLine)
        self.chartBar.setMinimumHeight(250)
        self.chartLine.setMinimumHeight(300)

        ############################################
        # TABLE WIDGETS COMBINED_detiled
        self.payFrameEmploee = PyFrame()
        self.payFrameEmploee.setMaximumHeight(40)
        self.emploetlsLay = QGridLayout(self.payFrameEmploee)
        self.emploetlsLay.setSpacing(6)
        self.emploetlsLay.setObjectName(u"emploetlsLay")
        self.emploetlsLay.setContentsMargins(0, 5, 0, 5)

        self.deleteEmploee = PyPushButton(
            text=self.language["main_app"]["delete"],
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["bg_one"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
            )
        self.deleteEmploee.setMinimumHeight(30)
        self.deleteEmploee.setMaximumWidth(250)
        self.emploetlsLay.addWidget(self.deleteEmploee)


        self.ui.load_pages.emplo_layout.addWidget(self.payFrameEmploee)
    # ADD GRIPS
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(
                self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(
                self, "bottom_right", self.hide_grips)

        # LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        # SET SIGNALS
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)

        # TITLE BAR / ADD EXTRA BUTTONS
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # SET SIGNALS
        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        # ADD Title
        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("SuperNova")

        # LEFT COLUMN SET SIGNALS
        # ///////////////////////////////////////////////////////////////
        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

        # SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS
        # ///////////////////////////////////////////////////////////////
        MainFunctions.set_page(self, self.ui.load_pages.page_1)
        MainFunctions.set_left_column_menu(
            self,
            menu=self.ui.left_column.menus.menu_1,
            title="Settings Left Column",
            icon_path=Functions.set_svg_icon("icon_settings.svg")
        )
        MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)

        # ///////////////////////////////////////////////////////////////
        # EXAMPLE CUSTOM WIDGETS
        #
        # OBJECTS FOR LOAD PAGES, LEFT AND RIGHT COLUMNS
        # You can access objects inside Qt Designer projects using
        # the objects below:
        #
        # <OBJECTS>
        # LEFT COLUMN: self.ui.left_column.menus
        # RIGHT COLUMN: self.ui.right_column
        # LOAD PAGES: self.ui.load_pages
        # </OBJECTS>
        # ///////////////////////////////////////////////////////////////

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # ///////////////////////////////////////////////////////////////
        # END - EXAMPLE CUSTOM WIDGETS
        # ///////////////////////////////////////////////////////////////
    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized
    # ///////////////////////////////////////////////////////////////

    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(
                self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(
                5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(
                self.width() - 20, self.height() - 20, 15, 15)
