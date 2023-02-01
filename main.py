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

        self.result = QPushButton("=", self)
        self.result.clicked.connect(self.answer)
        self.result.setGeometry(165, 400, 165, 100)
        self.result.setStyleSheet("""
            background-color: crimson;
            border: 1px solid black;
        """)

        # numbers
        self.one = QPushButton("1", self)
        self.one.clicked.connect(self.action1)
        self.one.setGeometry(0, 100, 110, 100)
        self.numbers(self.one)

        self.two = QPushButton("2", self)
        self.two.clicked.connect(self.action2)
        self.two.setGeometry(110, 100, 110, 100)
        self.numbers(self.two)

        self.three = QPushButton("3", self)
        self.three.clicked.connect(self.action3)
        self.three.setGeometry(220, 100, 110, 100)
        self.numbers(self.three)

        self.four = QPushButton("4", self)
        self.four.clicked.connect(self.action4)
        self.four.setGeometry(0, 200, 110, 100)
        self.numbers(self.four)

        self.five = QPushButton("5", self)
        self.five.clicked.connect(self.action5)
        self.five.setGeometry(110, 200, 110, 100)
        self.numbers(self.five)

        self.six = QPushButton("6", self)
        self.six.clicked.connect(self.action6)
        self.six.setGeometry(220, 200, 110, 100)
        self.numbers(self.six)

        self.seven = QPushButton("7", self)
        self.seven.clicked.connect(self.action7)
        self.seven.setGeometry(0, 300, 110, 100)
        self.numbers(self.seven)

        self.eight = QPushButton("8", self)
        self.eight.clicked.connect(self.action8)
        self.eight.setGeometry(110, 300, 110, 100)
        self.numbers(self.eight)

        self.nine = QPushButton("9", self)
        self.nine.clicked.connect(self.action9)
        self.nine.setGeometry(220, 300, 110, 100)
        self.numbers(self.nine)

        self.zero = QPushButton("0", self)
        self.zero.clicked.connect(self.action0)
        self.zero.setGeometry(0, 400, 165, 100)
        self.numbers(self.zero)

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

    @staticmethod
    def numbers(number):
        number.setStyleSheet("""
            background-color: orange;
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

    def answer(self):
        pass

    def action1(self):
        pass

    def action2(self):
        pass

    def action3(self):
        pass

    def action4(self):
        pass

    def action5(self):
        pass

    def action6(self):
        pass

    def action7(self):
        pass

    def action8(self):
        pass

    def action9(self):
        pass

    def action0(self):
        pass


app = QApplication(sys.argv)
application = Application()
application.show()
sys.exit(app.exec_())
