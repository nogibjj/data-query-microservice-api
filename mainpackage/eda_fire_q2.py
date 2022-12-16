import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(PROJECT_ROOT)
import helpers2

# Question 5: Global temperatures last decade from the max date of reporting  (2015-09-01)
def global_temperatures_decade():

    connection, cursor = helpers2.connect_to_db()

    cursor.execute(
        "SELECT *,(date_part('year','2015-12-01'::date)-date_part('year',dt::date)) as lastdecade FROM import.globaltemperatures where (date_part('year','2015-12-01'::date)-date_part('year',dt::date))<=10;"
    )
    df = pd.DataFrame(cursor.fetchall(), columns=[x[0] for x in cursor.description])
    df["landaveragetemperature"] = df["landaveragetemperature"].astype(float)
    df["dt"] = pd.to_datetime(df["dt"])
    df["movingaverage"] = df["landaveragetemperature"].rolling(window=1).mean()

    cursor.close()
    connection.close()

    return df.to_json()


# Question 6: Global temperatures in the last century -  (2015-09-01) is the maximum year..
def global_temperatures_century():

    connection, cursor = helpers2.connect_to_db()

    cursor.execute(
        "SELECT * FROM import.globaltemperatures where (date_part('year','2015-12-01'::date)-date_part('year',dt::date))<=100;"
    )
    df = pd.DataFrame(cursor.fetchall(), columns=[x[0] for x in cursor.description])
    df["landaveragetemperature"] = df["landaveragetemperature"].astype(float)
    df["dt"] = pd.to_datetime(df["dt"])
    data_frame = df.groupby(df["dt"].dt.year).mean()

    cursor.close()
    connection.close()

    return data_frame.to_json()


# Question 7: create a chart for each season color coded by country and tooltip for year and temperature
def get_temperatures_top5():

    connection, cursor = helpers2.connect_to_db()

    cursor.execute(
        # temperatures by the top 5 and least polluters countries in the last century: Higest pollutors = United States, China, Russia, India, Japan and least polluters = Cape Verde, Grenada, Puerto Rico
        "SELECT * FROM import.globaltemperaturesbycountry where (date_part('year','2015-12-01'::date)-date_part('year',dt::date))<=100 and country in ('United States','China','Russia','India','Japan');"
    )

    df = pd.DataFrame(cursor.fetchall(), columns=[x[0] for x in cursor.description])
    top5 = df.copy()
    top5["dt"] = pd.to_datetime(top5["dt"])
    top5["averagetemperature"] = top5["averagetemperature"].replace("", np.nan)
    top5["averagetemperature"] = top5["averagetemperature"].astype(float)
    top5["movingaverage"] = top5["averagetemperature"].rolling(window=3).mean()

    top5["year"] = top5["dt"].dt.year
    top_collapsed = top5.groupby(["year", "season", "country"]).mean().reset_index()

    winter = top_collapsed[top_collapsed["season"] == "winter"]
    spring = top_collapsed[top_collapsed["season"] == "spring"]
    summer = top_collapsed[top_collapsed["season"] == "summer"]
    autumn = top_collapsed[top_collapsed["season"] == "autumn"]

    seasons_df_list = [
        winter.to_json(),
        spring.to_json(),
        summer.to_json(),
        autumn.to_json(),
    ]

    cursor.execute(
        # temperatures by the top 5 and least polluters countries in the last century: Higest pollutors = United States, China, Russia, India, Japan and least polluters = Cape Verde, Grenada, Puerto Rico
        "SELECT * FROM import.globaltemperaturesbycountry where (date_part('year','2015-12-01'::date)-date_part('year',dt::date))<=100 and country in ('Cape Verde','Grenada','Puerto Rico');"
    )

    df_2 = pd.DataFrame(cursor.fetchall(), columns=[x[0] for x in cursor.description])
    bottom5 = df_2.copy()
    bottom5["dt"] = pd.to_datetime(bottom5["dt"])
    bottom5["averagetemperature"] = bottom5["averagetemperature"].replace("", np.nan)
    bottom5["averagetemperature"] = bottom5["averagetemperature"].astype(float)
    bottom5["movingaverage"] = bottom5["averagetemperature"].rolling(window=3).mean()

    bottom5["year"] = bottom5["dt"].dt.year
    bottom_collapsed = (
        bottom5.groupby(["year", "season", "country"]).mean().reset_index()
    )

    winter_2 = bottom_collapsed[bottom_collapsed["season"] == "winter"]
    spring_2 = bottom_collapsed[bottom_collapsed["season"] == "spring"]
    summer_2 = bottom_collapsed[bottom_collapsed["season"] == "summer"]
    autumn_2 = bottom_collapsed[bottom_collapsed["season"] == "autumn"]

    seasons_df_list = seasons_df_list + [
        winter_2.to_json(),
        spring_2.to_json(),
        summer_2.to_json(),
        autumn_2.to_json(),
    ]

    cursor.close()
    connection.close()

    # return dataframe
    return seasons_df_list
