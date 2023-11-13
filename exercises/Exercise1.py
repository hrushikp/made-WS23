import pandas as pd
from sqlalchemy import String, TEXT, INTEGER, Float, DECIMAL

data = pd.read_csv('https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit')
print(df)
columnTypes = {'column_1': INTEGER, 'column_2': String, 'column_3': String, 'column_4': String, 'column_5': String,
               'column_6': String, 'column_7': Float,'column_8': Float, 'column_9': INTEGER, 'column_10': Float,
               'column_11':TEXT,'column_12': String, 'geo_punkt': DECIMAL}

data.to_sql('airports','sqlite:///airports.sqlite', if_exists='replace', index=False)

#after running the oode, the output file will be generate with name "airports.sqlite".
