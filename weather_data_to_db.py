import requests
import json
import pandas as pd
import sqlite3
import datetime
from connect_to_weatherinfo import create_connection

stadt = "Alsdorf"
land = "Germany"
api_key = '1f376d57a9f8db239af30093b382b340'
db_path = "weatherinfo.db"

df = pd.read_json("data.json", orient='index')
dfc = df.iat[4, 0]
dfl = pd.json_normalize(dfc)
dfl.rename(columns={'id': 'city_id', 'name': 'city_name', "coord.lat": "coord_lat", "coord.lon": "coord_lon"},
           inplace=True)
dfl["create_date"] = datetime.datetime.now()
# print(dfl)
conn = sqlite3.connect(db_path)

dfl.to_sql("weather_request", conn, if_exists='replace', index=False)
pd.read_sql('select * from weather_request', conn)


