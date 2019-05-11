import paho.mqtt.client as paho
import time


 
client = paho.Client()
client.connect("broker.hivemq.com", 1883)
client.loop_start()
 
while True:
    (rc,mid)=client.publish("sirmvit/python", "Hi from ravi")
    print(rc,mid)
    time.sleep(1)
