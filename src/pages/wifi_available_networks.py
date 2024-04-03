
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QScrollArea
from PyQt5.QtCore import QObject, QSize, Qt, pyqtSignal
from src.qt_elements.buttons import (SettingButton, AddButton)
import time

class WifiAvailableNetworksPage(QObject):

    update_available_networks_signal = pyqtSignal(object)

    def __init__(self, app):
        super().__init__()
        self.widget = QWidget()
        self.layout = QVBoxLayout(self.widget)
        self.app = app
        self.update_available_networks_signal.connect(self.render_networks)

    def setup(self):
        scroll_area = QScrollArea(self.widget)
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.layout.addWidget(scroll_area)

        scroll_widget = QWidget()
        scroll_area.setWidget(scroll_widget)
        self.scroll_layout = QVBoxLayout(scroll_widget)

        # Placeholder for list of available networks - in actual app, fetch the real list
        available_networks_list = [
            "NO NETWORKS"
        ]

        # Create a button for each available network
        for network in available_networks_list:
            button = AddButton(network, {'ssid': network}, self.add_network)
            self.scroll_layout.addWidget(button)

        # Add refresh button
        refresh_button = SettingButton("Refresh", self.refresh_networks)

        # Add back to wifi networks button at the end
        back_button = SettingButton("Wifi Settings", self.app.show_wifi_settings_page)
        self.layout.addWidget(refresh_button, alignment=Qt.AlignBottom | Qt.AlignCenter)
        self.layout.addWidget(back_button, alignment=Qt.AlignBottom | Qt.AlignCenter)

    def add_network(self, info):
        self.app.wifi_add_network_page.set_params(info['ssid'], '')
        self.app.show_wifi_add_network_page()
        pass

    def refresh_networks(self):
        self.render_networks(['Scanning...'])
        req_id = str(int(time.time()))
        req_topic = f'System/wifi/list_available_networks/{req_id}'

        def on_refresh_networks(topic, payload):
            self.app.client.unsubscribe(f'{req_topic}/+', on_refresh_networks)
            topic_array = topic.split('/')
            status = topic_array[-1]
            if status == 'success':
                self.update_available_networks_signal.emit(payload['networks'])

        self.app.client.subscribe(f'{req_topic}/+', on_refresh_networks)
        self.app.client.publish(f'{req_topic}', {})

    def render_networks(self, network_list):
        # Remove all existing widgets from the layout and delete them
        while self.scroll_layout.count():
            item = self.scroll_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        # Add new widgets to the layout
        for network in network_list:
            button = AddButton(network, {'ssid': network}, self.add_network)
            self.scroll_layout.addWidget(button)
