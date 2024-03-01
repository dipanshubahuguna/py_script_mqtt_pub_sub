# python 3.6

import random
import time

from paho.mqtt import client as mqtt_client


broker = 'broker.emqx.io'
port = 1883
topic = "python/mqtt"
# Generate a Client ID with the publish prefix.
client_id = "132"

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




def publish(client):
    msg_count = 0
    # callback function which will be triggered 
    def on_publish(client,userdata,flags):
        print(f"Messsage is published with msg_count : {msg_count}")
    while True:
        time.sleep(1)
        msg = f"message number: {msg_count}"
        client.publish(topic,msg)
        client.on_publish = on_publish
        msg_count+=1
        if msg_count > 5:
            break


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)
    client.loop_stop()


if __name__ == '__main__':
    run()

