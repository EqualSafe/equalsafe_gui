class Wifi:
    def __init__(self, client):
        self.__topic = 'System/Wifi'
        self.__client = client

    # calls topic + /start
    def start_wifi(self):
        self.__client.publish(self.__topic + '/start', '{}')
        pass

    # calls topic + /stop
    def stop_wifi(self):
        self.__client.publish(self.__topic + '/stop', '{}')
        pass

    # based on the status of the wifi, we either start or stop it
    def toggle_wifi(self):
        pass

    # keep updating the information
    def subscribe_to_status(self, callback):
        self.__client.subscribe("System/Wifi/Info", callback)
        pass