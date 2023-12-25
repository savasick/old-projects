#!/usr/bin/python

import sys
from functools import partial
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QGridLayout, QLineEdit,
    QMainWindow, QPushButton,QVBoxLayout,
    QWidget,
)

WINDOW_WIDTH = 420
WINDOW_HEIGHT = 315
DISPLAY_HEIGHT = 100
BUTTON_SIZE = 50
ERROR_MSG = "ERR0R⚠️"

class CalculatedWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("calculated 🧮")

        self.setFixedSize(WINDOW_HEIGHT, WINDOW_WIDTH)

        self.generalLayout = QVBoxLayout()

        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setStyleSheet(" background: black;")
        self.setCentralWidget(centralWidget)

        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        self.display = QLineEdit()
        font = self.display.font()
        font.setPointSize(25)
        self.display.setFont(font)
        self.display.setStyleSheet("color: rgb(219,156,35);background: grey;")
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        self.buttonMap = {}
        self.keyMethods = {}
        buttonsLayout = QGridLayout()
        keyBoard = [
            ["7", "8", "9"],
            ["4", "5", "6"],
            ["1", "2", "3"],
            ["0", '.'],
        ]
        keyMethods = [
            ["/"],
            ["*", "("],
            ["-", ")"],
            ["+"],
        ]

        for row, keys in enumerate(keyBoard):
            for col, key in enumerate(keys):
                self.buttonMap[key] = QPushButton(key)
                self.buttonMap[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                self.buttonMap[key].setStyleSheet("color: rgb(219,156,35)")
                buttonsLayout.addWidget(self.buttonMap[key], row, col)
        
        for row, keys in enumerate(keyMethods):
            for col, key in enumerate(keys):
                self.buttonMap[key] = QPushButton(key)
                self.buttonMap[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                self.buttonMap[key].setStyleSheet("color: yellow")
                buttonsLayout.addWidget(self.buttonMap[key], row, col+3)

        self.buttonC = QPushButton("C", self)
        self.buttonC.setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
        self.buttonC.setStyleSheet("color: red")
        buttonsLayout.addWidget(self.buttonC, 0, 4)

        self.buttonDEL = QPushButton("DEL", self)
        self.buttonDEL.setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
        self.buttonDEL.setStyleSheet("color: red")
        buttonsLayout.addWidget(self.buttonDEL, 3, 2)

        self.buttonRES = QPushButton("=", self)
        self.buttonRES.setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
        self.buttonRES.setStyleSheet("color: red")
        buttonsLayout.addWidget(self.buttonRES, 3, 4)

        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        return self.display.text()

    def clearDisplay(self):
        self.setDisplayText("")
    
    def clearLast(self):
        text = self.display.text()
        self.display.setText(text[:len(text)-1])

def evaluateExpression(expression):
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG
    return result

class Calaculated:
    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connectSignalsAndSlots()

    def _calculateResult(self):
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, subExpression):
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()
        expression = self._view.displayText() + subExpression
        self._view.setDisplayText(expression)

    def _connectSignalsAndSlots(self):
        for keySymbol, button in self._view.buttonMap.items():
            if keySymbol not in {"=", "C"}:
                button.clicked.connect(
                    partial(self._buildExpression, keySymbol)
                )
        self._view.buttonRES.clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttonC.clicked.connect(self._view.clearDisplay)
        self._view.buttonDEL.clicked.connect(self._view.clearLast)

def main():
    calculatedApp = QApplication([])
    calculatedWindow = CalculatedWindow()
    calculatedWindow.show()
    Calaculated(model=evaluateExpression, view=calculatedWindow)
    sys.exit(calculatedApp.exec())

if __name__ == "__main__":
    main()