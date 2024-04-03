from mqtt_client import Client
import time


if __name__ == '__main__':
    mqtt_client = Client('127.0.0.1', None, {})
    mqtt_client.connect()
    time.sleep(3)

    mqtt_client.publish('System/wifi/Info', {'state': 'running'})
    mqtt_client.publish('System/bluetooth/Info', {'state': 'running'})
    mqtt_client.publish('Media/video_stream/Info', {'state': 'running'})
    mqtt_client.publish('System/deadbolt/status', {'state': 'Locked'})

    def wifi_cb(topic, payload):
        print(topic, payload)
    mqtt_client.subscribe('System/wifi/+/+', wifi_cb)

    def lock_cb(topic, payload):
        print(topic, payload)
        mqtt_client.publish('System/deadbolt/status', {'state': 'Unlocked'})
    mqtt_client.subscribe('System/deadlock/+/+', lock_cb)


    def known_networks_cb(topic, payload):
        print(topic, payload)
        mqtt_client.publish(f'{topic}/success', {'networks': ['mqtt refresh works', 'fake mqtt system']})
    mqtt_client.subscribe('System/wifi/list_known_networks/+', known_networks_cb)

    def available_networks_cb(topic, payload):
        print(topic, payload)
        mqtt_client.publish(f'{topic}/success', {'networks': ['mqtt refresh works', 'fake mqtt system']})
    mqtt_client.subscribe('System/wifi/list_available_networks/+', available_networks_cb)


    while True:
        time.sleep(1)





