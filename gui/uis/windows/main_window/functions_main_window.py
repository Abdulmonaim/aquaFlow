   

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import sys

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from . ui_main import *

# FUNCTIONS
class MainFunctions():
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    # SET MAIN WINDOW PAGES
    # ///////////////////////////////////////////////////////////////
    def set_page(self, page):
        self.ui.load_pages.pages.setCurrentWidget(page)

    # SET LEFT COLUMN PAGES
    # ///////////////////////////////////////////////////////////////
    def set_left_column_menu(
        self,
        menu,
        title,
        icon_path
    ):
        self.ui.left_column.menus.menus.setCurrentWidget(menu)
        self.ui.left_column.title_label.setText(title)
        self.ui.left_column.icon.set_icon(icon_path)

    # RETURN IF LEFT COLUMN IS VISIBLE
    # ///////////////////////////////////////////////////////////////
    def left_column_is_visible(self):
        width = self.ui.left_column_frame.width()
        if width == 0:
            return False
        else:
            return True

    # RETURN IF RIGHT COLUMN IS VISIBLE
    # ///////////////////////////////////////////////////////////////
    def right_column_is_visible(self):
        width = self.ui.right_column_frame.width()
        if width == 0:
            return False
        else:
            return True

    # RETURN IF RIGHT COLUMN IS VISIBLE
    # ///////////////////////////////////////////////////////////////
    def search_area_is_visible(self):
        height = self.ui.search_area_frame.height()
        #print(f'heagut is {height}')
        if height == 0:
            return False
        else:
            return True

    # SET RIGHT COLUMN PAGES
    # ///////////////////////////////////////////////////////////////
    def set_right_column_menu(self, menu):
        self.ui.right_column.menus.setCurrentWidget(menu)

    # GET TITLE BUTTON BY OBJECT NAME
    # ///////////////////////////////////////////////////////////////
    def get_title_bar_btn(self, object_name):
        return self.ui.title_bar_frame.findChild(QPushButton, object_name)

    # GET TITLE BUTTON BY OBJECT NAME
    # ///////////////////////////////////////////////////////////////
    def get_left_menu_btn(self, object_name):
        return self.ui.left_menu.findChild(QPushButton, object_name)
    
    
    # GET Addcat BUTTON BY OBJECT NAME
    # ///////////////////////////////////////////////////////////////
    def get_add_cat_btn(self, object_name):
        return self.ui.frame_2.findChild(QPushButton, object_name)
    

    # LEFT AND RIGHT COLUMNS / SHOW / HIDE
    # ///////////////////////////////////////////////////////////////
    def toggle_left_column(self):
        # GET ACTUAL CLUMNS SIZE
        width = self.ui.left_column_frame.width()
        right_column_width = self.ui.right_column_frame.width()

        MainFunctions.start_box_animation(self, width, right_column_width, "left")

    def toggle_right_column(self):
        # GET ACTUAL CLUMNS SIZE
        left_column_width = self.ui.left_column_frame.width()
        width = self.ui.right_column_frame.width()

        MainFunctions.start_box_animation(self, left_column_width, width, "right")


    def toggle_search_area(self):
        # GET ACTUAL CLUMNS SIZE
        height = self.ui.search_area_frame.height() 

        MainFunctions.start_box_animation_search(self, height, "down")
    
    def start_box_animation_search(self,area_height,direction):
        height = 0
        time_animation = self.ui.settings["time_animation"]
        minimum_search = self.ui.settings["search_area_size"]["minimum"]
        maximum_search = self.ui.settings["search_area_size"]["maximum"]

        # Check Right values        
        if area_height == minimum_search and direction == "down":
            height = maximum_search
            self.ui.title_bar_frame.setMaximumHeight(80)# from 40 to 90  
            self.ui.line_edit_search.setMaximumHeight(35)
            self.ui.search_area_frame.setMinimumHeight(40)
        else:
            height = minimum_search  
            self.ui.title_bar_frame.setMaximumHeight(40)# from 40 to 90  
            self.ui.line_edit_search.setMaximumHeight(0)
            self.ui.search_area_frame.setMinimumHeight(0)
  

    # LOAD SETTINGS
    # ///////////////////////////////////////////////////////////////
    settings = Settings()
    settings = settings.items

    # ///////////////////////////////////////////////////////////////
    if settings["language"] == "english":

        def start_box_animation(self, left_box_width, right_box_width, direction):
            right_width = 0
            left_width = 0
            time_animation = self.ui.settings["time_animation"]
            minimum_left = self.ui.settings["left_column_size"]["minimum"]
            maximum_left = self.ui.settings["left_column_size"]["maximum"]
            minimum_right = self.ui.settings["right_column_size"]["minimum"]
            maximum_right = self.ui.settings["right_column_size"]["maximum"]

            # Check Left Values        
            if left_box_width == minimum_left and direction == "left":
                left_width = maximum_left
            else:
                left_width = minimum_left

            # Check Right values        
            if right_box_width == minimum_right and direction == "right":
                right_width = maximum_right
            else:
                right_width = minimum_right       

            # ANIMATION LEFT BOX        
            self.left_box = QPropertyAnimation(self.ui.left_column_frame, b"minimumWidth")
            self.left_box.setDuration(time_animation)
            self.left_box.setStartValue(left_box_width)
            self.left_box.setEndValue(left_width)
            self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

            # ANIMATION RIGHT BOX        
            self.right_box = QPropertyAnimation(self.ui.right_column_frame, b"minimumWidth")
            self.right_box.setDuration(time_animation)
            self.right_box.setStartValue(right_box_width)
            self.right_box.setEndValue(right_width)
            self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

            # GROUP ANIMATION
            self.group = QParallelAnimationGroup()
            self.group.stop()
            self.group.addAnimation(self.left_box)
            self.group.addAnimation(self.right_box)
            self.group.start()
    else:

        def start_box_animation(self, left_box_width, right_box_width, direction):
            right_width = 0
            left_width = 0
            time_animation = self.ui.settings["time_animation"]
            minimum_left = self.ui.settings["left_column_size"]["minimum"]
            maximum_left = self.ui.settings["left_column_size"]["maximum"]
            minimum_right = self.ui.settings["right_column_size"]["minimum"]
            maximum_right = self.ui.settings["right_column_size"]["maximum"]

            # Check Left Values        
            if left_box_width == minimum_left and direction == "left":
                left_width = maximum_left
            else:
                left_width = minimum_left

            # Check Right values        
            if right_box_width == minimum_right and direction == "right":
                right_width = maximum_right
            else:
                right_width = minimum_right       

            # ANIMATION LEFT BOX        
            self.left_box = QPropertyAnimation(self.ui.left_column_frame, b"minimumWidth")
            self.left_box.setDuration(time_animation)
            self.left_box.setStartValue(left_box_width)
            self.left_box.setEndValue(left_width)
            self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

            # ANIMATION RIGHT BOX        
            self.right_box = QPropertyAnimation(self.ui.right_column_frame, b"minimumWidth")
            self.right_box.setDuration(time_animation)
            self.right_box.setStartValue(right_box_width)
            self.right_box.setEndValue(right_width)
            self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

            # GROUP ANIMATION
            self.group = QParallelAnimationGroup()
            self.group.stop()
            self.group.addAnimation(self.left_box)
            self.group.addAnimation(self.right_box)
            self.group.start()
        