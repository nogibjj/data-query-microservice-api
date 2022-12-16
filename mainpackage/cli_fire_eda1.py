#!/usr/bin/env python
# import os
# import sys
# # PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
# # sys.path.append(PROJECT_ROOT)
import fire
from eda_fire_q1 import get_city_year_temp
from eda_fire_q1 import get_country_plot
from eda_fire_q1 import get_countries_list
from eda_fire_q1 import get_future_temp
from eda_fire_q1 import get_country_year_temp


if __name__ == "__main__":
    fire.Fire()

# don't forget to chmod this file later, erase this line when you do.
# chmod +x cli-fire.py
