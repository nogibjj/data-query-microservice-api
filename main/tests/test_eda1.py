# from mylib.logic import get_activity_by_participant_count
# from mylib.logic import get_activity_by_type
# from mylib.logic import get_activity_by_price
import os
import sys
import re
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(PROJECT_ROOT)

import helpers
from eda.eda_q1 import get_country_plot
# from eda.eda_q1 import cleaner
from eda.eda_q1 import get_country_year_temp


cursor = helpers.connect_to_db()


# these are the import statements for the testing of the logic.py

# def test_f1():


def test_get_country_plot():

    """Testing the non-plot contents of get_country_plot"""

    df = get_country_plot("India", test=True)

    assert df.loc[df["dt"] == "2013-06-01", "averagetemperature"].iloc[0] == 28.766

    assert type(get_country_plot("Hogwarts", test=True)) == str

    assert 'Hogwarts' in get_country_plot("Hogwarts", test=True)

    pass


def test_get_country_year_temp():

    df = get_country_year_temp('Puerto Rico', 2012, test=True)

    mean = df.groupby('year').averagetemperature.mean()

    minimum = y.groupby('year').averagetemperature.min()

    maximum = y.groupby('year').averagetemperature.max()

    statement =  get_country_year_temp('Puerto Rico', 2012)

    metrics = re.findall('[0-9]{4}',statement)

    metrics = [int(i) for i in metrics]

    assert 



    # error handling 
    
    assert type(get_country_year_temp('Narnia','2010')) == str

    assert 'Narnia' in get_country_year_temp('Narnia','2010')

    assert type(get_country_year_temp('India','2022')) == str

    assert '2022' in get_country_year_temp('India','2022')

# doc string and assert statement


# def test_f2():

# doc string and assert statement


# def test_f3():

# doc string and assert statement

# test_function_1
# test_function_2
# test_function_3
