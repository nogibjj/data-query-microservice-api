import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import statsmodels.api as sm

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(PROJECT_ROOT)
import helpers

def cleaner(sql_payload, cursor):

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

    connection, cursor = helpers.connect_to_db()

    countries = list()
    cursor.execute(f"select distinct(country) from import.globaltemperaturesbycountry;")
    for row in cursor.fetchall():
        countries.append(row[0])

    connection.close()
    cursor.close()

    return countries

# Question 1: For a given country, what is the trend of their average temperature?
def get_country_plot(country):

    connection, cursor = helpers.connect_to_db()

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
def get_country_year_temp(country, year):

    connection, cursor = helpers.connect_to_db()

    cursor.execute(
        f"SELECT * FROM import.globaltemperaturesbycountry where country = '{country}' and dt like '%{year}%';"
    )
    country_data = cursor.fetchall()
    df_country = cleaner(country_data, cursor)
    max_temp = df_country["averagetemperature"].max()
    min_temp = df_country["averagetemperature"].min()
    mean_temp = df_country["averagetemperature"].mean()

    result = f"In {country}, during {year}, the maximum temperature was {str(max_temp)} and the minimum temperature was {str(min_temp)}."

    connection.close()
    cursor.close()

    return result

# Question 3: For a given year, which city has the highest/lowest temperature on average in a given country?
# TODO: Try just city here so it's not just major cities
def get_city_year_temp(country, year):

    connection, cursor = helpers.connect_to_db()

    cursor.execute(
        f"SELECT * FROM import.globaltemperaturesbymajorcity where country = '{country}' and dt like '%{year}%';"
    )
    country_data = cursor.fetchall()
    df_country = cleaner(country_data, cursor)

    connection.close()
    cursor.close()

    if df_country.empty:
        return "Data does not exist."

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

    connection, cursor = helpers.connect_to_db()

    cursor.execute(
        f"SELECT * FROM import.globaltemperaturesbycountry where country = '{country}';"
    )
    country_data = cursor.fetchall()
    df_country = cleaner(country_data, cursor)
    time_series = df_country.groupby("year")["averagetemperature"].mean().reset_index()

    connection.close()
    cursor.close()

    return time_series.to_json()

def main():

    get_future_temp("Thailand")

if __name__ == "__main__":
    main()
