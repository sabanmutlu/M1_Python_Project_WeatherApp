import requests
import json
import pandas as pd
import sqlite3

stadt = "Alsdorf"
land = "Germany"
api_key = '1f376d57a9f8db239af30093b382b340'

df = pd.read_json("data.json", orient='index')
df.iat[2, 0]