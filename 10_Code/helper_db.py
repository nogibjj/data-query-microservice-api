# 
import os
RDS_HOSTNAME_global_temperatures = os.environ.get("RDS_HOSTNAME")
RDS_PASSWORD = os.environ.get("RDS_PASSWORD")

import psycopg2

def connect_to_db():
    connection = psycopg2.connect(
        host=RDS_HOSTNAME_global_temperatures, port=5432, user="postgres", password=RDS_PASSWORD, database="globaltemperatures"
    )
    cursor = connection.cursor()
    return cursor

