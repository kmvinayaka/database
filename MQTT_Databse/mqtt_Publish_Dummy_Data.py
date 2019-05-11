import paho.mqtt.client as mqtt
import random, threading, json
from datetime import datetime


#====================================================
# MQTT Settings 
MQTT_Broker = "broker.hivemq.com"
MQTT_Port = 1883
Keep_Alive_Interval = 45

Mqtt="BTM/sensordata"

#====================================================

def on_connect(client, userdata, rc):
        if rc != 0:
                pass
                print ("Unable to connect to MQTT Broker...")
        else:
                print ("Connected with MQTT Broker: " + str(MQTT_Broker))

def on_publish(client, userdata, mid):
        pass
                
def on_disconnect(client, userdata, rc):
        if rc !=0:
                pass
                
mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_publish = on_publish
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))            

                
def publish_To_Topic(topic, message):
        mqttc.publish(topic,message)
        print ("Published: " + str(message) + " " + "on MQTT Topic: " + str(topic))
        print ("")


#====================================================
# FAKE SENSOR 
# Dummy code used as Fake Sensor to publish some random values
# to MQTT Broker

toggle = 0

def publish_Fake_Sensor_Values_to_MQTT():
        threading.Timer(3.0, publish_Fake_Sensor_Values_to_MQTT).start()
        Temperature_Fake_Value = float("{0:.2f}".format(random.uniform(1, 30)))
        Humidity_Fake_Value = float("{0:.2f}".format(random.uniform(50, 100)))
        sensordata = {}
        sensordata['Sensor_ID'] = "DHT11"
        sensordata['Date'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
        sensordata['Temperature'] = Temperature_Fake_Value
        sensordata['Humidity'] = Humidity_Fake_Value                                                                                
        temperature_json_data = json.dumps(sensordata)                                                                        
        print( "Publishing fake Temperature Value: " + str(sensordata) + "...")
        publish_To_Topic (Mqtt, temperature_json_data)                                                                        
        toggle = 0
                                                                                


publish_Fake_Sensor_Values_to_MQTT()

#====================================================
