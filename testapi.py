import requests
import json

api_key = "1f376d57a9f8db239af30093b382b340"
stadt = "Aachen"
land = "Germany"

url = f'https://api.openweathermap.org/data/2.5/forecast?q={stadt},{land}&appid={api_key}&units=metric' \
      f'&lang=de'
response = requests.get(url)
"""
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={api_key}&units=metric&lang=de'
response = requests.get(url)
"""
data = json.loads(response.text)

