#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
"""
A small example subscriber
"""
import paho.mqtt.client as paho

def on_message(mosq, obj, msg):
    print "%16s %s" % (msg.topic, msg.payload)

def on_publish(mosq, obj, mid):
     pass

if __name__ == '__main__':
    client = paho.Client()
    client.on_message = on_message
   # client.on_publish = on_publish

#client.tls_set('root.ca', certfile='c1.crt', keyfile='c1.key')
    client.connect("127.0.0.1", 1883, 60)

    client.subscribe("Items")
    client.subscribe("USER CPU used")
    client.subscribe("SYSTEM CPU used")
    client.subscribe("SOFTIRQ CPU used")
    client.subscribe("RAM used")
    client.subscribe("HOME DISK used")

    while client.loop() == 0:
        pass

# vi: set fileencoding=utf-8 :
