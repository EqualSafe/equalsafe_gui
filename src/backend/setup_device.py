from ..mqtt_client import Client
import json

class SetupDevice():
    def __init__(self, client, on_setup_end):
        self.client = client
        self.in_setup = False
        self.on_setup_end = on_setup_end
        self.setup_text = 'Please continue the setup on your phone.\n1. Pair bluetooth with "equalsafe"\n2. Open the EqualSafe app\n    and follow the instructions\n'

    def __wifi_connected(self, topic, payload):
        print('SetupDevice wifi connected')
        if payload.get('state') == 'running':
            self.stop_setup()
            self.on_setup_end()

    def start_setup(self):
        print('SetupDevice start_setup')

        if self.in_setup:
            return False

        self.in_setup = True

        # Stop the wifi
        self.client.publish('System/wifi/stop/1111', '{}')
        # Start bluetooth
        self.client.publish('System/bluetooth/start/1111', '{}')
        # wait for the bluetooth to be connected
        self.client.subscribe('System/wifi/Info', self.__wifi_connected)

        return True

    def stop_setup(self):
        print('SetupDevice stop_setup')
        if not self.in_setup:
            return False

        self.in_setup = False
        self.client.unsubscribe('System/wifi/Info', self.__wifi_connected)
        self.client.publish('System/bluetooth/stop/1111', '{}')

        return True
