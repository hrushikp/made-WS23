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



root_dir = os.path.abspath('.')


data_dir = os.path.join(root_dir, 'data')
db_path = os.path.join(data_dir, 'my_database.db')



conn = sqlite3.connect(db_path)
air_df.to_sql('air_table', conn, if_exists='replace', index=False)
weather_df.to_sql('weather_table', conn, if_exists='replace', index=False)
conn.close()

conn = sqlite3.connect(db_path)
cursor = conn.cursor()


cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
table_names = cursor.fetchall()
table_names = [name[0] for name in table_names]


print("Tables (datasets) in the database:")
for table_name in table_names:
    print(table_name)


conn.close()

print("Data pipeline complete! and dataets are succesfully stored in tyhe database")