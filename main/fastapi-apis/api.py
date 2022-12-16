from fastapi import FastAPI, Response
import json
import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(PROJECT_ROOT)
import eda.eda_q1 as eda
import eda.eda_q2 as eda2

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/countries")
def get_countries_list():
    countries = eda.get_countries_list()
    countries.sort()
    return Response(content=json.dumps({"result": countries}), media_type="application/json")

@app.get("/trend/{country}")
def get_country_plot(country: str):
    df_json = eda.get_country_plot(str(country))
    return Response(content=json.dumps({"result":df_json}), media_type="application/json")

@app.get("/year/{country}/{year}")
def get_country_year_temp(country: str, year: str):
    result = eda.get_country_year_temp(str(country), str(year))
    return Response(content=json.dumps({"result": str(result)}), media_type="application/json")

@app.get("/city/{country}/{year}")
def get_city_year_temp(country: str, year:str):
    result = eda.get_city_year_temp(str(country), str(year))
    return Response(content=json.dumps({"result": str(result)}), media_type="application/json")

@app.get("/prediction/{country}")
def get_init_temp(country: str):
    df_json = eda.get_future_temp(str(country))
    return Response(content=json.dumps({"result":df_json}), media_type="application/json")

@app.get("/decade")
def get_last_decade_temp():
    df_json = eda2.global_temperatures_decade()
    return Response(content=json.dumps({"result":df_json}), media_type="application/json")

@app.get("/century")
def get_last_century_temp():
    df_json = eda2.global_temperatures_century()
    return Response(content=json.dumps({"result":df_json}), media_type="application/json")

@app.get("/seasons")
def get_top5_seasons_temp():
    seasons_df_list = eda2.get_temperatures_top5()
    return Response(content=json.dumps({"result":seasons_df_list}), media_type="application/json")