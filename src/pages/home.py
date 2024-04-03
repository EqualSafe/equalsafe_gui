from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QFrame,
                             QGridLayout, QWidget, QStackedWidget)

from PyQt5.QtCore import QSize, Qt

from src.qt_elements.buttons import (FeatureButton, SettingButton)


class HomePage():
    def __init__(self, app):
        self.widget = QWidget()
        self.layout = QVBoxLayout(self.widget)
        self.app = app
        self.camera_status = False
        self.bluetooth_status = False
        self.wifi_status = False
        self.deadlock_status = False

    def setup(self):
        # # Screen Placeholder
        screen_placeholder = QLabel()
        screen_placeholder.setFixedSize(QSize(460, 200))
        screen_placeholder.setStyleSheet("background-color: gray; border-radius: 10px;")
        self.layout.addWidget(screen_placeholder, alignment=Qt.AlignCenter)

        # Grid Layout for feature buttons
        grid_layout = QGridLayout()
        self.layout.addLayout(grid_layout)

        # Feature buttons
        self.feature_buttons = {
            "Camera": FeatureButton("Camera", self.toggle_camera, self.get_feature_status),
            "Lock": FeatureButton("Lock", self.toggle_deadlock, self.get_feature_status),
            "Bluetooth": FeatureButton("Bluetooth", self.toggle_bluetooth, self.get_feature_status),
            "Wifi": FeatureButton("Wifi", self.toggle_wifi, self.get_feature_status)
        }

        positions = [(i, j) for i in range(2) for j in range(2)]
        for pos, (name, button) in zip(positions, self.feature_buttons.items()):
            grid_layout.addWidget(button, *pos)

        settings_button = SettingButton('Settings', self.app.show_settings_page)
        self.layout.addWidget(settings_button, alignment=Qt.AlignBottom|Qt.AlignCenter)

        # Comms
        self.app.client.subscribe('Media/video_stream/Info', self.handle_camera_info)
        self.app.client.subscribe('System/bluetooth/Info', self.handle_bluetooth_info)
        self.app.client.subscribe('System/wifi/Info', self.handle_wifi_info)
        self.app.client.subscribe('System/deadbolt/status', self.handle_deadlock_info)

    def handle_camera_info(self, topic, payload):
        self.feature_buttons['Bluetooth'].update_status_indicator(True if payload.get('state') == 'running' else False)
        self.camera_status = True if payload.get('state') == 'running' else False

    def handle_bluetooth_info(self, topic, payload):
        self.feature_buttons['Bluetooth'].update_status_indicator(True if payload.get('state') == 'running' else False)
        self.bluetooth_status = True if payload.get('state') == 'running' else False

    def handle_wifi_info(self, topic, payload):
        self.feature_buttons['Wifi'].update_status_indicator(True if payload.get('state') == 'running' else False)
        self.wifi_status = True if payload.get('state') == 'running' else False

    def handle_deadlock_info(self, topic, payload):
        self.feature_buttons['Lock'].update_status_indicator(True if payload.get('state') == 'Locked' else False)
        self.feature_buttons['Lock'].setText('Unlock' if payload.get('state') == 'Locked' else 'Lock')
        self.deadlock_status = True if payload.get('state') == 'Locked' else False

    def toggle_camera(self):
        command = 'stop' if self.camera_status else 'start'
        self.app.client.publish(f'Media/video_stream/{command}/1234', {})

    def toggle_bluetooth(self):
        command = 'stop' if self.bluetooth_status else 'start'
        self.app.client.publish(f'System/bluetooth/{command}/1234', {})

    def toggle_wifi(self):
        command = 'stop' if self.wifi_status else 'start'
        self.app.client.publish(f'System/wifi/{command}/1234', {})

    def toggle_deadlock(self):
        command = 'unlock' if self.deadlock_status else 'lock'
        self.app.client.publish(f'System/deadlock/{command}/1234', {})

    def do_something(self):
        pass

    def get_feature_status(self):
        pass