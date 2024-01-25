

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

#STYLE
# ///////////////////////////////////////////////////////////////
style = '''
QLabel {{
    border: none;
    color: {_color};
}}
'''


# PY PUSH BUTTON
# ///////////////////////////////////////////////////////////////
class PyLabel(QLabel):
    def __init__(
        self, 
        text,
        color,
        
    ):
        super().__init__()
        # SET PARAMETRES
        self.setText(text)
        self.setMaximumHeight(25)
        # SET STYLESHEET
        custom_style = style.format(
            _color = color,
        )
        self.setStyleSheet(custom_style)

        