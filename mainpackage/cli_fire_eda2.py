#!/usr/bin/env python
# import os
# import sys
# # PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
# # sys.path.append(PROJECT_ROOT)
import fire

from eda_fire_q2 import global_temperatures_decade
from eda_fire_q2 import global_temperatures_century
from eda_fire_q2 import get_temperatures_top5

if __name__ == "__main__":
    fire.Fire()

# don't forget to chmod this file later, erase this line when you do.
# chmod +x cli-fire.py
