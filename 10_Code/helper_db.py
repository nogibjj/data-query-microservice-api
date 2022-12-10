# 
RDS_HOSTNAME_global_temperatures="global-temperatures.cndtu3jnk9za.us-east-1.rds.amazonaws.com"
RDS_PASSWORD="postgres"
import psycopg2

def connect_to_db():
    connection = psycopg2.connect(
        host=RDS_HOSTNAME_global_temperatures, port=5432, user="postgres", password=RDS_PASSWORD, database="globaltemperatures"
    )
    cursor = connection.cursor()
    return cursor

