
from PyQt5.QtWidgets import QVBoxLayout, QWidget
from PyQt5.QtCore import QSize, Qt
from src.qt_elements.buttons import (FeatureButton, SettingButton)


class WifiSettingsPage:
    def __init__(self, app):
        self.widget = QWidget()
        self.layout = QVBoxLayout(self.widget)
        self.app = app

    def setup(self):
        self.known_networks_button = SettingButton("Known Networks", self.app.show_wifi_known_networks_page)
        self.available_networks_button = SettingButton("Available Networks", self.app.show_wifi_available_networks_page)
        self.custom_network_button = SettingButton("Custom Network", self.show_add_network)
        self.settings_button = SettingButton("Settings", self.app.show_settings_page)

        self.layout.addWidget(self.known_networks_button, alignment=Qt.AlignHCenter)
        self.layout.addWidget(self.available_networks_button, alignment=Qt.AlignHCenter)
        self.layout.addWidget(self.custom_network_button, alignment=Qt.AlignHCenter)
        self.layout.addWidget(self.settings_button, alignment=Qt.AlignBottom | Qt.AlignCenter)

    def show_add_network(self):
        self.app.wifi_add_network_page.set_params('', '')
        self.app.show_wifi_add_network_page()