# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from gui.uis.windows.main_window.functions_main_window import *
import sys
import os
import sqlite3
from datetime import datetime
from googleapiclient.http import MediaFileUpload
from Google import Create_Service

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT PY ONE DARK WINDOWS
# ///////////////////////////////////////////////////////////////
# MAIN WINDOW
from gui.uis.windows.main_window import *

# MAIN WINDOW
from gui.uis.windows.login import *
# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# ADJUST QT FONT DPI FOR HIGHT SCALE AN 4K MO NITOR
# ///////////////////////////////////////////////////////////////
os.environ["QT_FONT_DPI"] = "96"
# IF IS 4K MONITOR ENABLE 'os.environ["QT_SCALE_FACTOR"] = "2"'

#############################DATABASE##########################################
db = sqlite3.connect('plumbing.db')
control = db.cursor()
###############################################################################

############################UPLOAD DATABASE####################################
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
if current_time == "08:00:00":
    CLIENT_SECRET_FILE = 'client_secret.json'
    API_NAME = 'drive'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/drive']

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    folder_id = '1ewefEhStDY3YnCKwA4K7_kS-YlCaajme'
    file_name = 'plumbing.db'
    mime_type = 'application/vnd.sqlite3' # application/x-sqlite3

    file_metadata = {
        'name': file_name,
        'parents': [folder_id]
    }

    media = MediaFileUpload('./plumbing.db'.format(file_name), mimetype = mime_type)
    
    service.files().create(
        body = file_metadata,
        media_body = media,
        fields = 'id'
    ).execute()
###############################################################################

# MAIN WINDOW
# ///////////////////////////////////////////////////////////////

# GLOBALS
# ///////////////////////////////////////////////////////////////  
counter = 0
userType = 'admin'
seller = ""

# LOGIN
# ///////////////////////////////////////////////////////////////


