import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(PROJECT_ROOT)
import helpers

cursor = helpers.connect_to_db()


def cleaner(sql_payload):

    """Cleaning essential columns for plotting and return statements"""

    df_clean = pd.DataFrame(
        sql_payload, columns=[desc[0] for desc in cursor.description]
    )
    df_clean = df_clean.sort_values(by=["dt"], ascending=True)
    df_clean = df_clean.replace(to_replace="", value=np.nan, regex=True)
    df_clean = df_clean.dropna()
    df_clean["year"] = df_clean["dt"].str[:4].astype(int)
    df_clean["averagetemperature"] = df_clean["averagetemperature"].astype(float)

    return df_clean


# Question 1: For a given country, what is the trend of their average temperature?
def get_country_plot(country):

    cursor.execute(
        f"SELECT * FROM import.globaltemperaturesbycountry where country = '{country}';"
    )
    country_data = cursor.fetchall()
    df_country = cleaner(country_data)
    df_country["temperature"] = df_country.groupby("year")[
        "averagetemperature"
    ].transform("mean")

    return df_country.drop_duplicates(subset=["year"], keep="first").plot(
        x="year",
        y="temperature",
        kind="line",
        title="Average Temperature of " + country + " (by year)",
    )


# Question 2: For a given year and a given country, what is the max/min temperature?
# TODO: Do the max and min in sql
def get_country_year_temp(country, year):
    cursor.execute(
        f"SELECT * FROM import.globaltemperaturesbycountry where country = '{country}' and dt like '%{year}%';"
    )
    country_data = cursor.fetchall()
    df_country = cleaner(country_data)
    max_temp = df_country["averagetemperature"].max()
    min_temp = df_country["averagetemperature"].min()
    mean_temp = df_country["averagetemperature"].mean()
    return max_temp, min_temp, mean_temp


# Question 3: For a given year, which city has the highest/lowest temperature on average in a given country?
# TODO: Try the groupby in sql
def get_city_year_temp(country, year):
    cursor.execute(
        f"SELECT city FROM import.globaltemperaturesbymajorcity where country = '{country}' and dt like '%{year}%';"
    )
    country_data = cursor.fetchall()
    df_country = cleaner(country_data)
    df_country["temperature"] = df_country.groupby(["year", "city"])[
        "averagetemperature"
    ].transform("mean")
    highest = df_country.sort_values(by=["temperature"], ascending=False).head(1)
    lowest = df_country.sort_values(by=["temperature"], ascending=True).head(1)
    highest_city = highest["city"].values[0]
    lowest_city = lowest["city"].values[0]
    return highest_city, lowest_city


# Question 4: For a given country, what is the initial and the most recent temperature?
# TODO: Get the first date and last date in sql
def get_init_temp(country):
    cursor.execute(
        f"SELECT * FROM import.globaltemperaturesbycountry where country = '{country}';"
    )
    country_data = cursor.fetchall()
    df_country = pd.DataFrame(
        country_data, columns=[desc[0] for desc in cursor.description]
    )
    df_country = df_country.sort_values(by=["dt"], ascending=True)
    df_country = df_country.replace(to_replace="", value=np.nan, regex=True)
    df_country = df_country.dropna()
    df_country["year"] = df_country["dt"].str[:4].astype(int)
    df_country["month"] = df_country["dt"].str[5:7].astype(int)
    df_country["averagetemperature"] = df_country["averagetemperature"].astype(float)
    initial = str(df_country.loc[0, "averagetemperature"])
    initial_month = (
        str(df_country.loc[0, "year"]) + "-" + str(df_country.loc[0, "month"])
    )
    recent = str(df_country.iloc[-1]["averagetemperature"])
    recent_month = (
        str(df_country.iloc[-1]["year"]) + "-" + str(df_country.iloc[-1]["month"])
    )

    resp = f"The temperature on {initial_month} was {initial} and on {recent_month} was {recent}."

    return resp


def main():

    # get_country_plot("Europe")
    temps = get_init_temp("Afghanistan")
    print(temps)


if __name__ == "__main__":
    main()
