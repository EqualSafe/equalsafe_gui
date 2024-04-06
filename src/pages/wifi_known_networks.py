
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QScrollArea
from PyQt5.QtCore import QObject, QSize, Qt, pyqtSignal
from src.qt_elements.buttons import (FeatureButton, SettingButton, RemoveButton)

import time

class WifiKnownNetworksPage(QObject):

    update_known_networks_signal = pyqtSignal(object) # signal to update the known list

    def __init__(self, app):
        super().__init__()
        self.widget = QWidget()
        self.layout = QVBoxLayout(self.widget)
        self.app = app
        self.update_known_networks_signal.connect(self.render_networks)

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
            "NO NETWORKS",
        ]

        # Create a button for each known network
        for network in known_networks_list:
            button = RemoveButton(network, {'ssid': network}, self.remove_network)
            self.scroll_layout.addWidget(button)

        # Add back to wifi networks button at the end
        back_button = SettingButton("Wifi Settings", self.app.show_wifi_settings_page)
        self.layout.addWidget(back_button, alignment=Qt.AlignBottom | Qt.AlignCenter)

    def refresh_networks(self):
        req_id = str(int(time.time()))
        req_topic = f'System/wifi/list_known_networks/{req_id}'

        def on_refresh_networks(topic, payload):
            self.app.client.unsubscribe(f'{req_topic}/+', on_refresh_networks)
            topic_array = topic.split('/')
            status = topic_array[-1]
            if status == 'success':
                self.update_known_networks_signal.emit(payload['networks'])

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
            button = RemoveButton(network, {'ssid': network}, self.remove_network)
            self.scroll_layout.addWidget(button)

    def remove_network(self, info):
        print('remove', info['ssid'])
        req_id = str(int(time.time()))
        req_topic = f'System/wifi/remove_network/{req_id}'

        def on_message(topic, payload):
            self.app.client.unsubscribe(f'{req_topic}/+', on_message)
            topic_array = topic.split('/')
            status = topic_array[-1]
            if status == 'success':
                self.refresh_networks()
            elif status == 'error':
                print(topic, 'error:', info['ssid'])

        self.app.client.subscribe(f'{req_topic}/+', on_message)
        self.app.client.publish(f'{req_topic}', {'ssid': info['ssid']})
        pass