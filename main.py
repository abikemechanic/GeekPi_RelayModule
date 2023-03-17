from GeekPI_relay_module import RelayBoard
from mqtt.MQTTClient import MQTTClient

import time
import json


def on_mqtt_message(client, userdata, message):
    print(message.payload.decode('utf-8'))

def load_configuration():
    with open('relay_config.json') as json_config:
        config = json.load(json_config)

        for r in config['relays']:
            print(f'relay id: {r["name"]}, topic: {r["subscribe_topic"]}')


relayBoard = RelayBoard()
mqttClient = MQTTClient(8888, '192.168.1.13')
mqttClient.client.on_message = on_mqtt_message

for r in relayBoard.relay_list:
    relayBoard.turn_on(r)
    time.sleep(1)

for r in relayBoard.relay_list:
    relayBoard.turn_off(r)


if __name__ == '__main__':
    load_configuration()