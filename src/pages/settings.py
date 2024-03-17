from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QFrame,
                             QGridLayout, QWidget, QStackedWidget)

from PyQt5.QtCore import QSize, Qt

from src.qt_elements.buttons import (FeatureButton, SettingButton)


class SettingsPage():
    def __init__(self, app):
        self.widget = QWidget()
        self.layout = QVBoxLayout(self.widget)
        self.app = app

    def setup(self):
        setup_button = SettingButton('Setup Device', self.app.setup_device_page.enter_device_setup)
        wifi_button = SettingButton('Wifi Networks', self.app.show_home_page)
        bluetooth_button = SettingButton('Bluetooth Devices', self.app.show_home_page)
        info_button = SettingButton('System Info', self.app.show_info_menu)
        home_button = SettingButton('Home', self.app.show_home_page)

        self.layout.addWidget(setup_button, alignment=Qt.AlignHCenter)
        self.layout.addWidget(wifi_button, alignment=Qt.AlignHCenter)
        self.layout.addWidget(bluetooth_button, alignment=Qt.AlignHCenter)
        self.layout.addWidget(info_button, alignment=Qt.AlignHCenter)
        self.layout.addWidget(home_button, alignment=Qt.AlignBottom | Qt.AlignCenter)

    def do_something(self):
        pass

    def get_feature_status(self):
        pass