# import requests
# import json
import sqlite3
from sqlite3 import Error

import pandas as pd
import datetime


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def create_tables(conn):
    sql_create_weather_request_table = """ CREATE TABLE IF NOT EXISTS weather_request (
        id integer PRIMARY KEY AUTOINCREMENT,
        create_date DATETIME,
        city_id	INTEGER,
        city_name TEXT,
        country TEXT,
        population INTEGER,
        timezone INTEGER,
        sunrise INTEGER,
        sunset INTEGER,
        coord_lat REAL,
        coord_lon REAL
                                    ); """
    # create tables
    try:
        cur = conn.cursor()
        cur.execute(sql_create_weather_request_table)
    except Error as e:
        print(e)


def mk_weather_request():
    # stadt = "Alsdorf"
    # land = "Germany"
    # api_key = '1f376d57a9f8db239af30093b382b340'
    df = pd.read_json("data.json", orient='index')
    data_city = df.iat[4, 0]
    df_wr = pd.json_normalize(data_city)
    df_wr.rename(columns={"id": "city_id", "name": "city_name", "coord.lat": "coord_lat",
                          "coord.lon": "coord_lon"}, inplace=True)
    df_wr["create_date"] = datetime.datetime.now()
    return df_wr


def wf_to_sqlite():
    # Prepare table
    df_wr = mk_weather_request()

    # Connect database
    db_path = "weatherinfo.db"
    conn = create_connection(db_path)

    with conn:
        # Create table weather_request
        create_tables(conn)
        df_wr.to_sql("weather_request", conn, if_exists='append', index=False)
        see_table = pd.read_sql('select * from weather_request', conn)
        print(see_table)


if __name__ == '__main__':
    wf_to_sqlite()
