import paho.mqtt.client as mqtt


class MQTTTopic:
    def __init__(self, topic: str, subscribe: bool, publish: bool, message_callback=None):
        self.topic = topic
        self.subscribe = subscribe
        self.publish = publish
        if message_callback:
            self.message_callback = message_callback

    def send_message(self, json_message, mqtt_client: mqtt):
        mqtt_client.publish(self.topic, json_message)
