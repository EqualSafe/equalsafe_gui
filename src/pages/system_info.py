from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QFrame,
                             QGridLayout, QWidget, QStackedWidget)

from PyQt5.QtCore import QSize, Qt

from src.qt_elements.buttons import (FeatureButton, SettingButton)
from src.backend.system_control import (reboot_device)


class SystemInfoPage():
    def __init__(self, app):
        self.widget = QWidget()
        self.layout = QVBoxLayout(self.widget)
        self.app = app

    def setup(self):
        text_label = QLabel('EqualSafe\nAll rights reserved\n\nversion: %s\nserial: ES000001' % self.app.app_version)
        text_label.setStyleSheet("QLabel { color: white; font-size: 28px; }")
        reboot_device_button = SettingButton('Reboot', reboot_device, '#e9950c')
        unlink_device_button = SettingButton('Unlink Device', self.app.show_settings_page, '#e9950c')
        factory_reset_button = SettingButton('Factory reset', self.app.show_settings_page, '#d52222')
        settings_button = SettingButton('Settings', self.app.show_settings_page)

        self.layout.addWidget(text_label, alignment=Qt.AlignCenter)
        self.layout.addWidget(reboot_device_button, alignment=Qt.AlignHCenter)
        self.layout.addWidget(unlink_device_button, alignment=Qt.AlignHCenter)
        self.layout.addWidget(factory_reset_button, alignment=Qt.AlignHCenter)
        self.layout.addWidget(settings_button, alignment=Qt.AlignBottom|Qt.AlignHCenter)

    def do_something(self):
        pass

    def get_feature_status(self):
        pass