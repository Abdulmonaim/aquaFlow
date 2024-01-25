

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

#STYLE
# ///////////////////////////////////////////////////////////////
style = '''
QDateEdit {{
    border: none;
    color: {_color};
}}
'''


# PY PUSH BUTTON
# ///////////////////////////////////////////////////////////////
class PyDate(QDateEdit):
    def __init__(
        self, 
        color,
        
    ):
        super().__init__()
        # SET PARAMETRES
        self.setCalendarPopup(True)
        self.setDateTime(QDateTime.currentDateTime())
        self.setMaximumHeight(25)
        # SET STYLESHEET
        custom_style = style.format(
            _color = color,
        )
        self.setStyleSheet(custom_style)

        