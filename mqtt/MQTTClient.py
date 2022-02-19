import paho.mqtt.client as mqtt


class MQTTClient:
    def __init(self, port, hostname, subscribe_topics):
        self.client = mqtt.Client(client_id='mqtt_control')

        self.client.on_message = self.on_message

    def on_message(self, client, userdata, message):
        print(f'message received, payload: {message.payload.decode("utf-8")},'
              f'message topic: {message.topic}')

