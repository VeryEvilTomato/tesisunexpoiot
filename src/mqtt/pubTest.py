import paho.mqtt.client as mqtt
import time, json, random

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print ("Connected")

def on_publish(client, obj, mid):
    print("mid: " + str(mid))

msg = 20

client = mqtt.Client("Samuel", protocol=mqtt.MQTTv31)
client.on_connect=on_connect
client.on_publish=on_publish
client.username_pw_set("device", password="deviceiot")
client.connect("127.0.0.1", 1883, 60)
client.publish(topic="Samuel/monitors/Temperatura_garaje", payload=msg, qos=1)