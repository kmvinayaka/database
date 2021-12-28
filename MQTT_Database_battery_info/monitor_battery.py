import os
import time
import sys
import json
import psutil
import paho.mqtt.client as paho
from datetime import datetime
payload = {}

next_reading = time.time() 

INTERVAL=2
client = paho.Client()
client.connect("broker.hivemq.com", 1883)
client.loop_start()

try:
    while True:
        
        battery = psutil.sensors_battery()
        cpu_details = psutil.cpu_freq()
        payload["systemID"] = "dell_laptop"
        payload['Date'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
        payload["Battery_percentage"] = battery.percent
        payload["Battery_secs_left"] = battery.secsleft if str(battery.secsleft).isdigit() else "Charging"
        payload["Power_plugged"] = str(battery.power_plugged)
        payload["cpu_details"]= cpu_details.current
        payload["cpu_max"] = cpu_details.max
        payload["cpu_min"] = cpu_details.min
        print(payload)
        (rc,mid)=client.publish("python/sensordata/IoT", json.dumps(payload))
        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
except KeyboardInterrupt:
    pass


