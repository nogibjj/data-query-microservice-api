import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import statsmodels.api as sm

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(PROJECT_ROOT)
import helpers

cursor = helpers.connect_to_db()


def cleaner(df_to_clean):

    """Cleaning essential columns for plotting and return statements"""
    df_clean = df_to_clean
    df_clean = df_clean.sort_values(by=["dt"], ascending=True)
    df_clean = df_clean.replace(to_replace="", value=np.nan, regex=True)
    df_clean = df_clean.dropna()
    df_clean["year"] = df_clean["dt"].str[:4].astype(int)
    df_clean["averagetemperature"] = df_clean["averagetemperature"].astype(float)
    df_clean["month"] = df_clean["dt"].str[5:7].astype(int)

    return df_clean


# def get_countries_list():

#     countries = list()
#     cursor.execute(f"select distinct(country) from import.globaltemperaturesbycountry;")
#     for row in cursor.fetchall():
#         countries.append(row[0])

#     return countries


def options(which="both"):

    cursor.execute(f"SELECT country, year FROM import.globaltemperaturesbycountry;")

    country_data = cursor.fetchall()

    df_country = pd.DataFrame(
        country_data, columns=[desc[0] for desc in cursor.description]
    )

    df_country = cleaner(df_country)

    if which == "year":

        year_list = [i for i in df_country["year"].unique()]

        return year_list

    elif which == "country":

        country_list = [i for i in df_country["country"].unique()]

        return country_list

    elif which == "both":

        country_list = [i for i in df_country["country"].unique()]

        year_list = [i for i in df_country["year"].unique()]

        return country_list, year_list


countries, years = options()

# Question 1: For a given country, what is the trend of their average temperature?
def get_country_plot(country, validator=countries, test=False):

    # Error Handling
    if country not in validator:

        return f"Your country, {country}, is not listed in the options, please choose one from : {countries}."

    cursor.execute(
        f"SELECT * FROM import.globaltemperaturesbycountry where country = '{country}';"
    )

    # cursor.execute(
    #     f"SELECT * FROM import.globaltemperaturesbycountry where country = '{country}';"
    # )

    country_data = cursor.fetchall()
    df_country = pd.DataFrame(
        country_data, columns=[desc[0] for desc in cursor.description]
    )
    df_country = cleaner(df_country)
    df_country["temperature"] = df_country.groupby("year")[
        "averagetemperature"
    ].transform("mean")

    if test:

        return df_country

    return df_country.drop_duplicates(subset=["year"], keep="first").plot(
        x="year",
        y="temperature",
        kind="line",
        title="Average Temperature of " + country + " (by year)",
    )

    # df_country_copy = df_country.copy()
    # df_country_copy = df_country_copy.drop_duplicates(subset=["year"], keep="first")

    # return df_country_copy.to_json()


# Question 2: For a given year and a given country, what is the max/min temperature?
# TODO: Do the max and min in sql
# TODO: If the year is not found it should not give an error


def get_country_year_temp(country, year, validator=[countries, years], test=False):

    if country not in validator[0]:

        return f"Your country, {country}, is not listed in the options, please choose one from : {countries}."

    if year not in validator[1]:

        return f"Your country, {year}, is not listed in the options, please choose one from : {years}."

    cursor.execute(
        f"SELECT * FROM import.globaltemperaturesbycountry where country = '{country}' and dt like '%{year}%';"
    )
    country_data = cursor.fetchall()
    df_country = pd.DataFrame(
        country_data, columns=[desc[0] for desc in cursor.description]
    )
    df_country = cleaner(df_country)

    if test:

        return df_country

    max_temp = df_country["averagetemperature"].max()
    min_temp = df_country["averagetemperature"].min()
    mean_temp = df_country["averagetemperature"].mean()

    statement = f"In {country}, during {year}, the maximum temperature was {str(max_temp)}, the minimum temperature was {str(min_temp)}, and the average temperature was {mean_temp}."

    return statement


# Question 3: For a given year, which city has the highest/lowest temperature on average in a given country?
# TODO: Try the groupby in sql
def get_city_year_temp(country, year):
    cursor.execute(
        f"SELECT city FROM import.globaltemperaturesbymajorcity where country = '{country}' and dt like '%{year}%';"
    )
    country_data = cursor.fetchall()
    df_country = pd.DataFrame(
        country_data, columns=[desc[0] for desc in cursor.description]
    )
    # if df_country.empty:
    #     return "Data does not exist."
    df_country = cleaner(df_country)
    df_country["temperature"] = df_country.groupby(["year", "city"])[
        "averagetemperature"
    ].transform("mean")
    highest = df_country.sort_values(by=["temperature"], ascending=False).head(1)
    lowest = df_country.sort_values(by=["temperature"], ascending=True).head(1)
    highest_city = highest["city"].values[0]
    lowest_city = lowest["city"].values[0]

    result = f"In {country}, during {year}, the city with the highest recorded temperature was {highest_city}. The city with the lowest recorded temperature was {lowest_city}."

    return result


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
    country_data = cleaner(df_country)

    # time_series = df_country.groupby("year")["averagetemperature"].mean().reset_index()
    # print(time_series)

    # return time_series.to_json()

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

    # len = time_series.shape[0]
    # time_series.index = pd.period_range(
    #     start=np.min(time_series.index), periods=len, freq="Y"
    # )
    # endog = time_series
    # mod = sm.tsa.statespace.SARIMAX(
    #     endog, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12)
    # )
    # res = mod.fit()
    # fig, ax = plt.subplots(figsize=(12, 8))
    # plt.title("Temperature Forecast until 2050")
    # endog.loc["1824":].plot(ax=ax)
    # fcast = res.get_forecast("2050").summary_frame()
    # fcast["mean"].plot(ax=ax, style="k--", label="Forecast")
    # ax.fill_between(
    #     fcast.index,
    #     fcast["mean_ci_lower"],
    #     fcast["mean_ci_upper"],
    #     color="k",
    #     alpha=0.1,
    # )
    # return plt.show(block=True)


def main():

    get_future_temp("Thailand")


if __name__ == "__main__":
    main()
