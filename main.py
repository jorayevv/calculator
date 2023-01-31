import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Application(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMaximumSize(400, 500)
        self.setMinimumSize(400, 500)
        self.setWindowTitle("Calculator")
        self.setFont(QFont("Calibri", 20))


app = QApplication(sys.argv)
application = Application()
application.show()
sys.exit(app.exec_())
