from dotenv import load_dotenv
import os
import pandas as pd
import requests

locations = [
    {"lat":25.8600,"long":-97.4200},
    # {"lat":25.9000,"long":-97.5200},
    # {"lat":25.9000,"long":-97.4800},
    # {"lat":25.9000,"long":-97.4400},
    # {"lat":25.9000,"long":-97.4000},
    # {"lat":25.9200,"long":-97.3800},
    # {"lat":25.9400,"long":-97.5400},
    # {"lat":25.9400,"long":-97.5200},
    # {"lat":25.9400,"long":-97.4800},
    # {"lat":25.9400,"long":-97.4400}
]

load_dotenv()
TOMORROW_IO_API_KEY = os.getenv('TOMORROW_IO_API_KEY')

historical_endpoint = "https://api.tomorrow.io/v4/historical?apikey=" \
                      + TOMORROW_IO_API_KEY
forecast_endpoint = "https://api.tomorrow.io/v4/weather/forecast?apikey=" \
                    + TOMORROW_IO_API_KEY

def fetch_historical_data():
    params = {
        "units": "imperial",
        "timesteps": ["1h"],
        "fields": ["temperature"],
        "startTime": "nowMinus5d",
        "endTime": "now",
    }

    headers = {
        "accept": "application/json",
        "Accept-Encoding": "gzip",
        "content-type": "application/json"
    }

    for location in locations:
        params["location"] = f"{location['lat']},{location['long']}"

        response = requests.post(historical_endpoint, json=params, headers=headers)
        print(response.text)


def fetch_forecast_data():
    params = {
        "timesteps": "1h",
        "units": "imperial",
    }

    headers = {
        "accept": "application/json",
    }

    for location in locations:
        params["location"] = f"{location['lat']},{location['long']}"

        endpoint = forecast_endpoint + "&timesteps=" + params["timesteps"] \
                   + "&location=" + params["location"] + "&units=" \
                   + params["units"]
        
        response = requests.get(endpoint, headers=headers)
        data = response.json()
        print(data)
        for row in data:
            print(row)


if __name__ == "__main__":
    # fetch_historical_data()
    fetch_forecast_data()