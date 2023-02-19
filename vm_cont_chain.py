"""EE 250L Lab 04 Starter Code
Run vm_sub.py in a separate terminal on your VM."""

import paho.mqtt.client as mqtt
import time
from datetime import datetime
import socket

"""This function (or "callback") will be executed when this client receives 
a connection acknowledgement packet response from the server. """
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    #new, made by me
    client.subscribe("msbraga/pong")
    client.message_callback_add("msbraga/pong", on_message_from_pong)

#new, made by me
def on_message(client, userdata, msg):
    print("Default callback - topic: " + msg.topic + "   msg: " + str(msg.payload, "utf-8"))
def on_message_from_pong(client, userdata, message):
   n=int(message.payload.decode())
   n=n+1
   client.publish("msbraga/ping", n)
   print(n)
   time.sleep(1)


if __name__ == '__main__':
    #get IP address

    n=0 
    """your code here"""
    

    
    
    #create a client object
    client = mqtt.Client()
    
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect
    
    #new, made by me
    client.on_message = on_message
    """Connect using the following hostname, port, and keepalive interval (in 
    seconds). We added "host=", "port=", and "keepalive=" for illustrative 
    purposes. You can omit this in python. For example:
    
    `client.connect("eclipse.usc.edu", 11000, 60)` 
    
    The keepalive interval indicates when to send keepalive packets to the 
    server in the event no messages have been published from or sent to this 
    client. If the connection request is successful, the callback attached to
    `client.on_connect` will be called."""

    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)

    """ask paho-mqtt to spawn a separate thread to handle
    incoming and outgoing mqtt messages."""
    client.loop_start()
    client.publish("msbraga/ping", n)
    print(n)
    time.sleep(1)

    while True:
    	pass 
    
    
    
    
    
 
