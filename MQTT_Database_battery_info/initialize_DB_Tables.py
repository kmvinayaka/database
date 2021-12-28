import sqlite3

# SQLite DB Name
DB_Name =  "Battery_info-DB.db"

# SQLite DB Table Schema
TableSchema="""
drop table if exists system_battery_info ;
create table system_battery_info (
  id integer primary key autoincrement,
  systemID text,
  Date_n_Time text,
  Battery_percentage int,
  Battery_secs_left int,
  Power_plugged text,
  cpu_details real
);"""

#Connect or Create DB File
conn = sqlite3.connect(DB_Name)
curs = conn.cursor()

#Create Tables
sqlite3.complete_statement(TableSchema)

print(curs.executescript(TableSchema))

#Close DB
curs.close()
conn.close()
