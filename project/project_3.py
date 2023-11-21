import requests
import pandas as pd
from io import StringIO
import sqlite3
import os

monthly_air_traffic_figures = "https://opendata.muenchen.de/dataset/9a648dad-0b55-42c7-8ba6-24b7c6bcc599/resource/ad408efa-528e-409b-bfe2-e1f547992cde/download/monatszahlen2307_flugverkehr_10_07_23_nosum.csv"
monthly_weather_figures = "https://opendata.muenchen.de/dataset/d7e42935-8884-40d3-9284-096d9cafecdd/resource/64c8c183-7fd0-4b29-9958-4169d22ee883/download/monatszahlen2307_witterung_10_07_23_nosum.csv"

air_response = requests.get(monthly_air_traffic_figures)
weather_response= requests.get(monthly_weather_figures)

air_data = air_response.text
weather_data = weather_response.text

air_df = pd.read_csv(StringIO(air_data))
air_df = air_df.fillna(0) 

weather_df = pd.read_csv(StringIO(weather_data))
weather_df = weather_df.fillna(0) 

data_dir = '/data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Set database path 
db_path = os.path.join(data_dir, 'my_database.db')

conn = sqlite3.connect(db_path)
air_df.to_sql('air_table', conn, if_exists='replace', index=False)
weather_df.to_sql('weather_table', conn, if_exists='replace', index=False)
conn.close()

print("Data pipeline complete!")