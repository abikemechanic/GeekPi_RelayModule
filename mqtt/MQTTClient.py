import paho.mqtt.client as mqtt


class MQTTClient:
    def __init__(self, port, hostname, subscribe_topics=[]):
        self.client = mqtt.Client(client_id='mqtt_control')
        self.port = port
        self.hostname = hostname

        # self.client.on_message = self.on_message

    def on_message(self, client, userdata, message):
        print(f'message received, payload: {message.payload.decode("utf-8")},'
              f'message topic: {message.topic}')

    def subscribe_to_topic(self, topic, qos=0):
        self.client.subscribe(topic, qos=0)

    def unsubscribe_from_topic(self, topic):
        self.client.unsubscribe(topic)


