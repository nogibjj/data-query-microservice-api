# from mylib.logic import get_activity_by_participant_count
# from mylib.logic import get_activity_by_type
# from mylib.logic import get_activity_by_price
import os
import sys
import re
import pandas as pd

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(PROJECT_ROOT)

import helpers

from eda.eda_q1 import get_countries_list
from eda.eda_q1 import get_country_plot
from eda.eda_q1 import get_country_year_temp
from eda.eda_q1 import get_city_year_temp
from eda.eda_q1 import get_future_temp

# from eda.eda_q1 import cleaner


def test_get_countries_list():
    """Verifying country list length"""

    countries = get_countries_list()

    assert len(countries) == 243

    pass


def test_get_country_plot():

    """test_get_country_plot"""

    assert type(get_country_plot("India")) == str

    India = pd.read_json(get_country_plot("India"))

    assert (
        India.loc[India["dt"] == "2012-01-01", "averagetemperature"].iloc[0] == 16.778
    )

    assert (
        India.loc[India["dt"] == "2012-01-01", "averagetemperatureuncertainty"].iloc[0]
        == 0.267
    )

    assert India.loc[India["dt"] == "2012-01-01", "country"].iloc[0] == "India"

    assert India.loc[India["dt"] == "2012-01-01", "season"].iloc[0] == "winter"

    assert India.loc[India["dt"] == "2012-01-01", "year"].iloc[0] == 2012

    assert round(
        (India.loc[India["dt"] == "2012-01-01", "temperature"].iloc[0]), 3
    ) == round(24.640833, 3)

    # Triggering Error Handling for assert

    assert type(get_country_plot("Hogwarts")) == str

    assert "Hogwarts" in get_country_plot("Hogwarts")

    pass


def test_get_country_year_temp():

    """test_get_country_year_temp"""

    India = get_country_year_temp("India", 2012, test=True)

    assert India.loc[India["year"] == 2012, "country"].iloc[0] == "India"

    # mean = df.groupby('year').averagetemperature.mean()

    minimum = India.groupby("year").averagetemperature.min().iloc[0]

    maximum = India.groupby("year").averagetemperature.max().iloc[0]

    statement = get_country_year_temp("India", 2012)

    metrics = re.findall("[0-9]{0,3}\.[0-9]+", statement)

    metrics = [float(i) for i in metrics]

    test_max, test_min = metrics[0], metrics[1]

    assert round(test_max, 2) == round(maximum, 2)

    assert round(test_min, 2) == round(minimum, 2)

    # triggering error handling for assert

    assert type(get_country_year_temp("Narnia", "2010")) == str

    assert "Narnia" in get_country_year_temp("Narnia", "2010")

    assert type(get_country_year_temp("Uganda", "2022")) == str

    assert "Data does not exist" in get_country_year_temp("Uganda", "2022")

    pass


def test_get_city_year_temp():

    """test_get_city_year_temp"""

    us = get_city_year_temp("United States", 2008, test=True)

    assert us.loc[us["year"] == 2008, "country"].iloc[0] == "United States"

    assert (
        round(
            us.loc[
                (us["dt"] == "2008-12-01") & (us["city"] == "Chicago"),
                "averagetemperature",
            ].iloc[0],
            3,
        )
        == -0.664
    )

    check_city = [i for i in us["city"].unique()]

    for city in ["Chicago", "New York", "Los Angeles"]:

        assert city in check_city

    us["temperature"] = us.groupby(["year", "city"])["averagetemperature"].transform(
        "mean"
    )
    highest = us.sort_values(by=["temperature"], ascending=False).head(1)
    lowest = us.sort_values(by=["temperature"], ascending=True).head(1)
    highest_city = highest["city"].values[0]
    lowest_city = lowest["city"].values[0]

    statement = get_city_year_temp("United States", 2008)

    statement = statement.split(".")

    assert highest_city in statement[0] and highest_city not in statement[1]

    assert lowest_city in statement[1] and lowest_city not in statement[0]

    # triggering error handling for assert

    assert type(get_city_year_temp("Ghibli", "2010")) == str

    assert "Ghibli" in get_city_year_temp("Ghibli", "2010")

    assert type(get_city_year_temp("Puerto Rico", "2022")) == str

    assert "Data does not exist" in get_city_year_temp("Puerto Rico", "2022")

    pass


def test_get_future_temp():

    test_case = pd.read_json(get_future_temp("Uganda"))

    assert test_case.year.unique().min() == 1850

    assert test_case.year.unique().max() == 2013

    avg_temp = (test_case.loc[test_case["year"] == 2009, "averagetemperature"]).iloc[0]

    assert round(avg_temp, 3) == round(24.047167, 3)

    assert type(get_future_temp("Castle Oblivion")) == str

    assert "Data Engineering" in get_future_temp("Data Engineering")

    pass


test_get_countries_list()
test_get_country_plot()
test_get_country_year_temp()
test_get_city_year_temp()
test_get_future_temp()
