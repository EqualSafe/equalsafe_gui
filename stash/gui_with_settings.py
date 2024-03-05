import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout,
                             QLabel, QGridLayout, QWidget, QStackedWidget, QHBoxLayout)
from PyQt5.QtCore import QSize, Qt

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

        # Stacked Widget
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Main menu setup
        self.main_menu_widget = QWidget()
        self.main_menu_layout = QVBoxLayout(self.main_menu_widget)
        self.main_menu_layout.setAlignment(Qt.AlignTop)
        self.setup_main_menu()

        # Settings menu setup
        self.settings_menu_widget = QWidget()
        self.settings_menu_layout = QVBoxLayout(self.settings_menu_widget)
        self.settings_menu_layout.setAlignment(Qt.AlignTop)
        self.setup_settings_menu()

        # Add widgets to the stacked widget
        self.stacked_widget.addWidget(self.main_menu_widget)
        self.stacked_widget.addWidget(self.settings_menu_widget)

        self.show()

    def setup_main_menu(self):
        # Screen Placeholder
        screen_placeholder = QLabel()
        screen_placeholder.setFixedSize(QSize(280, 160))
        screen_placeholder.setStyleSheet("background-color: gray; border-radius: 10px;")
        self.main_menu_layout.addWidget(screen_placeholder, alignment=Qt.AlignCenter)

        # Grid Layout for buttons
        grid_layout = QGridLayout()
        self.main_menu_layout.addLayout(grid_layout)
        grid_layout.setSpacing(10)

        # Buttons
        self.add_button_with_indicator('Camera', self.trigger_camera, grid_layout, self.get_camera_status, 0, 0)
        self.add_button_with_indicator('Lock', self.trigger_lock, grid_layout, self.get_lock_status, 0, 1)
        self.add_button_with_indicator('Bluetooth', self.trigger_bluetooth, grid_layout, self.get_bluetooth_status, 1, 0)
        self.add_button_with_indicator('Wifi', self.trigger_wifi, grid_layout, self.get_wifi_status, 1, 1)

        # Settings Button
        settings_button = self.add_button('Settings', self.show_settings, grid_layout, 2, 0, colspan=2)
        settings_button.setFixedSize(QSize(280, 50))

    def setup_settings_menu(self):
        # Create and style buttons for the settings menu
        self.add_button('Setup Device', self.setup_device, self.settings_menu_layout)
        self.add_button('Wifi Networks', self.wifi_networks, self.settings_menu_layout)
        self.add_button('Bluetooth Devices', self.bluetooth_devices, self.settings_menu_layout)

        # Home Screen Button
        home_button = self.add_button('Home Screen', self.show_main_menu, self.settings_menu_layout)
        home_button.setFixedSize(QSize(280, 50))

    def add_button(self, text, function, layout, row=None, col=None, colspan=1):
        button = QPushButton(text)
        button.clicked.connect(function)
        button.setFixedSize(QSize(280, 50))
        button.setStyleSheet(
            "QPushButton {background-color: gray; color: white; border-radius: 10px;}"
            "QPushButton:pressed {background-color: #555555;}"
        )
        if isinstance(layout, QGridLayout):
            layout.addWidget(button, row, col, 1, colspan)
        else:
            layout.addWidget(button, alignment=Qt.AlignCenter)
        return button

    def add_button_with_indicator(self, text, function, layout, status_func, row=None, col=None, colspan=1):
        # Create a container widget for the button and the indicator
        container = QWidget()
        container_layout = QHBoxLayout()
        container.setLayout(container_layout)
        container.setStyleSheet("background-color: black;")  # Match the main window background

        # Create the button
        button = QPushButton(text)
        button.clicked.connect(function)
        button.setFixedSize(QSize(130, 50))
        button.setStyleSheet(
            "QPushButton {background-color: gray; color: white; border-radius: 10px;}"
            "QPushButton:pressed {background-color: #555555;}"
        )

        # Create the indicator label
        indicator = QLabel()
        indicator.setFixedSize(QSize(20, 20))
        indicator.setStyleSheet(f"background-color: {status_func()}; border-radius: 10px;")
        container_layout.addWidget(indicator)
        container_layout.addWidget(button)

        # Add the container to the specified layout
        if isinstance(layout, QGridLayout):
            layout.addWidget(container, row, col, 1, colspan)
        else:
            layout.addWidget(container, alignment=Qt.AlignCenter)
        return container, button, indicator

    # Placeholder functions for button status
    def get_camera_status(self):
        # Return 'green' if the camera is enabled, 'red' otherwise
        return 'green'

    def get_lock_status(self):
        # Return 'green' if the device is locked, 'red' otherwise
        return 'red'

    def get_bluetooth_status(self):
        # Return 'green' if Bluetooth is on, 'red' otherwise
        return 'green'

    def get_wifi_status(self):
        # Return 'green' if WiFi is connected, 'red' otherwise
        return 'red'

    def show_settings(self):
        self.stacked_widget.setCurrentIndex(1)

    def show_main_menu(self):
        self.stacked_widget.setCurrentIndex(0)

    # Placeholder functions for settings actions
    def setup_device(self):
        print("Setup Device function triggered")

    def wifi_networks(self):
        print("Wifi Networks function triggered")

    def bluetooth_devices(self):
        print("Bluetooth Devices function triggered")

    # Main functionality button actions
    def trigger_camera(self):
        print("Camera function triggered")

    def trigger_lock(self):
        print("Lock function triggered")

    def trigger_bluetooth(self):
        print("Bluetooth function triggered")

    def trigger_wifi(self):
        print("WiFi function triggered")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
