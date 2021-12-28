import json
import sqlite3

# SQLite DB Name
DB_Name = "Battery_info-DB.db"


# ===============================================================
# Database Manager Class

class DatabaseManager():
    def __init__(self):
        self.conn = sqlite3.connect(DB_Name)
        self.conn.execute('pragma foreign_keys = on')
        self.conn.commit()
        self.cur = self.conn.cursor()

    def add_del_update_db_record(self, sql_query, args=()):
        self.cur.execute(sql_query, args)
        self.conn.commit()
        return

    def __del__(self):
        self.cur.close()
        self.conn.close()


# ===============================================================
# Functions to push Sensor Data into Database

# Function to save Temperature to DB Table
def system_battery_info(jsonData):
    json_Dict = json.loads(jsonData)
    systemID = json_Dict['systemID']
    Data_and_Time = json_Dict['Date']
    Battery_percentage = json_Dict['Battery_percentage']
    Battery_secs_left = json_Dict['Battery_secs_left']
    Power_plugged = json_Dict['Power_plugged']
    cpu_details = json_Dict['cpu_details']
    dbObj = DatabaseManager()
    dbObj.add_del_update_db_record(
        "insert into system_battery_info (systemID, Date_n_Time, Battery_percentage,Battery_secs_left,Power_plugged, cpu_details) values (?,?,?,?,?,?)",
        [systemID, Data_and_Time, Battery_percentage, Battery_secs_left, Power_plugged,cpu_details])
    del dbObj
    print("Inserted Sensor Data into Database.")
    print("")


# ===============================================================
# Master Function to Select DB Funtion based on MQTT Topic

def system_Data_Handler(Topic, jsonData):
    system_battery_info(jsonData)

# ===============================================================
