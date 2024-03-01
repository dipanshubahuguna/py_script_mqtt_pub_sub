# python3.6

import random

from paho.mqtt import client as mqtt_client
import time

# open broker
broker = 'broker.emqx.io'
port = 1883
topic = "python/mqtt"
client_id = "123"


# callback function that will be triggered once any acknowledgement is received after client and broker connection.
def res_after_ack(client,userdata,flags,reason_code):
    if reason_code == 0:
        print("Connected to MQTT broker")
        # Subscribe to a topic once connected
        # client.subscribe("example/topic")
    else:
        print(f"Connection failed with result code {reason_code}")
    

def connect_mqtt():
    # creating client instance
    client = mqtt_client.Client(client_id) 
    # will be called after any ACK is received after client and broker connection
    client.on_connect = res_after_ack
    # connecting client with broker
    client.connect(broker, port)
    return client



# subscribe to a particular topic 
def subscribe(client: mqtt_client):
    # callback function for printing message after subscribing to a topic 
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
    client.subscribe(topic)
    client.on_message = on_message

# main function 
def run():
    client = connect_mqtt()
    subscribe(client)
    # start the loop to handle communication with broker continuously
    client.loop_forever()


if __name__ == '__main__':
    run()
