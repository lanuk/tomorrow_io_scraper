from dotenv import load_dotenv
import os
import pandas as pd
import requests

locations = [
    {"lat":25.8600,"lon":-97.4200},
    # {"lat":25.9000,"lon":-97.5200},
    # {"lat":25.9000,"lon":-97.4800},
    # {"lat":25.9000,"lon":-97.4400},
    # {"lat":25.9000,"lon":-97.4000},
    # {"lat":25.9200,"lon":-97.3800},
    # {"lat":25.9400,"lon":-97.5400},
    # {"lat":25.9400,"lon":-97.5200},
    # {"lat":25.9400,"lon":-97.4800},
    # {"lat":25.9400,"lon":-97.4400}
]

load_dotenv()
TOMORROW_IO_API_KEY = os.getenv('TOMORROW_IO_API_KEY')

metric_types = {
    "historical": "https://api.tomorrow.io/v4/weather/history/recent?apikey=",
    "forecast": "https://api.tomorrow.io/v4/weather/forecast?apikey="
}

params = {
    "timesteps": "1h",
    "units": "imperial"
}

headers = {
    "accept": "application/json",
}

def fetch_data_by_type(m):
    output = []
    for location in locations:
        params["location"] = f"{location['lat']},{location['lon']}"

        endpoint = metric_types[m] + TOMORROW_IO_API_KEY + "&timesteps=" \
                   + params["timesteps"] + "&location=" + params["location"] \
                   + "&units=" + params["units"]
        
        response = requests.get(endpoint, headers=headers)
        data = response.json()

        for row in data["timelines"]["hourly"]:
            row["metric_type"] = m
            row["lat"] = location["lat"]
            row["lon"] = location["lon"]
            output.append(row)

    return output


def get_all_data():
    output = []
    for m in metric_types:
        output_subset = fetch_data_by_type(m)
        output.append(output_subset)

    return output


if __name__ == "__main__":
    output = get_all_data()