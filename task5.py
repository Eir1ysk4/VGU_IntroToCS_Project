import paho.mqtt.client as mqttclient
from shared_resources import resources
import json

BROKER_ADDRESS = "demo.thingsboard.io"  # mqtt.thingsboard.cloud"
PORT = 1883
THINGS_BOARD_ACCESS_TOKEN = "QxslxIX70oPecwXifyjo"


class Task5:
    client = None

    def __init__(self):
        try:
            print("Init task 5")
            self.client = mqttclient.Client("Gateway_Thingsboard")
            self.client.username_pw_set(THINGS_BOARD_ACCESS_TOKEN)

            self.client.on_connect = self.connected()
            self.client.connect(BROKER_ADDRESS, 1883)
            self.client.loop_start()

            self.client.on_subscribe = self.subscribed()
            # self.client.on_message = self.recv_message()
            return
        except Exception as e:
            print(f"Error during initialization: {e}")

    def Task5_Run(self):
        try:
            print("Task 5 is activated!!!!")
            weather_data = resources.shared_data.get('task4_output')
            print(weather_data)
            if weather_data is not None:
                temp = weather_data['temp_celsius']
                humid = weather_data['humidity']
                longitude = weather_data['lon']
                latitude = weather_data['lat']
                collect_data = {'temperature': temp, 'humidity': humid, 'longitude': longitude,
                                'latitude': latitude}
                print(collect_data)
                self.client.publish('v1/devices/me/telemetry', json.dumps(collect_data), 1)
            else:
                print("Weather data not available yet.")
        except Exception as e:
            print(f"Error in Task5_Run: {e}")

    def subscribed(self):
        print("Subscribed...")

    def connected(self):
        try:
            rc = 0
            if rc == 0:
                print("Thingsboard connected successfully!!")
                self.client.subscribe("v1/devices/me/rpc/request/+")
            else:
                print("Connection is failed")
        except Exception as e:
            print(f"Error during connection: {e}")

    def recv_message(client, message):
        print("Received: ", message.payload.decode("utf-8"))
        temp_data = {'value': True}
        try:
            jsonobj = json.loads(message.payload)
            if jsonobj['method'] == "setValue":
                temp_data['value'] = jsonobj['params']
                client.publish('v1/devices/me/attributes', json.dumps(temp_data), 1)
        except Exception as e:
            print(f"Error during publishing data: {e}")