class LoginWindow(QMainWindow):

    def __init__(
        self, 
        text = "",
        place_holder_text = "",
        radius = 8,
        border_size = 2,
        color = "#FFF",
        selection_color = "#FFF",
        bg_color = "#333",
        bg_color_active = "#222",
        context_color = "#00ABE8"
        ):
        QMainWindow.__init__(self)
        # GET WIDGETS FROM "ui_login.py"
        # Load widgets inside LoginWindow
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items


        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # ADD DROP SHADOW
        # ///////////////////////////////////////////////////////////////
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.ui.bg.setGraphicsEffect(self.shadow)

        # QTIMER
        # ///////////////////////////////////////////////////////////////
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(30)

        # KEY PRESS EVENT
        # ///////////////////////////////////////////////////////////////
        self.ui.username.keyReleaseEvent = self.gotopass
        self.ui.password.keyReleaseEvent = self.check_login

        self.show()
    def gotopass(self, event):
        username = self.ui.username.text()
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            sql = "SELECT count(emp_name) FROM employee"
            control.execute(sql)
            h = control.fetchone()
            sql = "SELECT * FROM employee"
            control.execute(sql)
            f = control.fetchall()
            for i in range(h[0]):
                if username == f[i][0]:
                    self.ui.password.setFocus()
                    self.ui.user_description.setText(f"welcone {username}")
                    self.ui.username.setStyleSheet("#username:focus { border: 3px solid #bdff00; }")
                    return
                else:
                    self.ui.username.setStyleSheet("#username:focus { border: 3px solid rgb(255, 0, 127); }")
                    self.shacke_window()
                    self.ui.user_description.setText("username doesn't exist")
    # CHECK LOGIN
    # ///////////////////////////////////////////////////////////////
    def check_login(self, event):

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        global userType
        global seller
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            username = self.ui.username.text()
            password = self.ui.password.text()
            sql = "SELECT count(emp_name) FROM employee"
            control.execute(sql)
            h = control.fetchone()
            sql = "SELECT * FROM employee"
            control.execute(sql)
            f = control.fetchall()
            def open_main():
                # SHOW MAIN WINDOW
                self.main = MainWindow()
                #self.main.label_user.setText(username.capitalize())
                self.main.show()                
                self.close()
            flag = 0
            for i in range(h[0]):
                if username != f[i][0] or password != f[i][1]:
                    flag = 1
                elif username == f[i][0] and password == f[i][1]:
                    flag = 2
                    userType = f[i][2]
                    seller = f[i][0]
                    break
                    
            if flag == 1:
                self.ui.username.setStyleSheet("#username:focus { border: 3px solid rgb(255, 0, 127); }")
                self.ui.password.setStyleSheet("#password:focus { border: 3px solid rgb(255, 0, 127); }")
                self.shacke_window()
            elif flag == 2: 
                self.ui.user_description.setText(f"Welcome {username}!")
                self.ui.user_description.setStyleSheet("#user_description { color: #bdff00 }")
                self.ui.username.setStyleSheet("#username:focus { border: 3px solid #bdff00; }")
                self.ui.password.setStyleSheet("#password:focus { border: 3px solid #bdff00; }")
                QTimer.singleShot(1200, lambda: open_main())
            

    def shacke_window(self):
        # SHACKE WINDOW
        actual_pos = self.pos()
        QTimer.singleShot(0, lambda: self.move(actual_pos.x() + 1, actual_pos.y()))
        QTimer.singleShot(50, lambda: self.move(actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(100, lambda: self.move(actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(150, lambda: self.move(actual_pos.x() + -5, actual_pos.y()))
        QTimer.singleShot(200, lambda: self.move(actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(250, lambda: self.move(actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(300, lambda: self.move(actual_pos.x(), actual_pos.y()))

    # UPDATE PROGRESS BAR
    # ///////////////////////////////////////////////////////////////
    def update(self):
        global counter

        # CLOSE SPLASH SCREEN AND OPEN MAIN APP
        if counter >= 2:
            # STOP TIMER
            self.timer.stop()
            self.animation_login()

        # INCREASE COUNTER
        counter += 1

    # START ANIMATION TO LOGIN
    # ///////////////////////////////////////////////////////////////
    def animation_login(self):
        # ANIMATION
        self.animation = QPropertyAnimation(self.ui.frame_widgets, b"geometry")
        self.animation.setDuration(1500)
        self.animation.setStartValue(QRect(0, 70, self.ui.frame_widgets.width(), self.ui.frame_widgets.height()))
        self.animation.setEndValue(QRect(0, -325, self.ui.frame_widgets.width(), self.ui.frame_widgets.height()))
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

# MAIN WINDOW
class MainWindow(QMainWindow):
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
        self.settings = settings.items

        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.hide_grips = True  # Show/Hide resize gr ips
        SetupMainWindow.setup_gui(self)

        self.ui.line_edit_search.returnPressed.connect(self.findItem)

        # SETTINGS
        # ///////////////////////////////////////////////////////////////
        self.upload.clicked.connect(self.uploadFun)
        #/////////////////LANGUAGE
        self.arabic.clicked.connect(self.set_arabic)
        self.english.clicked.connect(self.set_english)
        #/////////////////Theme
        self.bright.clicked.connect(self.set_bright)
        self.customized.clicked.connect(self.set_customized)
        #////////////// CONFIRM
        self.ConfirmSettings.clicked.connect(self.ConfirmSettingsFun)

        # HOME PAGE
        # ///////////////////////////////////////////////////////////////
        #Clear Daily Table
        self.total_income_button.clicked.connect(self.clear_daily)
        
        #UPDATE CRITICAL ITEMS
        self.updateCriticalItems.clicked.connect(self.updateCriticalItemsfUN)

        #SALES AREA
        self.salesOrCombined.stateChanged.connect(self.soc)
        self.selsOrCombo.stateChanged.connect(self.ssoc)

        self.newOrExist.stateChanged.connect(self.noex)
        #self.AddNewRow.clicked.connect(self.salesNewRow)
        
        self.inputs.line_edit_widget.returnPressed.connect(self.choseItem)
        self.inputs_payments.line_edit_widget.returnPressed.connect(self.addPayments)
        self.deletNewRow.clicked.connect(self.salesDeleteRow)
        self.deletNewRowPayment.clicked.connect(self.payDeleteRow)

        self.inputs_cust.line_edit_widget.returnPressed.connect(self.findcust)
        #Quantity cell press to show total
        #current_total_row = self.salesOpTable.currentRow()
        #self.salesOpTable.cellPressed.connect(self.updateTotal)
        
        self.checkOut.clicked.connect(self.checkOutFun)
        self.Confirm.clicked.connect(self.ConfirmSale)

        #/////////////////////////////// Add subCategry
        self.categery_combo.currentIndexChanged.connect(self.update_categery_combo)
        self.subCatCombo.currentIndexChanged.connect(self.update_item_table)
        self.cat.clicked.connect(self.addCat)
        self.subCatbtn.clicked.connect(self.addSubCat)
        self.AddIteam.clicked.connect(self.addItemFun)
        self.table_widget.horizontalHeader().sectionClicked.connect(self.itemtablesort)

        self.updateItem.clicked.connect(self.updateItemFun)
        self.DeleteItem.clicked.connect(self.deleteItemFun)
        self.selectItem.clicked.connect(self.selectItemFun)

        #/////////////////////////////// sales
        self.salesbtn.clicked.connect(self.show_sales)
        self.showdtlsSales.clicked.connect(self.showSalesDetails)
        self.combinedbtn.clicked.connect(self.show_combined)
        self.showCombinedDetails.clicked.connect(self.showCombinedDetailsFun)
        self.ConfirmUpdatecart.clicked.connect(self.updateCombinedCart)

        self.inputs_com.line_edit_widget.returnPressed.connect(self.findcom)
        self.readyCombined.clicked.connect(self.ReadyForComFun)
        self.add_pay_com.clicked.connect(self.addPayCom)

        self.inputs_cust.line_edit_widget.returnPressed.connect(self.findcust)
        self.showdtls_cust.clicked.connect(self.showPayDetails)
        self.ReadyForPay.clicked.connect(self.ReadyForPayFun)
        self.add_pay_cust.clicked.connect(self.addPaySale)


        #//////////////////////////////// OUTCOME
        self.Add_Outcome.clicked.connect(self.addOutCome)
        self.OutCome_table_widget.horizontalHeader().sectionClicked.connect(self.OutCome_table_widget_sort)
        self.table_widget.horizontalHeader().sectionClicked.connect(self.itemtablesort)


        #//////////////////////////////// ARCHIVE
        self.staticBtn.clicked.connect(self.setStatics)
        self.emploeBtn.clicked.connect(self.setEmploe)

        self.Add_emmloe.clicked.connect(self.addEmploee)
        self.deleteEmploee.clicked.connect(self.deleteEmploeeFun)
        # SHOW MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.show()

        #set completer
        # make the value of the completer is the value of the search
     
        sql = "SELECT item FROM item"
        control.execute(sql)
        item = control.fetchall()
        items = []
        for i in item:
            items.append(i[0])
        complete = items
        completer = QCompleter(complete)
        #self.ui.line_edit_search.setCompleter(completer)
        self.inputs.line_edit_widget.setCompleter(completer)
        #self.ui.line_edit_search.returnPressed.connect(self.homesearch)
    
        #currentw = self.salesOpTable
        #currentw.setCompleter(completer)
        
    # LEFT MENU BTN IS CLICKED
    # Run function when btn is clicked
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////


    def btn_clicked(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # left menu
        # OPEN PAGE 1
        if btn.objectName() == "btn_home":
            self.ui.credits.message_label.setText("")
            # select menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # load Page
            MainFunctions.set_page(self, self.ui.load_pages.page_1)

            #set completer
            # make the value of the completer is the value of the search
            sql = "SELECT item FROM item"
            control.execute(sql)
            item = control.fetchall()
            items = []
            for i in item:
                items.append(i[0])
            complete = items
            completer = QCompleter(complete)
            self.ui.line_edit_search.setCompleter(completer)
            self.ui.line_edit_search.returnPressed.connect(self.homesearch)

        # OPEN PAGE 2
        if btn.objectName() == "btn_page_2":
            self.ui.credits.message_label.setText("")
            # select menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # load Page
            MainFunctions.set_page(self, self.ui.load_pages.page_2)
            #update tables items
            sql = "SELECT item FROM item"
            control.execute(sql)
            item = control.fetchall()
            items = []
            for i in item:
                items.append(i[0])
            complete = items
            completer = QCompleter(complete)
            self.ui.line_edit_search.setCompleter(completer)
            self.showItem()
        # OPEN Page 3
        if btn.objectName() == "btn_page_3":
            self.ui.credits.message_label.setText("")
            # select menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # load Page
            MainFunctions.set_page(self, self.ui.load_pages.page_3)
            #update sales and combined tables
            self.showSales()
            self.showCombined()
        if userType =='admin':
            # OPEN Page 4
            if btn.objectName() == "btn_page_4":
                self.ui.credits.message_label.setText("")
                # select menu
                self.ui.left_menu.select_only_one(btn.objectName())

                # load Page
                MainFunctions.set_page(self, self.ui.load_pages.page_4)
                # update customers table
                self.showCustomers()
            # OPEN Page 5
            if btn.objectName() == "btn_page_5":
                self.ui.credits.message_label.setText("")
                # select menu
                self.ui.left_menu.select_only_one(btn.objectName())

                # load Page
                MainFunctions.set_page(self, self.ui.load_pages.page_5)
                # update outcome table 
                self.show_outCome()
            # OPEN Page 6
            if btn.objectName() == "btn_page_6":
                self.ui.credits.message_label.setText("")
                # select menu
                self.ui.left_menu.select_only_one(btn.objectName())

                # load Page
                MainFunctions.set_page(self, self.ui.load_pages.page_6)
            # TITLE BAR MENU
            # ///////////////////////////////////////////////////////////////
        # SETTINGS TITLE BAR // RIGHT clomun
        if btn.objectName() == "btn_top_settings":
            # Toogle Active
            if not MainFunctions.right_column_is_visible(self):
                btn.set_active(True)

                # Show / Hide
                MainFunctions.toggle_right_column(self)
            else:
                btn.set_active(False)

                # Show / Hide
                MainFunctions.toggle_right_column(self)
            
        # DAILY // LEFT clumn
        if btn.objectName() == "btn_info" or btn.objectName() == "btn_close_left_column":
            # CHECK IF LEFT COLUMN IS VISIBLE
            if not MainFunctions.left_column_is_visible(self):
                # Show / Hide
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                self.ui.left_menu.deselect_all_tab()
                # Show / Hide
                MainFunctions.toggle_left_column(self)
                if btn.objectName() == "btn_close_left_column":
                    self.ui.left_menu.deselect_all_tab()
                    # Show / Hide
                    MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())

            # Change Left Column Menu
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self, 
                    menu = self.ui.left_column.menus.menu_1,
                    title = "Settings Left Column",
                    icon_path = Functions.set_svg_icon("icon_settings.svg")
                )
            # CHECK IF LEFT COLUMN IS VISIBLE
            if not MainFunctions.left_column_is_visible(self):
                # Show / Hide
                MainFunctions.toggle_left_column(self)
            else:
                if btn.objectName() == "btn_close_left_column":
                    self.ui.left_menu.deselect_all_tab()
                    # Show / Hide
                    MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            self.daily()
        #SEARCH BTN
        if btn.objectName() == "btn_search":
            # Toogle Active
            if not MainFunctions.search_area_is_visible(self):
                btn.set_active(True)

                # Show / Hide
                MainFunctions.toggle_search_area(self)
            else:
                btn.set_active(False)

                # Show / Hide
                MainFunctions.toggle_search_area(self)


        # DEBUG
        #print(f"Button {btn.objectName()}, clicked!")


        #/////////////////////////////////////////////////////////////
        # Categuraies

    # Run function when btn is released
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # DEBUG
        #print(f"Button {btn.objectName()}, released!")

    # RESIZE EVENT
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
  

    # SETTINGS
    # ///////////////////////////////////////////////////////////////
    def uploadFun(self):
        CLIENT_SECRET_FILE = 'client_secret.json'
        API_NAME = 'drive'
        API_VERSION = 'v3'
        SCOPES = ['https://www.googleapis.com/auth/drive']

        service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

        folder_id = '1ewefEhStDY3YnCKwA4K7_kS-YlCaajme'
        file_name = 'plumbing.db'
        mime_type = 'application/vnd.sqlite3' # application/x-sqlite3

        file_metadata = {
            'name': file_name,
            'parents': [folder_id]
        }

        media = MediaFileUpload('./plumbing.db'.format(file_name), mimetype = mime_type)
        
        service.files().create(
            body = file_metadata,
            media_body = media,
            fields = 'id'
        ).execute()

    #LANGUAGE
    def set_arabic(self):
        self.arabic.setCheckable(True)
        self.english.setCheckable(False)
        seting = Settings()
        self.setings = seting.items
        self.setings["language"] = "arabic"
        seting.serialize()
        #print(self.arabic.styleSheet())
        #self.arabic.setStyleSheet(self.arabic.styleSheet()[0][0]+"background-color: #fff;\n")
        #print(self.arabic.styleSheet())
    def set_english(self):
        self.english.setCheckable(True)
        self.arabic.setCheckable(False)
        seting = Settings()
        self.setings = seting.items
        self.setings["language"] = "english"
        seting.serialize()
    #THEME
    def set_bright(self):
        self.bright.setCheckable(True)
        self.customized.setCheckable(False)
        seting = Settings()
        self.setings = seting.items
        self.setings["theme_name"] = "bright_theme"
        seting.serialize()
        #print(self.setings["theme_name"])
    def set_customized(self):
        self.bright.setCheckable(False)
        self.customized.setCheckable(True)
        seting = Settings()
        self.setings = seting.items
        self.setings["theme_name"] = "dracula"
        seting.serialize()
        #print(self.setings["theme_name"])
    #Confirmation
    def ConfirmSettingsFun(self):
        python = sys.executable
        #print(*sys.argv)
        os.execl(python, python, * sys.argv)
    #HOME PAGE
    #////////////////////////////////////////////////////////////////
    #HOME SEARCH
    def homesearch(self):
        crntRow = self.salesOpTable.currentRow()
        text = self.ui.line_edit_search.text()
        sql = "SELECT priceOut FROM item WHERE item = (?)"
        val = (text,)
        control.execute(sql, val)
        x = control.fetchone()
        self.salesOpTable.setItem(crntRow, 0 ,QTableWidgetItem(text))
        self.salesOpTable.setItem(crntRow, 1 ,QTableWidgetItem(str(x)))
    #UPDATE CRIICAL ITEMS
    def updateCriticalItemsfUN(self):
        self.critical_iteams.clear()
        sql = "SELECT COUNT(item) FROM item"
        control.execute(sql)
        h = control.fetchone()

        sql = "SELECT quantity, critQuan, item FROM item"
        control.execute(sql)
        f = control.fetchall()
        for i in range(h[0]):
            if f[i][1] >= f[i][0]:
                item = QListWidgetItem(str(f[i][2]))
                self.critical_iteams.addItem(item)
    #show daily #///////////////////////////////////////////// just make sure it's today
    def daily(self):
        self.table_widget_dialy.clearContents()
        while self.table_widget_dialy.rowCount() > 0:
            self.table_widget_dialy.removeRow(self.table_widget_dialy.rowCount() - 1)

        self.totalIncomeValue = 0
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        dt_string = now.strftime("%d/%m/%Y")
        #print(f'{dt_string} and the type {type(dt_string)}')
        
        #outcome
        sql = "SELECT COUNT(descrip) FROM outCome WHERE draw_date = (?)"
        val = (dt_string,)
        control.execute(sql,val)
        h = control.fetchone()
        sql = "SELECT descrip, moneyTaken, draw_date FROM outCome WHERE draw_date = (?)"
        val = (dt_string,)
        control.execute(sql,val)
        f = control.fetchall()

        #sales
        sql = "SELECT COUNT(op_id) FROM sales WHERE op_date = (?)"
        val = (dt_string,)
        control.execute(sql,val)
        hs = control.fetchone()

        sql = "SELECT op_id, money_paid, op_time FROM sales WHERE op_date = (?)"
        val = (dt_string,)
        control.execute(sql,val)
        fs = control.fetchall()

        #sales payment
        sql = "SELECT COUNT(spay_id) FROM sPayment WHERE spay_date = (?)"
        val = (dt_string,)
        control.execute(sql,val)
        hp = control.fetchone()

        sql = "SELECT spay_id, money_pay, spay_time FROM sPayment WHERE spay_date = (?)"
        val = (dt_string,)
        control.execute(sql,val)
        fp = control.fetchall()
        #outcome
        for x in range(h[0]):
            row_number = self.table_widget_dialy.rowCount()
            self.table_widget_dialy.insertRow(row_number) 
            # Insert row
            for i in range(3):
                self.table_widget_dialy.setItem(row_number, i, QTableWidgetItem(str(f[x][i])))
                if i == 1:
                    self.totalIncomeValue = (self.totalIncomeValue + int(f[x][1])) * -1 
                    self.table_widget_dialy.setItem(row_number, i, QTableWidgetItem(str("-" + str(f[x][1]))))
        #sales
        for x in range(hs[0]):
            row_number = self.table_widget_dialy.rowCount()
            self.table_widget_dialy.insertRow(row_number) 
            # Insert row
            for i in range(3):
                self.table_widget_dialy.setItem(row_number, i, QTableWidgetItem(str(fs[x][i])))
                #if i == 2: 
                    #self.table_widget_dialy.setItem(row_number, i, QTableWidgetItem(str(f[x][2]) + "      " + str(f[x][3])))
                if i == 1:
                    self.totalIncomeValue = (self.totalIncomeValue + int(fs[x][1]))
                    self.table_widget_dialy.setItem(row_number, i, QTableWidgetItem(str(fs[x][1])))
        #sales payment
        for x in range(hp[0]):
            row_number = self.table_widget_dialy.rowCount()
            self.table_widget_dialy.insertRow(row_number) 
            # Insert row
            for i in range(3):
                self.table_widget_dialy.setItem(row_number, i, QTableWidgetItem(str(fp[x][i])))
                #if i == 2: 
                    #self.table_widget_dialy.setItem(row_number, i, QTableWidgetItem(str(f[x][2]) + "      " + str(f[x][3])))
                if i == 1:
                    self.totalIncomeValue = (self.totalIncomeValue + int(fp[x][1]))
                    self.table_widget_dialy.setItem(row_number, i, QTableWidgetItem(str(fp[x][1])))
        self.total_income.setText(str(self.totalIncomeValue))
    #Clear DAILY
    def clear_daily(self):
        self.total_income.setText("0")
        self.table_widget_dialy.clearContents()
        while self.table_widget_dialy.rowCount() > 0:
            self.table_widget_dialy.removeRow(self.table_widget_dialy.rowCount() - 1)
    #SalesOrCombined 
    def soc(self,value):
        if value:
            self.HomeSaleName.setPlaceholderText(self.language["main_app"]["sale_name_com"])
            #self.ui.load_pages.Homesales1.addWidget(self.newOrExist,0,alignment=Qt.AlignRight)
            self.ui.load_pages.Homesales2.addWidget(self.payFrame,0,1)

            self.ui.load_pages.Homesales1.removeWidget(self.selsOrCombo)
            self.selsOrCombo.setParent(None)
            self.selsOrCombo.setChecked(False)


        else:
            self.HomeSaleName.setPlaceholderText(self.language["main_app"]["sale_name_ord"])
            self.ui.load_pages.Homesales2.removeWidget(self.payFrame)
            self.payFrame.setParent(None)


            self.ui.load_pages.Homesales1.addWidget(self.selsOrCombo)
            self.ui.load_pages.Homesales1.addWidget(self.HomeSaleName)

            #self.ui.load_pages.Homesales1.removeWidget(self.newOrExist)
            #self.newOrExist.setParent(None)
            #self.newOrExist.setChecked(False)
    def ssoc(self):
        if self.selsOrCombo.isChecked():
            self.HomeSaleName.setPlaceholderText(self.language["main_app"]["sale_name_com"])
            sql = "SELECT cust_name FROM combined"
            control.execute(sql)
            item = control.fetchall()
            items = []
            for i in item:
                items.append(i[0])
            complete = items
            completer = QCompleter(complete)
            self.HomeSaleName.setCompleter(completer)
        else:
            self.HomeSaleName.setPlaceholderText(self.language["main_app"]["sale_name_ord"])
            complete = []
            completer = QCompleter(complete)
            self.HomeSaleName.setCompleter(completer)
    #new combined or exist
    def noex(self,value):
        if self.newOrExist.isChecked():
             print("hh")

        else:
            print("WW")
    #ADD NEW ROW with item
    def salesNewRow(self):
        text = self.inputs.line_edit_widget.text()
        if text != "" and text != " ":
            sql = "SELECT priceOut FROM item WHERE item = (?)"
            val = (text,)
            control.execute(sql, val)
            h = control.fetchone()
            if h != None: 
                row_number = self.salesOpTable.rowCount()
                self.salesOpTable.insertRow(row_number) # Insert row
                self.salesOpTable.setItem(row_number, 2, QTableWidgetItem(str(1)))
                self.salesOpTable.setItem(row_number, 1, QTableWidgetItem(str(h[0])))
                self.salesOpTable.setItem(row_number, 0, QTableWidgetItem(str(text))) 
            else:
                self.ui.credits.message_label.setText("please chose an item")
            self.inputs.line_edit_widget.clear()

    #ADD DELETE ROW FOR SALES
    def salesDeleteRow(self):
        if self.salesOpTable.rowCount() > 0:

            self.HomeSaleName.setText("")
            self.HomeSalePaid.setText("")
            self.inputs.line_edit_widget.setText("")
            selected = self.salesOpTable.currentRow()
            if selected >= 0:
                self.salesOpTable.removeRow(selected)
            else:
                self.salesOpTable.removeRow(self.salesOpTable.rowCount()-1)
    #ADD DELETE ROW FOR PAYMENTS
    def payDeleteRow(self):
        if self.salesOpTablePayments.rowCount() > 0:
            selected = self.salesOpTablePayments.currentRow()
            if selected >= 0:
                self.salesOpTablePayments.removeRow(selected)
            else:
                self.salesOpTablePayments.removeRow(self.salesOpTablePayments.rowCount()-1)
    #COUNT TOTAL
    def updateTotal(self):
        current_total_row = self.salesOpTable.currentRow()
    #SEARCH IN ITEMS
    def choseItem(self):
        self.salesNewRow()   
        self.inputs.line_edit_widget.clear()  
    #ADD PAYMENTS
    def addPayments(self):
        text = self.inputs_payments.line_edit_widget.text()
        date = self.date_payment.date()
        date = str(date.day()) + '/' + str(date.month()) + '/' + str(date.year())
        if text != "" and text != " ":
            row_number = self.salesOpTablePayments.rowCount()
            self.salesOpTablePayments.insertRow(row_number) # Insert row
            self.salesOpTablePayments.setItem(row_number, 0, QTableWidgetItem(str(text))) 
            self.salesOpTablePayments.setItem(row_number, 1, QTableWidgetItem(str(date))) 
            self.inputs_payments.line_edit_widget.clear()
        self.inputs_payments.line_edit_widget.clear()  
    #READ DATA FOR THE CART
    def read_dataU(self):
        rowCount = self.salesOpTable.rowCount()
        colCount = self.salesOpTable.columnCount()
        saleName = self.HomeSaleName.text()
        cart = []
        
        if self.salesOrCombined.isChecked():
            for row in range(rowCount):
                rowe = []
                sql = "SELECT max(op_id) FROM comCart"
                control.execute(sql)
                op_id = control.fetchone()
                if op_id[0] == None:
                    rowe.append(1)
                else:
                    rowe.append(op_id[0] + 1)
                
                for col in range(colCount):
                    item = self.salesOpTable.item(row, col)
                    if item != None:
                        rowe.append(item.text())
                        
                    try:
                        (int(rowe[3]))
                    except:
                        self.ui.credits.message_label.setText("plese check the Quantity")
                        self.salesOpTable.selectRow(row)

                    try:
                        (int(rowe[2]))
                    except:
                        self.ui.credits.message_label.setText("plese check the price")
                        self.salesOpTable.selectRow(row)

                    """
                    sql = "SELECT quantity FROM item WHERE item = (?)"
                    val = (rowe[1],)
                    control.execute(sql, val)
                    h = control.fetchone()
                    #////////////////////////////////////catch the error if the quatity is a word
                    # also if the quantit >> the exist quatity
                    try:
                        remainingQuatity = h[0] - int(rowe[3])
                        if remainingQuatity >= 0:
                            sql = "UPDATE item SET quantity = (?) WHERE item = (?)"
                            val = (remainingQuatity, rowe[1])
                            control.execute(sql, val)
                            db.commit()
                        else:
                            print("there's o enaough Quantity of the item in the store")
                        self.salesOpTable.selectRow(row)
                    except:
                        pass
                    """
                rowa = tuple(rowe)
                cart.append(rowa)

                #THE PAYMENTS  here we will read the data from self.salesOpTablePayments table 
        else:
            if self.selsOrCombo.isChecked():    
                for row in range(rowCount):
                    rowe = []
                    sql = "SELECT op_id FROM combined WHERE cust_name = (?)"
                    val = (saleName,)
                    control.execute(sql, val)
                    op_id = control.fetchone()
                    if op_id == None:
                        self.ui.credits.message_label.setText("please enter a name in combine or check the box")
                        return
                    else:
                        rowe.append(op_id[0])
                    for col in range(colCount):
                        item = self.salesOpTable.item(row, col)
                        if item != None:
                            rowe.append(item.text())
                    try:
                        (int(rowe[3]))
                    except:
                        self.ui.credits.message_label.setText("plese check the Quantity")
                        self.salesOpTable.selectRow(row)
                    try:
                        (int(rowe[2]))
                    except:
                        self.ui.credits.message_label.setText("plese check the price")
                        self.salesOpTable.selectRow(row)
                    
                    sql = "SELECT quantity FROM item WHERE item = (?)"
                    val = (rowe[1],)
                    control.execute(sql, val)
                    h = control.fetchone()
                    #////////////////////////////////////catch the error if the quatity is a word
                    # also if the quantit >> the exist quatity
                   
                    try:
                        remainingQuatity = h[0] - int(rowe[3])
                        if remainingQuatity >= 0:
                            pass
                        else:
                            self.ui.credits.message_label.setText("there's no enaough Quantity of the item in the store")
                            self.salesOpTable.selectRow(row)
                    except:
                        pass
                    
                    rowa = tuple(rowe)
                    cart.append(rowa)
            else:
                for row in range(rowCount):
                    rowe = []
                    sql = "SELECT max(op_id) FROM sCart"
                    control.execute(sql)
                    op_id = control.fetchone()
                    if op_id[0] == None:
                        rowe.append(1)
                    else:
                        rowe.append(op_id[0] + 1)
                        
                    for col in range(colCount):
                        item = self.salesOpTable.item(row, col)
                        if item != None:
                            rowe.append(item.text())
                        
                    try:
                        (int(rowe[3]))
                    except:
                        self.ui.credits.message_label.setText("plese check the Quantity")
                        self.salesOpTable.selectRow(row)

                    try:
                        (int(rowe[2]))
                    except:
                        self.ui.credits.message_label.setText("plese check the price")

                        self.salesOpTable.selectRow(row)
                    

                    sql = "SELECT quantity FROM item WHERE item = (?)"
                    val = (rowe[1],)
                    control.execute(sql, val)
                    h = control.fetchone()
                    #////////////////////////////////////catch the error if the quatity is a word
                    # also if the quantit >> the exist quatity
                    try:
                        remainingQuatity = h[0] - int(rowe[3])
                        if remainingQuatity >= 0:
                           pass
                        else:
                            self.ui.credits.message_label.setText("there's no enaough Quantity of the item in the store")
                            self.salesOpTable.selectRow(row)
                            return
                    except:
                        pass
                    

                    rowa = tuple(rowe)
                    cart.append(rowa)
        return cart
    #READ DATA FOR THE PAYMENTS
    def read_datap(self):
        rowCount = self.salesOpTablePayments.rowCount()
        colCount = self.salesOpTablePayments.columnCount()
        payment = []
        
        for row in range(rowCount):
            rowp = []
            sql = "SELECT max(op_id) FROM payPlan"
            control.execute(sql)
            op_id = control.fetchone()
            if op_id[0] == None:
                rowp.append(1)
            else:
                rowp.append(op_id[0] + 1)
                
            for col in range(colCount):
                item = self.salesOpTablePayments.item(row, col)
                rowp.append(item.text())
            rowq = tuple(rowp)
            payment.append(rowq)
        return payment
    def clearPaymentTable(self):
        while self.salesOpTablePayments.rowCount() > 0:
            self.salesOpTablePayments.removeRow(self.salesOpTablePayments.rowCount() - 1)

    #CONFIRM SALE
    def clearsaleArea(self):
        while self.salesOpTable.rowCount() > 0:
            self.salesOpTable.removeRow(self.salesOpTable.rowCount() - 1)
        while self.salesOpTable.rowCount() < 0:
            self.salesOpTable.insertRow(self.salesOpTable.rowCount())   
        # set the next items to default
        self.HomeSaleName.setText("") 
        self.HomeSalePaid.setText("")
        self.HomeSaleLeft.setText("")
        self.inputs.line_edit_widget.setText("")
        self.salesOpTable.clearContents() 
        self.total_Op_price.setText("0")
        complete = []
        completer = QCompleter(complete)
        self.HomeSaleName.setCompleter(completer)
        self.ui.credits.message_label.setText("")
        self.clearPaymentTable()
    def checkOutFun(self):    
        rowCount = self.salesOpTable.rowCount() 
        colCount = self.salesOpTable.columnCount()
        saleName = self.HomeSaleName.text()
        salePaid = self.HomeSalePaid.text()
        saleLeft = 0
        cartTotal = 0
        #self.ui.credits.message_label.setText("www")
        if (salePaid):
            if rowCount != 0:
                for row in range(rowCount):
                    for col in range(colCount):
                        if col == 1:
                            try:
                                itemp = self.salesOpTable.item(row, col).text()
                                itemq = self.salesOpTable.item(row, col+1).text()
                                (float(itemp))
                                (float(itemq))
                            except:
                                self.ui.credits.message_label.setText("watch the quantity and the price")
                                return
                            itemp = self.salesOpTable.item(row, col).text()
                            itemq = self.salesOpTable.item(row, col+1).text()    
                            cartTotal += float(itemp) * float(itemq) 

                self.total_Op_price.setText(str(cartTotal))
                saleLeft = float(cartTotal) - float(salePaid)
                self.HomeSaleLeft.setText(str(saleLeft))
            else:
                self.inputs.line_edit_widget.setFocus()
                self.ui.credits.message_label.setText("please add items")
        else:
            self.ui.credits.message_label.setText("please insert the money")
            self.HomeSalePaid.setFocus()
    def ConfirmSale(self):
        cart = self.read_dataU() # the function of read data
        #self.total_Op_price.setText(str(float(x[0]) * float(idgetItem)))
        saleName = self.HomeSaleName.text()
        salePaid = self.HomeSalePaid.text()
        saleLeft = None
        cartTotal = 0
        try:
            for i in cart:
                cartTotal += int(i[2]) * int(i[3])
            saleLeft = cartTotal - int(salePaid) 
        except:
            self.ui.credits.message_label.setText("please check the cart or enter a name")
            return
        #check if there's monye paid or not 
        if cart != None:
            if len(cart) != 0:
                if (salePaid):
                    if self.salesOrCombined.isChecked():
                        if (saleName):
                            #try:
                            pay_plan = self.read_datap()
                            for i in cart:
                                sql = "SELECT item, quantity FROM item WHERE item = (?)"
                                val = (i[1],)
                                control.execute(sql, val)
                                h = control.fetchone()

                                sql = "INSERT INTO comCart VALUES (?, ?, ?, ?)"
                                control.execute(sql, i)
                                db.commit()
                                cartTotal += int(i[2]) * int(i[3])

                                QUantityleft = float(h[1]) - float(i[3])
                                sql = "UPDATE item SET quantity = (?) WHERE item = (?)"
                                val = (QUantityleft ,i[1])
                                control.execute(sql, val)

                            for i in pay_plan:
                                sql = "INSERT INTO payPlan VALUES (?, ?, ?)"
                                control.execute(sql, i)
                                db.commit()

                            now = datetime.now()
                            current_time = now.strftime("%H:%M:%S")
                            dt_string = now.strftime("%d/%m/%Y")
                            sql = "SELECT max(op_id) FROM comCart"
                            control.execute(sql)
                            op_id = control.fetchone()
                            saleLeft = cartTotal - int(salePaid)
                            sql = "INSERT INTO combined VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
                            val = (op_id[0], saleName, cartTotal, salePaid, saleLeft, dt_string, current_time, seller)
                            control.execute(sql, val)
                            db.commit()
                            self.clearPaymentTable()
                            self.table_combined.clearContents()
                            while self.table_combined.rowCount() > 0:
                                self.table_combined.removeRow(self.table_combined.rowCount() - 1)
                            self.showCombined()
                            self.clearsaleArea()
                            #except:
                                #print("something went wrong")
                        else:
                            self.HomeSaleName.setFocus()
                            self.ui.credits.message_label.setText("please insert new name")
                    else:
                        if self.selsOrCombo.isChecked():
                            if (saleName):
                                try:
                                    sql = "SELECT op_id, money_left FROM combined WHERE cust_name = (?)"
                                    val = (saleName,)
                                    control.execute(sql, val)
                                    h = control.fetchone()
                                    for i in cart:
                                        sql = "SELECT item, quantity FROM item WHERE item = (?)"
                                        val = (i[1],)
                                        control.execute(sql, val)
                                        h = control.fetchone()

                                        sql = "INSERT INTO comCart VALUES (?, ?, ?, ?)"
                                        control.execute(sql, i)
                                        db.commit()
                                        cartTotal += float(i[2]) * float(i[3])

                                        QUantityleft = float(h[1]) - float(i[3])
                                        sql = "UPDATE item SET quantity = (?) WHERE item = (?)"
                                        val = (QUantityleft ,i[1])
                                        control.execute(sql, val)

                                    Mleft = int(cartTotal) - int(salePaid)
                                    udate_money_left = h[1] + Mleft

                                    sql = "UPDATE combined SET money_left = (?) WHERE op_id = (?)"
                                    val = (udate_money_left, h[0])
                                    control.execute(sql, val)
                                    db.commit()
                                    self.clearsaleArea()
                                except:
                                    pass
                            else:
                                self.HomeSaleName.setFocus()
                                self.ui.credits.message_label.setText("please chose a name that has a combined")
                        else:
                            try:
                                if saleLeft >=0:
                                    if saleLeft == 0:
                                        for i in cart:
                                            sql = "SELECT item, quantity FROM item WHERE item = (?)"
                                            val = (i[1],)
                                            control.execute(sql, val)
                                            h = control.fetchone()

                                            sql = "INSERT INTO sCart VALUES (?, ?, ?, ?)"
                                            control.execute(sql, i)
                                            db.commit()
                                            cartTotal += int(i[2]) * int(i[3])

                                            QUantityleft = float(h[1]) - float(i[3])
                                            sql = "UPDATE item SET quantity = (?) WHERE item = (?)"
                                            val = (QUantityleft ,i[1])
                                            control.execute(sql, val)
                                            db.commit()
                                        now = datetime.now()
                                        current_time = now.strftime("%H:%M:%S")
                                        dt_string = now.strftime("%d/%m/%Y")
                                        sql = "SELECT max(op_id) FROM sCart"
                                        control.execute(sql)
                                        op_id = control.fetchone()
                                        saleLeft = cartTotal - int(salePaid)

                                        sql = "INSERT INTO sales VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
                                        val = (op_id[0], saleName, cartTotal, salePaid, saleLeft, dt_string, current_time, seller)
                                        control.execute(sql, val)
                                        db.commit()
                                        self.table_Customers.clearContents()
                                        while self.table_Customers.rowCount() > 0:
                                            self.table_Customers.removeRow(self.table_Customers.rowCount() - 1)
                                        self.showCustomers()
                                        self.clearsaleArea()
                                    if saleLeft != 0 or saleLeft != 0.0 :
                                        if (saleName):
                                            for i in cart:
                                                sql = "SELECT item, quantity FROM item WHERE item = (?)"
                                                val = (i[1],)
                                                control.execute(sql, val)
                                                h = control.fetchone()
                                                #
                                                sql = "INSERT INTO sCart VALUES (?, ?, ?, ?)"
                                                control.execute(sql, i)
                                                db.commit()
                                                cartTotal += int(i[2]) * int(i[3])
                                                QUantityleft = float(h[1]) - float(i[3])
                                                sql = "UPDATE item SET quantity = (?) WHERE item = (?)"
                                                val = (QUantityleft ,i[1])
                                                control.execute(sql, val)
                                                db.commit()

                                            now = datetime.now()
                                            current_time = now.strftime("%H:%M:%S")
                                            dt_string = now.strftime("%d/%m/%Y")
                                            sql = "SELECT max(op_id) FROM sCart"
                                            control.execute(sql)
                                            op_id = control.fetchone()
                                            saleLeft = cartTotal - int(salePaid)
                                            sql = "INSERT INTO sales VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
                                            val = (op_id[0], saleName, cartTotal, salePaid, saleLeft, dt_string, current_time, seller)
                                            control.execute(sql, val)
                                            db.commit()
                                            self.table_Customers.clearContents()
                                            while self.table_Customers.rowCount() > 0:
                                                self.table_Customers.removeRow(self.table_Customers.rowCount() - 1)
                                            self.showCustomers()
                                            self.clearsaleArea()
                                        else:
                                            self.HomeSaleName.setFocus()
                                else:
                                    self.HomeSaleLeft.setFocus()
                                    self.ui.credits.message_label.setText("plese recheck the paid and left")
                            except:
                                self.ui.credits.message_label.setText("something went wrong")
                    #TO SET THE ROWS TO 1 ROWS
                else:
                    self.HomeSalePaid.setFocus()
                    self.ui.credits.message_label.setText("please enter the amount of money paid")
            else:
                self.inputs.line_edit_widget.setFocus()
                self.ui.credits.message_label.setText("please enter items in the cart")
        else:
            self.inputs.line_edit_widget.setFocus()
            self.ui.credits.message_label.setText("cart doesn't exist")
        # SUB CATEGUARY    

    #///////////////////////////////////////////////////////////////
    # cat
    def fn(self):
        self.ui.load_pages.frame.setMaximumHeight(160)
        self.ui.load_pages.frame_3.setMaximumHeight(50)
        #self.table_widget.setMinimumHeight(200)
        self.subCatCombo.setMaximumHeight(33)
        self.subCatbtn.setMaximumHeight(33)
        self.line_edit_sub_cat.setMaximumHeight(33)
        self.spcFrame = PyFrame()
    def update_categery_combo(self,index):
        self.fn()
        crnt_cat = self.categery_combo.currentText()
        sql = "SELECT subCat FROM sub_category where cat = (?)"
        val = (crnt_cat,)
        control.execute(sql, val)
        sub_catst = control.fetchall()
        sub_cats = []
        for i in sub_catst:
            for j in i:
                sub_cats.append(j)
        self.subCatCombo.clear()
        self.subCatCombo.addItems(sub_cats)
    def update_item_table(self, index):
        self.table_widget.clearContents()
        while self.table_widget.rowCount() > 0:
            self.table_widget.removeRow(self.table_widget.rowCount() - 1)
        
        crnt_subCat = self.subCatCombo.currentText()
        sql = "SELECT COUNT(subCat) FROM item WHERE subCat = (?)"
        val = (crnt_subCat,)
        control.execute(sql, val)
        h = control.fetchone()
        sql = "SELECT item, quantity, dateIn, priceIn, priceOut, critQuan FROM item WHERE subCat = (?)"
        val = (crnt_subCat,)
        control.execute(sql, val)
        f = control.fetchall()
        for x in range(h[0]):
            row_number = self.table_widget.rowCount()
            self.table_widget.insertRow(row_number) 
            # Insert row
            for i in range(6):
                self.table_widget.setItem(row_number, i, QTableWidgetItem(str(f[x][i])))
                #self.table_widget.QTableWidgetItem().setTextAlignment(Qt.AlignRight)
    #ADD CAT
    def addCat(self):
        catName = self.line_edit_cat.text() 
        if catName != "" and catName!=" ":
            sql = "INSERT INTO category (cat) VALUES (?)"
            val = (catName,)
            control.execute(sql, val)
            db.commit()
            self.categery_combo.addItem(catName)
            self.ui.credits.message_label.setText("")
        else:
            self.ui.credits.message_label.setText("Invalid Name")
        self.line_edit_cat.setText("")
    #ADD SUB CAT
    def addSubCat(self):
        crnt_cat = self.categery_combo.currentText()
        subCatName = self.line_edit_sub_cat.text()
        if subCatName != "" and subCatName!=" ":
            sql = "INSERT INTO sub_category (subCat, cat) VALUES (?, ?)"
            val = (subCatName, crnt_cat)
            control.execute(sql, val)
            db.commit()
            self.ui.credits.message_label.setText("")
            self.subCatCombo.addItem(subCatName)
        else:
            self.ui.credits.message_label.setText("Invalid Name")
        self.line_edit_sub_cat.setText("")
    #ADD ITEMS

    def addItemFun(self):
        crnt_subCat = self.subCatCombo.currentText()
        itmName = self.Item_Name.text()
        itm_prc_in = self.price_in.text()
        itm_qnt = self.QUantity.text()
        itm_prc_out = self.Price_Out.text()
        itm_crcl_qnt = self.Critical_Quuantity.text()
        if crnt_subCat != '':
            if itmName != "" and itmName !=" ":
                if (itm_prc_in):
                    if (itm_qnt):
                        if (itm_prc_out):
                            if (itm_crcl_qnt):
                                try:
                                    now = datetime.now()
                                    #current_time = now.strftime("%H:%M:%S")
                                    dt_string = now.strftime("%d/%m/%Y")
                                    sql = "INSERT INTO item (item, dateIn, priceIn, priceOut, quantity, critQuan, subCat) VALUES (?, ?, ?, ?, ?, ?, ?)"
                                    val = (itmName, dt_string, itm_prc_in, itm_prc_out, itm_qnt, itm_crcl_qnt, crnt_subCat)
                                    control.execute(sql, val)
                                    db.commit()
                                    self.table_widget.clearContents()
                                    while self.table_widget.rowCount() > 0:
                                        self.table_widget.removeRow(self.table_widget.rowCount() - 1)
                                    
                                    crnt_subCat = self.subCatCombo.currentText()
                                    sql = "SELECT COUNT(subCat) FROM item WHERE subCat = (?)"
                                    val = (crnt_subCat,)
                                    control.execute(sql, val)
                                    h = control.fetchone()

                                    self.table_widget.clearContents()
                                    while self.table_widget.rowCount() > 0:
                                        self.table_widget.removeRow(self.table_widget.rowCount() - 1)

                                    sql = "SELECT item, quantity, dateIn, priceIn, priceOut, critQuan FROM item WHERE subCat = (?)"
                                    val = (crnt_subCat,)
                                    control.execute(sql, val)
                                    f = control.fetchall()
                                    for x in range(h[0]):
                                        row_number = self.table_widget.rowCount()
                                        self.table_widget.insertRow(row_number) 
                                        # Insert row
                                        for i in range(6):
                                            self.table_widget.setItem(row_number, i, QTableWidgetItem(str(f[x][i])))

                                    self.Item_Name.setText("")
                                    self.price_in.setText("")
                                    self.QUantity.setText("")
                                    self.Price_Out.setText("")
                                    self.Critical_Quuantity.setText("")
                                    self.ui.credits.message_label.setText("")
                                except:
                                    self.Item_Name.setFocus()
                                    self.ui.credits.message_label.setText("please insert a new Name")
                            else:
                                self.Critical_Quuantity.setFocus()
                                self.Critical_Quuantity.setText("1")
                                self.ui.credits.message_label.setText("insert the Critical_Quuantity or it will be 1")

                        else:
                            self.Price_Out.setFocus()
                            self.ui.credits.message_label.setText("insert Price_Out")

                    else:
                        self.QUantity.setFocus()
                        self.ui.credits.message_label.setText("Invalid Quantity")

                else:
                    self.price_in.setFocus()
                    self.ui.credits.message_label.setText("Invalid price_in")
            else:
                self.Item_Name.setFocus()
                self.ui.credits.message_label.setText("insert a unique name")
        else:
            self.ui.credits.message_label.setText("please select categery and subCat")
    def showItem(self):
        crnt_subCat = self.subCatCombo.currentText()
        self.table_widget.clearContents()
        while self.table_widget.rowCount() > 0:
            self.table_widget.removeRow(self.table_widget.rowCount() - 1)
        sql = "SELECT COUNT(subCat) FROM item WHERE subCat = (?)"
        val = (crnt_subCat,)
        control.execute(sql, val)
        h = control.fetchone()
        sql = "SELECT item, quantity, dateIn, priceIn, priceOut, critQuan FROM item WHERE subCat = (?)"
        val = (crnt_subCat,)
        control.execute(sql, val)
        f = control.fetchall()
        for x in range(h[0]):
            row_number = self.table_widget.rowCount()
            self.table_widget.insertRow(row_number) 
            # Insert row
            for i in range(6):
                self.table_widget.setItem(row_number, i, QTableWidgetItem(str(f[x][i])))
                #self.table_widget.QTableWidgetItem().setTextAlignment(Qt.AlignRight)
    
        self.table_widget.sortItems(0, Qt.AscendingOrder)#AA--ZZ
    def findItem(self):
        itm = self.ui.line_edit_search.text()
        btn = SetupMainWindow.setup_btns(self)
        if self.ui.load_pages.pages.currentIndex() == 1:
            sql = "SELECT item, subCat FROM item WHERE item = (?)"
            val = (itm,)
            control.execute(sql, val)
            item = control.fetchone()
            """ to set the categry
            sql = "SELECT cat FROM sub_category WHERE subCat = (?)"
            val = (item[0],)
            control.execute(sql, val)
            sub = control.fetchone()
            
            self.categery_combo.clear()
            self.categery_combo.setItem(sub[0])
            """
            self.fn()
            self.subCatCombo.clear()
            self.subCatCombo.addItems([item[1]])

    def selectItemFun(self):
        try:
            self.itemLayCntrl.addWidget(self.updateItem,0,2)
            currentRow = self.table_widget.currentRow()
            item = self.table_widget.item(currentRow, 0).text()  
            sql = "SELECT item, dateIn, priceIn, priceOut, quantity, critQuan, subCat FROM item WHERE item = (?)"
            val = (item,)
            control.execute(sql, val) 
            h = control.fetchone()
            now = datetime.now()
            #current_time = now.strftime("%H:%M:%S")
            dt_string = now.strftime("%d/%m/%Y")
            #crnt_subCat = self.subCatCombo.setCurrentText(h[6])
            itmName = self.Item_Name.setText(str(h[0]))
            itm_prc_in = self.price_in.setText(str(h[2]))
            itm_qnt = self.QUantity.setText(str(h[4]))
            itm_prc_out = self.Price_Out.setText(str(h[3]))
            itm_crcl_qnt = self.Critical_Quuantity.setText(str(h[5]))
            self.ui.credits.message_label.setText("")
        except:
            self.ui.credits.message_label.setText("please select the item")
    def updateItemFun(self):
        try:
            itmName = self.Item_Name.text()
            itm_prc_in = self.price_in.text()
            itm_qnt = self.QUantity.text()
            itm_prc_out = self.Price_Out.text()
            itm_crcl_qnt = self.Critical_Quuantity.text()
            now = datetime.now()
            #current_time = now.strftime("%H:%M:%S")
            if (itm_prc_in) and (itm_qnt) and (itm_prc_out) and (itm_crcl_qnt): 
                dt_string = now.strftime("%d/%m/%Y")
                sql = "UPDATE item SET dateIn = (?), priceIn = (?), priceOut = (?), quantity = (?), critQuan = (?) WHERE item = (?)"
                val = (now, itm_prc_in, itm_prc_out, itm_qnt, itm_crcl_qnt, itmName)
                control.execute(sql, val)
                db.commit()
                self.showItem()
                self.Item_Name.setText("")
                self.price_in.setText("")
                self.QUantity.setText("")
                self.Price_Out.setText("")
                self.Critical_Quuantity.setText("")
                self.ui.credits.message_label.setText("")

            else:
                self.ui.credits.message_label.setText("please insert data")
        except:
            self.ui.credits.message_label.setText("don't change the fucken name!! u can delete it ")
    def deleteItemFun(self):
        try:
            currentRow = self.table_widget.currentRow()
            item = self.table_widget.item(currentRow, 0).text()
            sql = "SELECT item FROM item WHERE item = (?)"
            val = (item,)
            control.execute(sql, val)
            h = control.fetchone()
            if h[0] != seller:
                sql = "DELETE FROM item WHERE item = (?)"
                val = (item,)
                control.execute(sql, val)
                db.commit()
                self.table_widget.clearContents()
                while self.table_widget.rowCount() > 0:
                    self.table_widget.removeRow(self.table_widget.rowCount() - 1)
                self.ui.credits.message_label.setText("")
                self.showItem()
        except:
            self.ui.credits.message_label.setText("please select the item")
    def itemtablesort(self,logicalIndex):
        self.table_widget.sortItems(logicalIndex, Qt.AscendingOrder)

    #SALES
    #//////////////////////////////////////////////////////////////
    def show_sales(self):
        self.salesbtn.setCheckable(True)
        self.combinedbtn.setCheckable(False)
        self.ui.load_pages.sales_widget.setCurrentWidget(self.ui.load_pages.sales)
    def showSales(self):
       
        while self.table_widget_Sales.rowCount() > 0:
            self.table_widget_Sales.removeRow(self.table_widget_Sales.rowCount() - 1)
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
    def showSalesDetails(self):
        if self.payFrameSalesTabes.findChild(QTableWidget,"table_Sales_cart"):
            self.salesLayTables.removeWidget(self.table_Sales_cart)
            self.table_Sales_cart.setParent(None)
        else:
            currentRow = self.table_widget_Sales.currentRow()
            custID = self.table_widget_Sales.item(currentRow, 0)
            self.salesLayTables.addWidget(self.table_Sales_cart,0,1)
            
            sql = "SELECT COUNT(op_id) FROM sCart"
            control.execute(sql)
            g = control.fetchone()

            sql = "SELECT op_id, item, priceOut, quantity FROM sCart"
            control.execute(sql)
            k = control.fetchall()

            self.table_Sales_cart.clearContents()
            while self.table_Sales_cart.rowCount() > 0:
                self.table_Sales_cart.removeRow(self.table_Sales_cart.rowCount() - 1)
            for x in range(g[0]):
                if custID != None:
                    if k[x][0] == int(custID.text()):
                        row_number = self.table_Sales_cart.rowCount()
                        self.table_Sales_cart.insertRow(row_number) 
                        # Insert row
                        for i in range(3):
                            self.table_Sales_cart.setItem(row_number, i, QTableWidgetItem(str(k[x][i+1])))
    def show_combined(self):
        self.salesbtn.setCheckable(False)
        self.combinedbtn.setCheckable(True)
        self.ui.load_pages.sales_widget.setCurrentWidget(self.ui.load_pages.combined)
    def showCombined(self):
       
        while self.table_combined.rowCount() > 0:
            self.table_combined.removeRow(self.table_combined.rowCount() - 1)
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
    def showCombinedDetailsFun(self):
        if self.ui.load_pages.frame_8.findChild(QFrame,"payFrameCombineddtls"):
            #check it again
            self.ui.load_pages.verticalLayout_c2.removeWidget(self.payFrameCombineddtls)
            self.payFrameCombineddtls.setParent(None)
        else:
            self.ui.load_pages.verticalLayout_c2.addWidget(self.payFrameCombineddtls)
            currentRow = self.table_combined.currentRow()
            customerName = self.table_combined.item(currentRow,1)
            custID = self.table_combined.item(currentRow, 0)
            if custID != None:
                self.customer_Name_combined.setText(str(customerName.text()))
            #cart
            sql = "SELECT COUNT(op_id) FROM comCart"
            control.execute(sql)
            g = control.fetchone()
            sql = "SELECT op_id, item, priceOut, quantity FROM comCart"
            control.execute(sql)
            k = control.fetchall()
            #payplan
            sql = "SELECT COUNT(op_id) FROM payPlan"
            control.execute(sql)
            o = control.fetchone()
            sql = "SELECT op_id, op_date, oMoney_paid FROM payPlan"
            control.execute(sql)
            p = control.fetchall()
            #fetchPayments
            sql = "SELECT COUNT(compay_id) FROM ComPayment"
            control.execute(sql)
            cj = control.fetchone()

            sql = "SELECT compay_id, money_pay, spay_date, spay_time, seller FROM ComPayment"
            control.execute(sql)
            pq = control.fetchall()
        
            #for Cart Tables
            self.table_widget_Combined.clearContents()
            while self.table_widget_Combined.rowCount() > 0:
                self.table_widget_Combined.removeRow(self.table_widget_Combined.rowCount() - 1)
            for x in range(g[0]):
                if custID != None:
                    if k[x][0] == int(custID.text()):
                        row_number = self.table_widget_Combined.rowCount()
                        self.table_widget_Combined.insertRow(row_number) 
                        # Insert row
                        for i in range(3):
                            self.table_widget_Combined.setItem(row_number, i, QTableWidgetItem(str(k[x][i+1])))

            #for the left part of the payment table "PayPlan"
            self.table_widget_Combined_payment.clearContents()
            while self.table_widget_Combined_payment.rowCount() > 0:
                self.table_widget_Combined_payment.removeRow(self.table_widget_Combined_payment.rowCount() - 1)
            for x in range(o[0]):
                if custID != None:
                    if p[x][0] == int(custID.text()):
                        row_number = self.table_widget_Combined_payment.rowCount()
                        self.table_widget_Combined_payment.insertRow(row_number) 
                        # Insert row
                        for i in range(2):
                            self.table_widget_Combined_payment.setItem(row_number, i, QTableWidgetItem(str(p[x][i+1])))
            if custID != None:
            #the count of payment
                for y in range(cj[0]):
                    if pq[y][0] == custID.text():
                        #row_number = self.table_widget_Combined_payment.rowCount()
                        #self.table_widget_Combined_payment.insertRow(row_number) 
                        # Insert row
                        for i in range(4):
                            self.table_widget_Combined_payment.setItem(row_number, i+2, QTableWidgetItem(str(pq[y][i+1])))
     
    def updateCombinedCart(self):
        rowCount = self.table_widget_Combined.rowCount()
        colCount = self.table_widget_Combined.columnCount()
        newcart = []
        
        for row in range(rowCount):
            rowp = []
            sql = "SELECT op_id FROM combined"
            control.execute(sql)
            op_id = control.fetchone()
            #rowp.append(op_id[0] + 1)     
            for col in range(colCount):
                item = self.table_widget_Combined.item(row, col)
                rowp.append(item.text())
            rowq = tuple(rowp)
            newcart.append(rowq)

        #for i in newcart:
            #sql = "UPDATE  comCart SET item = (?), priceOut = (?), quantity = (?) WHERE op_id = (?)"
            #val = (i[0], i[1], i[2], op_id)
            #control.execute(sql, val)
            #db.commit()
            #print(i[0])

        #sql = "UPDATE comCart SET item = (?), priceOut = (?), quantity = (?) WHERE op_id = (?)"
        #val = (now, itm_prc_in, itm_prc_out, itm_qnt, itm_crcl_qnt, itmName)
        #control.execute(sql, val)
        #db.commit()

        return newcart
        
    def ReadyForComFun(self):
        currentRow = self.table_combined.currentRow()
        custID = self.table_combined.item(currentRow, 0)
        if custID != None:
            custID = self.table_combined.item(currentRow, 0).text()
            sql = "SELECT money_left, cust_name FROM combined WHERE op_id = (?)"
            val = (custID,)
            control.execute(sql, val)
            h = control.fetchone()
            self.customer_Name_com.setText(str(h[0]))
            self.inputs_com.line_edit_widget.setText(str(h[1]))
    def findcom(self):
        custname = self.inputs_com.line_edit_widget.text()

        sql = "SELECT money_left FROM combined WHERE cust_name = (?)"
        val = (custname,)
        control.execute(sql, val)
        h = control.fetchone()
        if h != None:
            self.customer_Name_com.setText(str(h[0]))
        else:
            self.ui.credits.message_label.setText("not in the dara , try again pleae")
    def addPayCom(self):
        text = self.customer_Name_com.text()
        custname = self.inputs_com.line_edit_widget.text()

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        dt_string = now.strftime("%d/%m/%Y")

        sql = "SELECT money_left, op_id FROM combined WHERE cust_name = (?)"
        val = (custname,)
        control.execute(sql, val)
        h = control.fetchone()
        if text != "" and text !=" " and float(text) > 0: 
            left = h[0] - float(text)

            if left >= 0:
                custname = self.inputs_com.line_edit_widget.text()
                sql = "UPDATE combined SET money_left = (?) WHERE cust_name = (?)"
                val = (left, custname)
                control.execute(sql, val)
                #db.commit()
                
                
                sql = "INSERT INTO ComPayment VALUES (?, ?, ?, ?, ?)"
                val = (h[1], text, dt_string, current_time, seller)
                control.execute(sql, val)
                db.commit()
                    

                self.table_combined.clearContents()
                while self.table_combined.rowCount() > 0:
                    self.table_combined.removeRow(self.table_combined.rowCount() - 1)
                self.showCombined()
                self.inputs_com.line_edit_widget.setText("")
                self.customer_Name_com.setText("")
                self.ui.credits.message_label.setText("")

            else:
                self.ui.credits.message_label.setText("r u dumb ! check the left or paid or cart idk wtf u did")
        else:
            self.ui.credits.message_label.setText("Invalid input")
            text = self.customer_Name_com.setFocus()

    def ReadyForPayFun(self):
        currentRow = self.table_Customers.currentRow()
        custID = self.table_Customers.item(currentRow, 1)
        if custID != None:
            custID = self.table_Customers.item(currentRow, 1).text()
            sql = "SELECT money_left, cust_name FROM sales WHERE op_id = (?)"
            val = (custID,)
            control.execute(sql, val)
            h = control.fetchone()
            self.customer_Name_sale.setText(str(h[0]))
            self.inputs_cust.line_edit_widget.setText(str(h[1]))
    def findcust(self):
        custname = self.inputs_cust.line_edit_widget.text()

        sql = "SELECT money_left FROM sales WHERE cust_name = (?)"
        val = (custname,)
        control.execute(sql, val)
        h = control.fetchone()
        if h != None:
            self.customer_Name_sale.setText(str(h[0]))
            self.ui.credits.message_label.setText("")
        else:
            self.ui.credits.message_label.setText("not in the dara , try again pleae")
    def addPaySale(self):
        text = self.customer_Name_sale.text()
        custname = self.inputs_cust.line_edit_widget.text()

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        dt_string = now.strftime("%d/%m/%Y")

        sql = "SELECT money_left, op_id FROM sales WHERE cust_name = (?)"
        val = (custname,)
        control.execute(sql, val)
        h = control.fetchone()
        if text != "" and text !=" " and float(text) > 0: 
            left = h[0] - float(text)

            if left >= 0:
                custname = self.inputs_cust.line_edit_widget.text()
                sql = "UPDATE sales SET money_left = (?) WHERE cust_name = (?)"
                val = (left, custname)
                control.execute(sql, val)
                #db.commit()
                
                
                sql = "INSERT INTO sPayment VALUES (?, ?, ?, ?, ?)"
                val = (h[1], text, dt_string, current_time, seller)
                control.execute(sql, val)
                db.commit()
                    

                self.table_Customers.clearContents()
                while self.table_Customers.rowCount() > 0:
                    self.table_Customers.removeRow(self.table_Customers.rowCount() - 1)
                self.showCustomers()
                self.inputs_cust.line_edit_widget.setText("")
                self.customer_Name_sale.setText("")
                self.ui.credits.message_label.setText("")

            else:
                self.ui.credits.message_label.setText("check the maths !!")
        else:
            self.ui.credits.message_label.setText("Invalid input as money")
    def showCustomers(self):
        while self.table_Customers.rowCount() > 0:
            self.table_Customers.removeRow(self.table_Customers.rowCount() - 1)
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
    def showPayDetails(self):
        if self.payFrameCustTabes.findChild(QTableWidget,"table_Customers_cart"):
            self.custLayTables.removeWidget(self.table_Customers_cart)
            self.table_Customers_cart.setParent(None)
            self.custLayTables.removeWidget(self.table_Customers_payments)
            self.table_Customers_payments.setParent(None)
        else:
            currentRow = self.table_Customers.currentRow()
            custID = self.table_Customers.item(currentRow, 1)
            self.custLayTables.addWidget(self.table_Customers_cart,1,0,1,1)
            self.custLayTables.addWidget(self.table_Customers_payments,1,1,1,1)
            
            #fetchCart
            sql = "SELECT COUNT(op_id) FROM sCart"
            control.execute(sql)
            g = control.fetchone()
            sql = "SELECT op_id, item, priceOut, quantity FROM sCart"
            control.execute(sql)
            k = control.fetchall()

            #fetchPayments
            sql = "SELECT COUNT(spay_id) FROM sPayment"
            control.execute(sql)
            cj = control.fetchone()
            sql = "SELECT spay_id, money_pay, spay_date, spay_time, seller FROM sPayment"
            control.execute(sql)
            p = control.fetchall()
            #carts
            self.table_Customers_cart.clearContents()
            while self.table_Customers_cart.rowCount() > 0:
                self.table_Customers_cart.removeRow(self.table_Customers_cart.rowCount() - 1)
            for x in range(g[0]):
                if custID != None:
                    if k[x][0] == int(custID.text()):
                        row_number = self.table_Customers_cart.rowCount()
                        self.table_Customers_cart.insertRow(row_number) 
                        # Insert row
                        for i in range(3):
                            self.table_Customers_cart.setItem(row_number, i, QTableWidgetItem(str(k[x][i+1])))
            #paymenst
            self.table_Customers_payments.clearContents()
            while self.table_Customers_payments.rowCount() > 0:
                self.table_Customers_payments.removeRow(self.table_Customers_payments.rowCount() - 1)
            if custID != None:
                #the count of payment
                for y in range(cj[0]):
                    if p[y][0] == custID.text():
                        row_number = self.table_Customers_payments.rowCount()
                        self.table_Customers_payments.insertRow(row_number) 
                        # Insert row
                        for i in range(4):
                            self.table_Customers_payments.setItem(row_number, i, QTableWidgetItem(str(p[y][i+1])))
        
    #OUTCOME
    #/////////////////////////////////////////////////////////////////
    def show_outCome(self):
        self.OutCome_table_widget.clearContents()
        self.OutCome_table_widget.clearContents()
        while self.OutCome_table_widget.rowCount() > 0:
            self.OutCome_table_widget.removeRow(self.OutCome_table_widget.rowCount() - 1)
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
    def addOutCome(self):
        disc = self.line_edit_OutCome_Dics.text()
        money_out = self.line_edit_OutCome.text()
        if disc != "" and disc != " " and money_out != "" and money_out !=" ":
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            dt_string = now.strftime("%d/%m/%Y")
            sql = "INSERT INTO outCome VALUES (?, ?, ?, ?)"
            val = (disc, money_out, dt_string, current_time)
            control.execute(sql, val)
            db.commit()
            self.show_outCome()
            self.line_edit_OutCome_Dics.setText("")
            self.line_edit_OutCome.setText("")
            self.ui.credits.message_label.setText("")
        else:
            self.ui.credits.message_label.setText("please check ur inputs")
    def OutCome_table_widget_sort(self,logicalIndex):
        self.OutCome_table_widget.sortItems(logicalIndex, Qt.AscendingOrder)
    #ARCHIVE
    #/////////////////////////////////////////////////////////////////
    def setStatics(self):
        self.staticBtn.setCheckable(True)
        self.emploeBtn.setCheckable(False)
        self.ui.load_pages.Archive.setCurrentWidget(self.ui.load_pages.statics_page)
    def setEmploe(self):
        self.staticBtn.setCheckable(False)
        self.emploeBtn.setCheckable(True)
        self.ui.load_pages.Archive.setCurrentWidget(self.ui.load_pages.emloe_page)

    def show_employee_data(self):
        self.emploe_table_widget.clearContents()
        self.emploe_table_widget.clearContents()
        while self.emploe_table_widget.rowCount() > 0:
            self.emploe_table_widget.removeRow(self.emploe_table_widget.rowCount() - 1)
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
    def addEmploee(self):
        emploeName = self.line_edit_emploe.text()
        emploepass = self.line_edit_emploe_pas.text()
        emploeType = self.emploe_type.currentText()
        if emploeName !="" and emploeName !=" " and emploepass !="" and emploepass !=" ":
            sql = "INSERT INTO employee VALUES (?, ?, ?)"
            val = (emploeName, emploepass, emploeType)
            control.execute(sql, val)
            db.commit()
            self.show_employee_data()
            self.line_edit_emploe.setText("")
            self.line_edit_emploe_pas.setText("")
            self.ui.credits.message_label.setText("")
        else:
            self.ui.credits.message_label.setText("please check ur inputs")
    def showEmploee(self):
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
    def deleteEmploeeFun(self):
        currentRow = self.emploe_table_widget.currentRow()
        Emp = self.emploe_table_widget.item(currentRow, 0).text()

        sql = "SELECT emp_name FROM employee WHERE emp_name = (?)"
        val = (Emp,)
        control.execute(sql, val)
        h = control.fetchone()
        if h[0] != seller:
            sql = "DELETE FROM employee WHERE emp_name = (?)"
            val = (Emp,)
            control.execute(sql, val)
            db.commit()
            self.emploe_table_widget.clearContents()
            while self.emploe_table_widget.rowCount() > 0:
                self.emploe_table_widget.removeRow(self.emploe_table_widget.rowCount() - 1)
            self.ui.credits.message_label.setText("")
            self.showEmploee()
        else:
            self.ui.credits.message_label.setText("u can't delete the active user !!!")

#verticalLayout_customers
# SETTINGS WHEN TO START
# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////

if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = LoginWindow()
    #window = MainWindow()

    # EXEC APP
    # ///////////////////////////////////////////////////////////////

    sys.exit(app.exec())



 















