import requests
import pandas as pd
from io import StringIO
import sqlite3
import os

electronic_sales = "https://www.techgig.com/files/contest_upload_files/electronics.csv"

item_id = requests.get(electronic_sales)
product_count = requests.get(electronic_sales)

product_count_df = pd.read_csv(StringIO(product_count))
product_count = product_count_df.fillna(0) 


item_id = pd.read_csv(StringIO(item_id))
item_id = item_id_df.fillna(0) 



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
