
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QScrollArea
from PyQt5.QtCore import QSize, Qt
from src.qt_elements.buttons import (FeatureButton, SettingButton, RemoveButton)

class WifiKnownNetworksPage():
    def __init__(self, app):
        self.widget = QWidget()
        self.layout = QVBoxLayout(self.widget)
        self.app = app

    def setup(self):
        scroll_area = QScrollArea(self.widget)
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.layout.addWidget(scroll_area)

        scroll_widget = QWidget()
        scroll_area.setWidget(scroll_widget)
        self.scroll_layout = QVBoxLayout(scroll_widget)

        # Placeholder for list of known networks - in actual app, fetch the real list
        known_networks_list = [
            "KanjiWifi",
            "TWifi",
            "Spectrum-1221",
            "Wifi Network 1",
            "Wifi Network 2",
            "Wifi Network Test 1",
            "Wifi Network Test 2",
            "XXXXXXXXXX",
            "HelloWorld",
        ]

        # Create a button for each known network
        for network in known_networks_list:
            button = RemoveButton(network, {'ssid': network}, self.remove_network)
            self.scroll_layout.addWidget(button)

        # Add back to wifi networks button at the end
        back_button = SettingButton("Wifi Settings", self.app.show_wifi_settings_page)
        self.layout.addWidget(back_button, alignment=Qt.AlignBottom | Qt.AlignCenter)

    def render_networks(self, network_list):
        # Remove all existing widgets from the layout and delete them
        while self.scroll_layout.count():
            item = self.scroll_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        # Add new widgets to the layout
        for network in network_list:
            button = RemoveButton(network, {'ssid': network}, self.remove_network)
            self.scroll_layout.addWidget(button)

    def remove_network(self, info):
        print('remove', info['ssid'])
        pass