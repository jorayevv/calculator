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

        # input
        self.input = QLineEdit(self)
        self.input.setGeometry(0, 0, 400, 50)
        self.input.setStyleSheet("""
            background-color: lightgrey;
            border: none;
        """)

        # on/off button
        self.main_button = QPushButton("ON", self)
        self.main_button.clicked.connect(self.on_off)
        self.main_button.setGeometry(0, 50, 165, 50)
        self.main_button.setStyleSheet("""
            background-color: green;
            border: 1px solid black;
        """)

        # clear button
        self.clear_button = QPushButton("C", self)
        self.clear_button.clicked.connect(self.clear)
        self.clear_button.setGeometry(165, 50, 165, 50)
        self.clear_button.setStyleSheet("""
            background-color: cyan;
            border: 1px solid black;
        """)

        # symbols
        self.add_button = QPushButton("+", self)
        self.add_button.clicked.connect(self.add)
        self.add_button.setGeometry(330, 50, 70, 150)
        self.symbols(self.add_button)

        self.subtract_button = QPushButton("-", self)
        self.subtract_button.clicked.connect(self.subtract)
        self.subtract_button.setGeometry(330, 200, 70, 100)
        self.symbols(self.subtract_button)

        self.multiply_button = QPushButton("*", self)
        self.multiply_button.clicked.connect(self.multiply)
        self.multiply_button.setGeometry(330, 300, 70, 100)
        self.symbols(self.multiply_button)

        self.division_button = QPushButton(":", self)
        self.division_button.clicked.connect(self.division)
        self.division_button.setGeometry(330, 400, 70, 100)
        self.symbols(self.division_button)

    # Methods
    def on_off(self):
        if self.main_button.text() == "ON":
            self.main_button.setText("OFF")
            self.input.setText("")
            self.input.setReadOnly(True)
        else:
            self.main_button.setText("ON")
            self.input.setReadOnly(False)

    def clear(self):
        self.input.setText("")

    @staticmethod
    def symbols(symbol):
        symbol.setStyleSheet("""
            background-color: violet;
            border: 1px solid black;
        """)

    def add(self):
        pass

    def subtract(self):
        pass

    def multiply(self):
        pass

    def division(self):
        pass


app = QApplication(sys.argv)
application = Application()
application.show()
sys.exit(app.exec_())
