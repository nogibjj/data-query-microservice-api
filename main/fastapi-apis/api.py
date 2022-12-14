from fastapi import FastAPI
import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(PROJECT_ROOT)
import eda.eda_q1 as eda

app = FastAPI()

@app.get("/")
def root(text):
    return {"message": "Hello World"}

@app.get("/trend/{country}")
def get_country_plot(value: str):
    eda.get_country_plot(str(country))
    return {"result": str(country)}

@app.get("/year/{country}/{year}")
def get_country_year_temp(value: str):
    result = eda.get_country_year_temp(str(country), str(year))
    return {"result": str(result)}

@app.get("/city/{country}/{year}")
def get_city_year_temp(value: str):
    result = eda.get_city_year_temp(str(country), str(year))
    return {"result": str(result)}

@app.get("/init/{country}")
def get_init_temp(value: str):
    result = eda.get_init_temp(str(country))
    return {"result": str(result)}