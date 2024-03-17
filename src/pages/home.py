from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QFrame,
                             QGridLayout, QWidget, QStackedWidget)

from PyQt5.QtCore import QSize, Qt

from src.qt_elements.buttons import (FeatureButton, SettingButton)


class HomePage():
    def __init__(self, app):
        self.widget = QWidget()
        self.layout = QVBoxLayout(self.widget)
        self.app = app

    def setup(self):
        # # Screen Placeholder
        screen_placeholder = QLabel()
        screen_placeholder.setFixedSize(QSize(280, 160))
        screen_placeholder.setStyleSheet("background-color: gray; border-radius: 10px;")
        self.layout.addWidget(screen_placeholder, alignment=Qt.AlignCenter)

        # Grid Layout for feature buttons
        grid_layout = QGridLayout()
        self.layout.addLayout(grid_layout)

        # Feature buttons
        self.feature_buttons = {
            "Camera": FeatureButton("Camera", self.do_something, self.get_feature_status),
            "Lock": FeatureButton("Lock", self.do_something, self.get_feature_status),
            "Bluetooth": FeatureButton("Bluetooth", self.do_something, self.get_feature_status),
            "Wifi": FeatureButton("Wifi", self.do_something, self.get_feature_status)
        }

        positions = [(i, j) for i in range(2) for j in range(2)]
        for pos, (name, button) in zip(positions, self.feature_buttons.items()):
            grid_layout.addWidget(button, *pos)

        settings_button = SettingButton('Settings', self.app.show_settings_page)
        self.layout.addWidget(settings_button, alignment=Qt.AlignBottom|Qt.AlignCenter)

    def do_something(self):
        pass

    def get_feature_status(self):
        pass