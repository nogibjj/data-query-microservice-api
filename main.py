from fastapi import FastAPI
import uvicorn

# from mylib.logic import function_1
# from mylib.logic import function_2
# from mylib.logic import function_3

app = FastAPI()

# Here, I pasted my overall structure of project 4 that is relevant to this project.

# @app.get("/")
# async def root():
#     return {
#         "message": "Message to write here soon."
#     }


# @app.get("/types/{value}")
# async def types(value: str):
#     """docstring"""

#     result = function1(value)

#     return {"result": result}


# @app.get("/price/{value}")
# async def price(value: str):

#     """docstring"""

#     result = function2(value)

#     return {"result": result}


# @app.get("/participants/{value}")
# async def participants(value: str):

#     """docstring"""

#     result = function3(value)

#     return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
