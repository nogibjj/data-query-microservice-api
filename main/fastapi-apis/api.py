from fastapi import FastAPI, Response
import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(PROJECT_ROOT)
import eda.eda_q1 as eda

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/trend/{country}")
def get_country_plot(country: str):
    eda.get_country_plot(str(country))
    return {"result": str(country)}

@app.get("/year/{country}/{year}")
def get_country_year_temp(country: str, year: str):
    result = eda.get_country_year_temp(str(country), str(year))
    return {"result": str(result)}

@app.get("/city/{country}/{year}")
def get_city_year_temp(country: str, year:str):
    result = eda.get_city_year_temp(str(country), str(year))
    return {"result": str(result)}

@app.get("/init/{country}")
def get_init_temp(country: str):
    # result = eda.get_init_temp(str(country))
    result = [1, 2, 3, 4]
    return Response(content=result, media_type="application/json")