from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QFrame,
                             QGridLayout, QWidget, QStackedWidget)

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap

from src.qt_elements.buttons import (FeatureButton, SettingButton)
from src.backend.system_control import (reboot_device)


class SystemInfoPage():
    def __init__(self, app):
        self.widget = QWidget()
        self.layout = QVBoxLayout(self.widget)
        self.app = app

    def setup(self):
        logo = QLabel('')
        logo.setPixmap(QPixmap('images/logo_white_96.png'))
        text_label = QLabel('EqualSafe OS\nAll rights reserved\n\nversion: %s\nserial: ES000001' % self.app.app_version)
        text_label.setStyleSheet("QLabel { color: white; font-size: 20px; }")
        check_for_updates_button = SettingButton('Check for updates', self.app.show_settings_page, '#308d46')
        reboot_device_button = SettingButton('Reboot', reboot_device, '#e9950c')
        factory_reset_button = SettingButton('Factory reset', self.app.show_settings_page, '#d52222')
        settings_button = SettingButton('Settings', self.app.show_settings_page)

        self.layout.addWidget(logo, alignment=Qt.AlignCenter)
        self.layout.addWidget(text_label, alignment=Qt.AlignCenter)
        self.layout.addWidget(check_for_updates_button, alignment=Qt.AlignHCenter)
        self.layout.addWidget(reboot_device_button, alignment=Qt.AlignHCenter)
        self.layout.addWidget(factory_reset_button, alignment=Qt.AlignHCenter)
        self.layout.addWidget(settings_button, alignment=Qt.AlignBottom|Qt.AlignHCenter)

    def do_something(self):
        pass

    def get_feature_status(self):
        pass