

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

#STYLE
# ///////////////////////////////////////////////////////////////
style = '''
QComboBox {{
    border: none;
    color: {_color};
    border-radius: {_radius};   
    background-color: {_bg_color};
}}
'''


# PY PUSH BUTTON
# ///////////////////////////////////////////////////////////////
class PyCombo(QComboBox):
    def __init__(
        self, 
        radius,
        color,
        bg_color,
        combo_theme=[],
        
    ):
        super().__init__()
        # SET PARAMETRES
        
        for i in range(len(combo_theme)):
            self.addItem(combo_theme[i])
        self.setMaximumHeight(33)
        self.setCursor(Qt.PointingHandCursor)
        self.setMaximumWidth(200)
        # SET STYLESHEET
        custom_style = style.format(
            _color = color,
            _radius = radius,
            _bg_color = bg_color,
        )
        self.setStyleSheet(custom_style)

        