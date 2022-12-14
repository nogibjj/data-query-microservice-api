import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import statsmodels.api as sm

import helpers2


def cleaner(sql_payload, cursor):

    """Cleaning essential columns for plotting and return statements"""

    df_clean = pd.DataFrame(
        sql_payload, columns=[desc[0] for desc in cursor.description]
    )
    df_clean = df_clean.sort_values(by=["dt"], ascending=True)
    df_clean = df_clean.replace(to_replace="", value=np.nan, regex=True)
    df_clean["season"] = df_clean["season"].fillna("no season assigned by ESEP")
    df_clean = df_clean.dropna()
    df_clean["year"] = df_clean["dt"].str[:4].astype(int)
    df_clean["averagetemperature"] = df_clean["averagetemperature"].astype(float)

    return df_clean


def cleaner_without_season(sql_payload, cursor):

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


def get_countries_list():

    connection, cursor = helpers2.connect_to_db()

    countries = list()
    cursor.execute(f"select distinct(country) from import.globaltemperaturesbycountry;")
    for row in cursor.fetchall():
        countries.append(row[0])

    cursor.close()
    connection.close()

    return countries


country_list = get_countries_list()

# Question 1: For a given country, what is the trend of their average temperature?
def get_country_plot(country):

    if country not in country_list:

        return f"{country} is not in our list of countries found in this dataset. Maybe you mistyped it. These are our available options : {country_list}."

    connection, cursor = helpers2.connect_to_db()

    cursor.execute(
        f"SELECT * FROM import.globaltemperaturesbycountry where country = '{country}';"
    )
    country_data = cursor.fetchall()
    df_country = cleaner(country_data, cursor)
    df_country["temperature"] = df_country.groupby("year")[
        "averagetemperature"
    ].transform("mean")

    df_country_copy = df_country.copy()
    df_country_copy = df_country_copy.drop_duplicates(subset=["year"], keep="first")

    connection.close()
    cursor.close()

    return df_country_copy.to_json()


# Question 2: For a given year and a given country, what is the max/min temperature?
# TODO: If the year is not found it should not give an error
def get_country_year_temp(country, year, test=False):

    if country not in country_list:

        return f"{country} is not in our list of countries found in this dataset. Maybe you mistyped it. These are our available options : {country_list}."

    connection, cursor = helpers2.connect_to_db()

    cursor.execute(
        f"SELECT * FROM import.globaltemperaturesbycountry where country = '{country}' and dt like '%{year}%';"
    )
    country_data = cursor.fetchall()
    df_country = cleaner(country_data, cursor)

    if df_country.empty:

        return "Data does not exist. Try again."

    if test:

        return df_country

    max_temp = df_country["averagetemperature"].max()
    min_temp = df_country["averagetemperature"].min()
    # mean_temp = df_country["averagetemperature"].mean()

    result = f"In {country}, during {year}, the maximum temperature was {str(max_temp)} and the minimum temperature was {str(min_temp)}."

    cursor.close()
    connection.close()

    return result


# Question 3: For a given year, which city has the highest/lowest temperature on average in a given country?
# TODO: Try just city here so it's not just major cities


def get_city_year_temp(country, year, test=False):

    if country not in country_list:

        return f"{country} is not in our list of countries found in this dataset. Maybe you mistyped it. These are our available options : {country_list}."

    connection, cursor = helpers2.connect_to_db()

    cursor.execute(
        f"SELECT * FROM import.globaltemperaturesbymajorcity where country = '{country}' and dt like '%{year}%';"
    )
    country_data = cursor.fetchall()
    df_country = cleaner_without_season(country_data, cursor)

    cursor.close()
    connection.close()

    if df_country.empty:
        return "Data does not exist."

    if test:

        return df_country

    else:
        df_country["temperature"] = df_country.groupby(["year", "city"])[
            "averagetemperature"
        ].transform("mean")
        highest = df_country.sort_values(by=["temperature"], ascending=False).head(1)
        lowest = df_country.sort_values(by=["temperature"], ascending=True).head(1)
        highest_city = highest["city"].values[0]
        lowest_city = lowest["city"].values[0]

        result = f"In {country}, during {year}, the city with the highest recorded temperature was {highest_city}. The city with the lowest recorded temperature was {lowest_city}."

        return result


# Question 4: For a given country, what is the future trend of their average temperature?
def get_future_temp(country):

    if country not in country_list:

        return f"{country} is not in our list of countries found in this dataset. Maybe you mistyped it. These are our available options : {country_list}."

    connection, cursor = helpers2.connect_to_db()

    cursor.execute(
        f"SELECT * FROM import.globaltemperaturesbycountry where country = '{country}';"
    )
    country_data = cursor.fetchall()
    df_country = cleaner(country_data, cursor)

    if df_country.empty:

        return "Data does not exist. Try again."

    time_series = df_country.groupby("year")["averagetemperature"].mean().reset_index()

    cursor.close()
    connection.close()

    return time_series.to_json()


def main():

    get_future_temp("Thailand")


if __name__ == "__main__":
    main()
