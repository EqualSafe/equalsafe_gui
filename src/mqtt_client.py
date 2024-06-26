import ssl
import random
import socket
import paho.mqtt.client as mqtt
import re
import json
import time

class Client:
    def __init__(self, ip, password, udata):
        self.__device_ip = ip
        self.__password = password or "admin"
        self.__client_id = self.__generate_id(ip)
        self.__subscribers = {}
        self.__ssl_ctx = None
        self.__mqtt_client = None
        self.__user_data = udata
        self.on_connect = None
        self.__callbacks = {}

    def __generate_id(self, ip=None):
        ip = ip or self.__device_ip or str(random.randint(10000, 99999))
        return f"{ip.replace('.','')}_{random.randint(1000, 9999)}"

    def __match_topic(self, topic, sub):
        sub_parts = sub.split('/')
        topic_parts = topic.split('/')

        for i in range(len(sub_parts)):
            if sub_parts[i] == '#':
                return True
            if i >= len(topic_parts) or (sub_parts[i] != '+' and sub_parts[i] != topic_parts[i]):
                return False
            elif sub_parts[i] == '+':
                continue
        if len(sub_parts) < len(topic_parts) and sub_parts[-1] != '#':
            return False

        return True

    def __default_on_msg(self, client, userdata, msg, *_):
        topic = msg.topic
        payload = {}
        try:
            payload = json.loads(msg.payload)
        except Exception as e:
            print(topic, 'not a valid json payload')
            return

        callbacks_copy = self.__callbacks.copy()
        for sub_topic in callbacks_copy:
            if self.__match_topic(topic, sub_topic):
                for callback in callbacks_copy[sub_topic]:
                    callback(topic, payload)

    def __on_connect(self, client, userdata, flags, rc, *_):
        if not self.on_connect:
            return

        return_msg = {
            0: "Connection successful",
            1: "Connection refused - incorrect protocol version",
            2: "Connection refused - invalid client identifier",
            3: "Connection refused - server unavailable",
            4: "Connection refused - bad username or password",
            5: "Connection refused - not authorised "
        }

        success = True
        if rc > 0:
            success = False

        self.on_connect(success, return_msg[int(rc)])

    def connect(self):
        '''
            Connects to the teradek device with the specified ip
        '''
        if self.__mqtt_client:
            self.disconnect()

        self.__mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=self.__client_id, clean_session=True, reconnect_on_failure=True, protocol= mqtt.MQTTv31, userdata=self.__user_data)
        # self.__mqtt_client.username_pw_set("admin", self.__password)

        # # cert config
        # self.__create_cert()
        # self.__mqtt_client.tls_set_context(self.__ssl_ctx)
        # self.__mqtt_client.tls_insecure_set(True)

        try:
            self.__mqtt_client.connect(self.__device_ip, 1883)
        except socket.timeout:
            return False, "Socket Timeout"
        except OSError as e:
            if e.errno == 113:
                return False, "Cannot Connect to IP Address"
            elif e.errno == -2:
                return False, "Invalid IP Address"
            else:
                return False, f"OS Error {e.errno}"
        except Exception as e:
            return False, str(e)

        self.__mqtt_client.on_message = self.__default_on_msg
        self.__mqtt_client.on_connect = self.__on_connect
        self.__mqtt_client.loop_start()

        return True


    def disconnect(self):
        '''
            Disconnects from the teradek device
        '''
        self.__mqtt_client.loop_stop()
        self.__mqtt_client.disconnect()
        self.__mqtt_client = None


    def reconnect(self):
        '''
            Reconnects to the teradek device
        '''
        self.disconnect()
        self.connect()

    def set_ip(self, new_ip):
        '''
            Changes the device IP and reconnects
        '''
        self.__device_ip = new_ip
        self.reconnect()

    def publish(self, topic, payload) -> bool:
        '''
            Publishes the payload under the topic provided
            returns:
            - success: bool
        '''
        if not self.__mqtt_client.is_connected():
            return False, "MQTT not connected"

        self.__mqtt_client.publish(topic=topic, payload=json.dumps(payload))
        return True

    def subscribe(self, topic, callback) -> bool:
        '''
            Subscibes to the topic provided and triggers the callback on message
            returns:
            - success: bool
        '''
        if not self.__mqtt_client.is_connected():
            return False, "MQTT not connected"

        if not self.__callbacks.get(topic):
            self.__callbacks[topic] = []
            self.__mqtt_client.subscribe(topic=topic)

        self.__callbacks[topic].append(callback)
        return True

    def unsubscribe(self, topic, callback):
        '''
            unsubscibes from a topic and removes all the callbacks
            returns:
            - success: bool
        '''
        if not self.__mqtt_client.is_connected():
            return False, "MQTT not connected"

        if self.__callbacks.get(topic):
            idx = self.__callbacks[topic].index(callback)
            del self.__callbacks[topic][idx]

            if len(self.__callbacks[topic]) == 0:
                del self.__callbacks[topic]
                self.__mqtt_client.unsubscribe(topic=topic)

        return True