import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QApplication, QLineEdit)
from PyQt5.QtCore import pyqtSignal, Qt

class QwertyKeyboard(QWidget):
    keyPressed = pyqtSignal(str)  # Signal for key press

    def __init__(self):
        super().__init__()
        self.shiftActive = False
        self.initUI()

    def initUI(self):
        mainLayout = QVBoxLayout(self)
        self.setMaximumWidth(500)
        # Keyboard layout
        self.rows = [
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='],
            ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '\'', '⏎'],
            ['⇧', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', '⌫'],
            ['Space']
        ]

        self.keyWidgets = []  # Keep track of key widgets for updating

        for row in self.rows:
            rowLayout = QHBoxLayout()
            for key in row:
                button = QPushButton(key)
                button.setStyleSheet("""
                    QPushButton {
                        color: white;
                        font-size: 16px;
                        font-weight: 600;
                        background-color: #222222;
                        width: 30px;
                        height: 40px;
                    }
                    QPushButton:pressed {
                        background-color: #333333;
                    }
                    QPushButton:focus {
                        outline: none;
                    }
                """)
                button.setFocusPolicy(Qt.NoFocus)
                button.clicked.connect(lambda checked, key=key: self.onKeyPressed(key))
                rowLayout.addWidget(button)
                self.keyWidgets.append(button)
            mainLayout.addLayout(rowLayout)

    def updateKeys(self):
        # Update key labels based on the shiftActive state
        for button in self.keyWidgets:
            key = button.text()
            if self.shiftActive:
                button.setText(key.upper())
            else:
                if key != '⇧' and key != '⏎' and key != 'Space':
                    button.setText(key.lower())

    def onKeyPressed(self, key):
        if key == '⇧':
            self.shiftActive = not self.shiftActive  # Toggle shift state
            self.updateKeys()  # Update keys to reflect shift state
        elif key == 'Space':
            self.keyPressed.emit(' ')
        elif key == '⏎':
            self.keyPressed.emit('\n')
        else:
            self.keyPressed.emit(key.upper() if self.shiftActive else key)
            if self.shiftActive:
                # If a key is pressed after shift, turn off shift (like a real keyboard)
                self.shiftActive = False
                self.updateKeys()