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


# Question 4: For a given country, what is the future trend of their average temperature?
# TODO: Try prediction


def get_future_temp(country):
    cursor.execute(
        f"SELECT * FROM import.globaltemperaturesbycountry where country = '{country}';"
    )
    country_data = cursor.fetchall()
    df_country = cleaner(country_data)
    time_series = df_country.groupby("year")["averagetemperature"].mean()
    time_series.index = pd.period_range(df_country["year"].min, df_country["year"].max, freq="Y")
    endog = time_series
    mod = sm.tsa.statespace.SARIMAX(
        endog, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12)
    )
    res = mod.fit()
    fig, ax = plt.subplots(figsize=(12, 8))
    plt.title("Temperature Forecast until 2050")
    endog.loc["1824":].plot(ax=ax)
    fcast = res.get_forecast("2050").summary_frame()
    fcast["mean"].plot(ax=ax, style="k--", label="Forecast")
    ax.fill_between(
        fcast.index,
        fcast["mean_ci_lower"],
        fcast["mean_ci_upper"],
        color="k",
        alpha=0.1,
    )
    return plt.show(block=True)


def main():

    # get_country_plot("Europe")
    # temps = get_init_temp("Afghanistan")
    # print(temps)
    get_future_temp("Afghanistan")


if __name__ == "__main__":
    main()
