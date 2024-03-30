import sys
from src.qt_elements.buttons import (FeatureButton, SettingButton)
from src.mqtt_client import Client
from src.backend.wifi import Wifi
from src.backend.setup_device import SetupDevice
from src.pages.home import HomePage
from src.pages.settings import SettingsPage
from src.pages.setup_device import SetupDevicePage
from src.pages.system_info import SystemInfoPage

from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QFrame,
                             QGridLayout, QWidget, QStackedWidget)
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QPixmap



class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'EQUAL SAFE GUI'
        self.app_version = 'v1.0.0'
        self.client = Client('127.0.0.1', None, self)
        self.client.connect()
        self.init_device_setup()
        self.init_wifi()
        self.initUI()

    def handle_wifi_status(topic, payload):
        pass

    def setup_ended(self):
        self.show_home_page()

    def init_device_setup(self):
        self.device_setup = SetupDevice(self.client, self.setup_ended)

    def init_wifi(self):
        self.wifi = Wifi(self.client)
        self.wifi.subscribe_to_status(self.handle_wifi_status)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setStyleSheet("background-color: black;")

        # Stacked Widget
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Main menu
        self.home_page = HomePage(self)
        self.home_page.setup()

        # Setup device menu
        self.setup_device_page = SetupDevicePage(self)
        self.setup_device_page.setup()

        # Settings menu
        self.settings_page = SettingsPage(self)
        self.settings_page.setup()

        # Setup device menu
        self.system_info_page = SystemInfoPage(self)
        self.system_info_page.setup()

        # Add widgets to the stacked widget
        self.stacked_widget.addWidget(self.home_page.widget)
        self.stacked_widget.addWidget(self.settings_page.widget)
        self.stacked_widget.addWidget(self.setup_device_page.widget)
        self.stacked_widget.addWidget(self.system_info_page.widget)



    def do_something(self):
        print('CHANGE ME TO AN ACTUAL ACTION...')
        # example of changing status for feature button...
        # self.feature_buttons["Camera"].update_status_indicator(True)
        pass

    def get_feature_status(self):
        # Just for demonstration, should be replaced with actual status check logic
        return 'green'

    def show_home_page(self):
        print('show_home_page')
        self.stacked_widget.setCurrentWidget(self.home_page.widget)

    def show_settings_page(self):
        print('show_settings')
        self.stacked_widget.setCurrentWidget(self.settings_page.widget)

    def show_setup_device_page(self):
        self.stacked_widget.setCurrentWidget(self.setup_device_page.widget)

    def show_info_menu(self):
        self.stacked_widget.setCurrentWidget(self.system_info_page.widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.setGeometry(100, 100, 480, 800)
    ex.show()
    sys.exit(app.exec_())

