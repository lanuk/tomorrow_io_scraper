from dotenv import load_dotenv
import os
import pandas as pd
import requests

locations = [
	{"lat":25.8600,"long":-97.4200},
	{"lat":25.9000,"long":-97.5200},
	{"lat":25.9000,"long":-97.4800},
	{"lat":25.9000,"long":-97.4400},
	{"lat":25.9000,"long":-97.4000},
	{"lat":25.9200,"long":-97.3800},
	{"lat":25.9400,"long":-97.5400},
	{"lat":25.9400,"long":-97.5200},
	{"lat":25.9400,"long":-97.4800},
	{"lat":25.9400,"long":-97.4400}
]

historical_endpoint = "https://api.tomorrow.io/v4/historical"
forecast_endpoint = "https://api.tomorrow.io/v4/weather/forecast"

load_dotenv()
TOMORROW_IO_API_KEY = os.getenv('TOMORROW_IO_API_KEY')

def fetch_weather_data():
	for location in locations:
		params = {
			"location": f"{location['lat']},{location['long']}",
			"units": "imperial",
			"timesteps": "1h",
			"fields": "temperature",

		}
		historical_response = requests.get(historical_endpoint, params=params)
		data = historical_response.json()
		print(data)


if __name__ == "__main__":
	fetch_weather_data()