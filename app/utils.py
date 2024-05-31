import requests
from flask import current_app

def fetch_weather_data(cidade):
    api_key = current_app.config['OPENWEATHERMAP_API_KEY']
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={cidade}&appid={api_key}"

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None