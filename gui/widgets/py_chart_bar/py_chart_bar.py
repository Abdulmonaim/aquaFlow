

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *
from PySide6.QtCharts import QChart, QChartView, QLineSeries

# STYLE
# ///////////////////////////////////////////////////////////////
style = '''
PyChartBar {{
	border: none;
    padding-left: 10px;
    padding-right: 5px;
    color: {_color};
	border-radius: {_radius};	
	background-color: {_bg_color};
}}
'''

# PY PUSH BUTTON
# ///////////////////////////////////////////////////////////////
class PyChartBar(QWidget):
    def __init__(
        self, 
        color,
    ):
        super().__init__()
        self.chart = QChart()
        self.series = QBarSeries()
        self.main_layout = QGridLayout()
        self.main_layout.setContentsMargins(0,0,0,0)
        # Create chart view with the chart
        self.chart_view = QChartView(self.chart, self)
        self.chart_view.setContentsMargins(0,0,0,0)
        self.chart_view.setStyleSheet("background-color: transparent;\n")
        # Create layout for grid and detached legend
        self.main_layout.addWidget(self.chart_view, 0, 1, 3, 1)
        self.setLayout(self.main_layout)
        self.create_series()

    def create_series(self):
        self.add_barset()
        self.add_barset()
        self.add_barset()
        self.add_barset()

        self.chart.addSeries(self.series)
        #self.chart.setTitle("Legend detach example")
        self.chart.createDefaultAxes()
        self.setStyleSheet("background-color: transparent;\n")

        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)
        #self.chart_view.setRenderHint(QPainter.Antialiasing)

    def add_barset(self):
        series_count = self.series.count()
        bar_set = QBarSet(f"set {series_count}")
        delta = series_count * 0.1
        bar_set.append([1 + delta, 2 + delta, 3 + delta, 4 + delta])
        self.series.append(bar_set)
        
        #SET STYLESHEET
        #custom_style = style.format(
        #   _color = color,
        #  )
        #self.setStyleSheet(custom_style)