import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    """
    finally:
        if conn:
            conn.close()
    """
    return conn


def create_tables():
    sql_create_weather_request_table = """
        CREATE TABLE IF NOT EXISTS weather_request ( 
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

    # create a database connection
    conn = None
    cur = None
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        print(sqlite3.version)
    except Error as e:
        print(e)

    # create tables
    if conn is not None:
        # create weather_request table
        cur.execute(sql_create_weather_request_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    db_path = "weatherinfo.db"
    create_tables()
