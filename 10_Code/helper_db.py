import psycopg2
import os

# RDS_HOSTNAME_global_temperatures = os.environ.get("RDS_HOSTNAME")
# RDS_PASSWORD = os.environ.get("RDS_PASSWORD")


def connect_to_db():
    connection = psycopg2.connect(
        host="global-temperatures.cndtu3jnk9za.us-east-1.rds.amazonaws.com",
        port=5432,
        user="postgres",
        password="postgres",
        database="globaltemperatures",
    )
    cursor = connection.cursor()
    return cursor
