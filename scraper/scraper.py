from datetime import datetime, timezone
from db_tools import connect_to_db, create_table, load_data
from sqlalchemy import Column, Float, MetaData, Table, Text, TIMESTAMP
import os
import requests
import time

locations = [
    {"lat":25.8600,"lon":-97.4200},
    {"lat":25.9000,"lon":-97.5200},
    {"lat":25.9000,"lon":-97.4800},
    {"lat":25.9000,"lon":-97.4400},
    {"lat":25.9000,"lon":-97.4000},
    {"lat":25.9200,"lon":-97.3800},
    {"lat":25.9400,"lon":-97.5400},
    {"lat":25.9400,"lon":-97.5200},
    {"lat":25.9400,"lon":-97.4800},
    {"lat":25.9400,"lon":-97.4400}
]

meta = MetaData()
table = Table(
    'weather', meta,
    Column('time', TIMESTAMP, primary_key=True, comment="The timestamp that these metrics refer to"),
    Column('snapshot_time', TIMESTAMP, primary_key=True, comment="The timestamp when these metrics were pulled"),
    Column('lat', Float, primary_key=True, comment="Location latitude (in degrees)"),
    Column('lon', Float, primary_key=True, comment="Location longitude (in degrees)"),
    Column('temperature', Float, comment="Temperature in degrees Fahrenheit"),
    Column('wind_speed', Float, comment="Wind speed in miles per hour"),
    Column('metric_type', Text, primary_key=True, comment="Whether these metrics are forecasts or actual historical")
)

API_KEY = os.environ['API_KEY']

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
    current_time = datetime.now(timezone.utc)

    for location in locations:
        params["location"] = f"{location['lat']},{location['lon']}"

        endpoint = metric_types[m] + API_KEY + "&timesteps=" \
                   + params["timesteps"] + "&location=" + params["location"] \
                   + "&units=" + params["units"]
        
        response = requests.get(endpoint, headers=headers)
        data = response.json()
        output_columns = ["lat", "lon", "metric_type", "wind_speed",
                          "temperature", "time", "snapshot_time"]
        
        for row in data["timelines"]["hourly"]:
            row["values"]["metric_type"] = m
            row["values"]["lat"] = location["lat"]
            row["values"]["lon"] = location["lon"]
            row["values"]["time"] = row["time"]
            row["values"]["wind_speed"] = row["values"]["windSpeed"]
            row["values"]["wind_speed"] = row["values"]["windSpeed"]
            row["values"]["snapshot_time"] = current_time

            row_clean = {}
            for c in output_columns:
                row_clean[c] = row["values"][c]
            output.append(row_clean)

        time.sleep(1) # to comply with the API rate limit

    return output


def get_all_data():
    output = []
    for m in metric_types:
        output_subset = fetch_data_by_type(m)
        output.extend(output_subset)

    return output


if __name__ == "__main__":
    output = get_all_data()
    
    # Connect to database
    engine = connect_to_db()

    create_table(engine, table)
    load_data(engine, table, output)