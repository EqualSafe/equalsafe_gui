import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout,
                             QLabel, QGridLayout, QWidget)
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'TEST 1'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color: black;")

        # Central Widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Main layout
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setAlignment(Qt.AlignTop)

        # Screen Placeholder
        self.screen_placeholder = QLabel()
        self.screen_placeholder.setFixedSize(QSize(280, 160))
        self.screen_placeholder.setStyleSheet("background-color: gray; border-radius: 10px;")
        self.layout.addWidget(self.screen_placeholder, alignment=Qt.AlignCenter)

        # Grid Layout for buttons
        self.grid_layout = QGridLayout()
        self.layout.addLayout(self.grid_layout)
        self.grid_layout.setSpacing(10)

        # Buttons
        self.add_button('Camera', self.trigger_camera, 0, 0)
        self.add_button('Lock', self.trigger_lock, 0, 1)
        self.add_button('Bluetooth', self.trigger_bluetooth, 1, 0)
        self.add_button('Wifi', self.trigger_wifi, 1, 1)

        # Settings Button
        self.settings_button = self.add_button('Settings', self.open_settings, 2, 0, colspan=2)
        self.settings_button.setFixedSize(QSize(280, 50))
        self.layout.addWidget(self.settings_button, alignment=Qt.AlignCenter)

        self.show()

    def add_button(self, text, function, row, col, colspan=1):
        button = QPushButton(text)
        button.clicked.connect(function)
        button.setFixedSize(QSize(130, 50))
        button.setStyleSheet(
            "QPushButton {background-color: gray; color: white; border-radius: 10px;}"
            "QPushButton:pressed {background-color: #555555;}"
        )
        self.grid_layout.addWidget(button, row, col, 1, colspan)
        return button

    def trigger_camera(self):
        print("Camera function triggered")

    def trigger_lock(self):
        print("Lock function triggered")

    def trigger_bluetooth(self):
        print("Bluetooth function triggered")

    def trigger_wifi(self):
        print("WiFi function triggered")

    def open_settings(self):
        print("Settings opened")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
