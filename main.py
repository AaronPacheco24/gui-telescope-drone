# file imports
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
import qdarktheme  # pip install pyqtdarktheme
from widget import Widget

# standard imports
import sys


# Apply dark theme.
app = QApplication(sys.argv)
app.setStyleSheet(qdarktheme.load_stylesheet())

widget = Widget()

widget.show()

app.exec()
