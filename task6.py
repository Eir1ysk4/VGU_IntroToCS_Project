import paho.mqtt.client as mqttclient
import time
import json

BROKER_ADDRESS = "demo.thingsboard.io"  #mqtt.thingsboard.cloud"
PORT = 1883
THINGS_BOARD_ACCESS_TOKEN = "QxslxIX70oPecwXifyjo"
class Task6:

    client = None
    def __init__(self):
        print("Init task 6")
        self.client = mqttclient.Client("Gateway_Thingsboard")
        self.client.username_pw_set(THINGS_BOARD_ACCESS_TOKEN)

        self.client.on_connect = self.connected()
        self.client.connect(BROKER_ADDRESS, 1883)
        self.client.loop_start()

        self.client.on_subscribe = self.subscribed()
        # self.client.on_message = self.recv_message()
        return

    def Task6_Run(self, data):
        print("Task 6 is activated!!!!")
        temp = data.temp_kelvin
        humid = data.humidity

        longitude = data.lon
        latitude = data.lat
        while True:
            collect_data = {'temperature': temp, 'humidity': humid, 'longitude': longitude,
                            'latitude': latitude}
            print(collect_data)
            temp += 1
            humid += 1
            self.client.publish('v1/devices/me/telemetry', json.dumps(collect_data), 1)
            time.sleep(5)

    def subscribed(self):
        print("Subscribed...")

    def connected(self):
        rc = 0

        if rc == 0:
            print("Thingsboard connected successfully!!")
            self.client.subscribe("v1/devices/me/rpc/request/+")
        else:
            print("Connection is failed")
    def recv_message(client, message):
        print("Received: ", message.payload.decode("utf-8"))
        temp_data = {'value': True}
        try:
            jsonobj = json.loads(message.payload)
            if jsonobj['method'] == "setValue":
                temp_data['value'] = jsonobj['params']
                client.publish('v1/devices/me/attributes', json.dumps(temp_data), 1)
        except:
            pass