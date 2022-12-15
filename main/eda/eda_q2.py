import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(PROJECT_ROOT)
import helpers

cursor = helpers.connect_to_db()

# Question 5: Global temperatures last decade from the max date of reporting  (2015-09-01)
def global_temperatures_decade():
    cursor.execute(
        "SELECT *,(date_part('year','2015-12-01'::date)-date_part('year',dt::date)) as lastdecade FROM import.globaltemperatures where (date_part('year','2015-12-01'::date)-date_part('year',dt::date))<=10;"
    )
    df = pd.DataFrame(cursor.fetchall(), columns=[x[0] for x in cursor.description])
    df['landaveragetemperature'] = df['landaveragetemperature'].astype(float)
    df['dt'] = pd.to_datetime(df['dt'])
    df['movingaverage'] = df['landaveragetemperature'].rolling(window=1).mean()

    return df.to_json()

# Question 6: Global temperatures in the last century -  (2015-09-01) is the maximum year..
def global_temperatures_century():
    cursor.execute(
        "SELECT * FROM import.globaltemperatures where (date_part('year','2015-12-01'::date)-date_part('year',dt::date))<=100;"
    )
    df = pd.DataFrame(cursor.fetchall(), columns=[x[0] for x in cursor.description])
    df['landaveragetemperature'] = df['landaveragetemperature'].astype(float)
    df['dt'] = pd.to_datetime(df['dt'])
    data_frame = df.groupby(df['dt'].dt.year).mean()

    return data_frame.to_json()