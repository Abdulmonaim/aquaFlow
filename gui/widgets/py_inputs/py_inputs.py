
# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# IMPORT THEME LANGUAGE
# ///////////////////////////////////////////////////////////////
from gui.core.json_language import Language
# IMPORT BUTTON AND DIV
# ///////////////////////////////////////////////////////////////
# IMPORT FUNCTIONS
# ///////////////////////////////////////////////////////////////
from gui.core.functions import *

# ///////////////////////////////////////////////////////////////
from gui.widgets import *


style = '''
QChart {{
    border: none;
    color: {_color};
    background-color: {_bg_color};
}}
QLineSeries {{
    border: none;
    color: {_color};
    background-color: {_bg_color};
}}
'''

# PY PUSH BUTTON
# ///////////////////////////////////////////////////////////////
class PyInputs(QWidget):
    def __init__(
        self, 
        color= "#343b48",
        bg_color = "#343b48",
        line_color = "#cd1234"
    ):
        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # LOAD THEME Language
        # ///////////////////////////////////////////////////////////////
        language = Language()
        self.language = language.items
        super().__init__()
        self.chart = QFrame()
        
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0,0,0,0)
        # Create chart view with the chart
        self.line_edit_widget = PyLineEdit(
            text = "",
            place_holder_text = self.language["main_app"]["sale_search_item"],
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.line_edit_widget.setMinimumHeight(33)
        self.line_edit_widget.setMaximumWidth(300)
        
        self.main_layout.addWidget(self.line_edit_widget)

        self.setLayout(self.main_layout)


        

        # SET STYLESHEET
        self.set_stylesheet(
            color,
            bg_color,
        )
    # SET STYLESHEET
    def set_stylesheet(
        self,
        color,
        bg_color,
    ):
        # APPLY STYLESHEET
        style_format = style.format(    
            _color = color,
            _bg_color = bg_color,
        )
        self.setStyleSheet(style_format)


    
