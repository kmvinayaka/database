
import paho.mqtt.client as mqtt
from store_Sensor_Data_to_DB import system_Data_Handler



# MQTT Settings 
MQTT_Broker = "broker.hivemq.com"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic = "python/sensordata/ravi"

#Subscribe to all Sensors at Base Topic
def on_connect(client,userdata,flags,rc):
	print(mqttc.subscribe(MQTT_Topic, 0))

#Save Data into DB Table
def on_message(mqttc,userdata,msg):
	# This is the Master Call for saving MQTT Data into DB
	# For details of "sensor_Data_Handler" function please refer "sensor_data_to_db.py"
	print( "MQTT Data Received...")
	print( "MQTT Topic: " + msg.topic)
	print ("Data: " + str(msg.payload))
	system_Data_Handler(msg.topic, msg.payload)
	

def on_subscribe(mosq, obj, mid, granted_qos):
    pass

mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Connect
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))

# Continue the network loop
mqttc.loop_forever()
