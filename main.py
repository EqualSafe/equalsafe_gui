import sys
from src.qt_elements.buttons import (FeatureButton, SettingButton)
from src.mqtt_client import Client
from src.backend.wifi import Wifi
from src.backend.setup_device import SetupDevice

from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QFrame,
                             QGridLayout, QWidget, QStackedWidget)
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QPixmap

app_version = 'v1.0.0'

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'EQUAL SAFE GUI'
        self.client = Client('127.0.0.1', None, self)
        self.client.connect()
        self.init_device_setup()
        self.init_wifi()
        self.initUI()

    def handle_wifi_status(topic, payload):
        pass

    def setup_ended(self):
        self.show_main_menu()

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
        self.main_menu_widget = QWidget()
        self.main_menu_layout = QVBoxLayout(self.main_menu_widget)
        self.setup_main_menu()

        # Settings menu
        self.settings_menu_widget = QWidget()
        self.settings_menu_layout = QVBoxLayout(self.settings_menu_widget)
        self.setup_settings_menu()

        # Setup device menu
        self.setup_device_widget = QWidget()
        self.setup_device_layout = QVBoxLayout(self.setup_device_widget)
        self.setup_setup_device_menu()

         # Setup device menu
        self.info_menu_widget = QWidget()
        self.info_menu_layout = QVBoxLayout(self.info_menu_widget)
        self.setup_info_menu()

        # Add widgets to the stacked widget
        self.stacked_widget.addWidget(self.main_menu_widget)
        self.stacked_widget.addWidget(self.settings_menu_widget)
        self.stacked_widget.addWidget(self.setup_device_widget)
        self.stacked_widget.addWidget(self.info_menu_widget)

    def setup_main_menu(self):
        # # Screen Placeholder
        screen_placeholder = QLabel()
        screen_placeholder.setFixedSize(QSize(280, 160))
        screen_placeholder.setStyleSheet("background-color: gray; border-radius: 10px;")
        self.main_menu_layout.addWidget(screen_placeholder, alignment=Qt.AlignCenter)

        # Grid Layout for feature buttons
        grid_layout = QGridLayout()
        self.main_menu_layout.addLayout(grid_layout)

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

        settings_button = SettingButton('Settings', self.show_settings)
        self.main_menu_layout.addWidget(settings_button, alignment=Qt.AlignBottom|Qt.AlignCenter)

    def setup_settings_menu(self):
        setup_button = SettingButton('Setup Device', self.enter_device_setup)
        wifi_button = SettingButton('Wifi Networks', self.show_main_menu)
        bluetooth_button = SettingButton('Bluetooth Devices', self.show_main_menu)
        info_button = SettingButton('Info', self.show_info_menu)
        home_button = SettingButton('Home', self.show_main_menu)

        self.settings_menu_layout.addWidget(setup_button, alignment=Qt.AlignHCenter)
        self.settings_menu_layout.addWidget(wifi_button, alignment=Qt.AlignHCenter)
        self.settings_menu_layout.addWidget(bluetooth_button, alignment=Qt.AlignHCenter)
        self.settings_menu_layout.addWidget(info_button, alignment=Qt.AlignHCenter)
        self.settings_menu_layout.addWidget(home_button, alignment=Qt.AlignBottom | Qt.AlignCenter)

    def setup_setup_device_menu(self):
        # Create a QLabel with some text
        text_label = QLabel(self.device_setup.setup_text)
        text_label.setStyleSheet("QLabel { color: white; font-size: 14px; }")

        settings_button = SettingButton('Cancel setup', self.exit_device_setup, '#d52222')

        self.setup_device_layout.addWidget(text_label, alignment=Qt.AlignCenter)
        self.setup_device_layout.addWidget(settings_button, alignment=Qt.AlignBottom|Qt.AlignCenter)
        #self.setup_device_layout.addWidget(home_button, alignment=Qt.AlignCenter)

    def setup_info_menu(self):
        text_label = QLabel('EqualSafe\nAll rights reserved\n\nversion: %s\nserial: ES000001' % app_version)
        text_label.setStyleSheet("QLabel { color: white; font-size: 14px; }")
        unlink_device_button = SettingButton('Unlink device', self.show_settings, '#e9950c')
        factory_reset_button = SettingButton('Factory reset', self.show_settings, '#d52222')
        settings_button = SettingButton('Settings', self.show_settings)

        self.info_menu_layout.addWidget(text_label, alignment=Qt.AlignCenter)
        self.info_menu_layout.addWidget(unlink_device_button, alignment=Qt.AlignHCenter)
        self.info_menu_layout.addWidget(factory_reset_button, alignment=Qt.AlignHCenter)
        self.info_menu_layout.addWidget(settings_button, alignment=Qt.AlignBottom|Qt.AlignHCenter)

    def do_something(self):
        print('CHANGE ME TO AN ACTUAL ACTION...')
        # example of changing status for feature button...
        # self.feature_buttons["Camera"].update_status_indicator(True)
        pass

    def get_feature_status(self):
        # Just for demonstration, should be replaced with actual status check logic
        return 'green'

    def show_settings(self):
        print('show_settings')
        self.stacked_widget.setCurrentWidget(self.settings_menu_widget)

    def show_main_menu(self):
        print('show_main_menu')
        self.stacked_widget.setCurrentWidget(self.main_menu_widget)

    def enter_device_setup(self):
        print('show_device_setup')
        self.device_setup.start_setup()
        self.stacked_widget.setCurrentWidget(self.setup_device_widget)

    def exit_device_setup(self):
        self.device_setup.stop_setup()
        self.stacked_widget.setCurrentWidget(self.settings_menu_widget)

    def show_info_menu(self):
        self.stacked_widget.setCurrentWidget(self.info_menu_widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.setGeometry(100, 100, 320, 480)
    ex.show()
    sys.exit(app.exec_())

