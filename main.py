from fastapi import FastAPI
import uvicorn
from mylib.logic import get_activity_by_price
from mylib.logic import get_activity_by_type
from mylib.logic import get_activity_by_participant_count

app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "Bored API.  Get your random activity by calling /types, /price  or /participants ."
    }


@app.get("/types/{value}")
async def types(value: str):
    """Get random activity according to type inputted"""

    result = get_activity_by_type(value)

    return {"result": result}


@app.get("/price/{value}")
async def price(value: str):

    """Get random activity according to price inputted"""

    result = get_activity_by_price(value)

    return {"result": result}


@app.get("/participants/{value}")
async def participants(value: str):

    """Get random activity according to number of participants inputted"""

    result = get_activity_by_participant_count(value)

    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
