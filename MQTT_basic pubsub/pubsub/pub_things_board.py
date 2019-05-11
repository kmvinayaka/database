import paho.mqtt.client as paho
import time
import json
import random 

def on_connect(client, userdata, rc):
    pass
 
def on_publish(client, userdata, mid):
    pass
   
 
ACCESS_TOKEN = 'IsSe66xxYI9CUjsMZt7X'


 
client = paho.Client()
client.on_publish = on_publish
client.username_pw_set(ACCESS_TOKEN)
client.connect("demo.thingsboard.io", 1883)
client.loop_start()
attri={'temp':"",'Hum':''}
while True:    
    t=round(random.uniform(20,40),2)
    h=round(random.uniform(40,80),2)
    attri['temp']=t
    attri['Hum']=h
    json.dumps(attri)
    (rc, mid) = client.publish("v1/devices/me/telemetry", json.dumps(attri), qos=1)
    print (json.dumps(attri))
    print (mid)
    time.sleep(2)
