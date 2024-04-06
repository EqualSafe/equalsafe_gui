from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QFrame,
                             QGridLayout, QWidget, QStackedWidget)

from PyQt5.QtCore import QSize, Qt

from src.qt_elements.buttons import (FeatureButton, SettingButton)


class SetupDevicePage():
    def __init__(self, app):
        self.widget = QWidget()
        self.layout = QVBoxLayout(self.widget)
        self.app = app

    def setup(self):
        text_label = QLabel(self.app.device_setup.setup_text)
        text_label.setStyleSheet("QLabel { color: white; font-size: 20px; }")

        settings_button = SettingButton('Cancel Setup', self.exit_device_setup, '#d52222')

        self.layout.addWidget(text_label, alignment=Qt.AlignCenter)
        self.layout.addWidget(settings_button, alignment=Qt.AlignBottom|Qt.AlignCenter)

    def enter_device_setup(self):
        self.app.device_setup.start_setup()
        self.app.show_setup_device_page()

    def exit_device_setup(self):
        self.app.device_setup.stop_setup()
        self.app.show_settings_page()

    def do_something():
        pass

    def get_feature_status():
        pass