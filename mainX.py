from fastapi import FastAPI
import uvicorn

from main.eda import eda_q1

# # from mylib.logic import function_1
# # from mylib.logic import function_2
# # from mylib.logic import function_3
# from main.logic import hello_world
# from main.logic import ESEP_fun_facts

# app = FastAPI()


# # Here, I pasted my overall structure of project 4 that is relevant to this project.

# @app.get("/")
# async def root():
#     return {
#         "message": "Message to write here soon. 706 ESEP TEAM ASSEMBLE!!!..."
#     }


# @app.get("/hello/{value}")
# async def types(value: str):
#     """Prints hello world"""

#     result = hello_world(value)

#     return {"result": result}

# @app.get("/members/{value}")
# async def members(value: str):
#     """Prints member fun facts, none of your business, those who know ... know"""

#     result = ESEP_fun_facts(value)

#     return {"result": result}


# # @app.get("/types/{value}")
# # async def types(value: str):
# #     """docstring"""

# #     result = function1(value)

# #     return {"result": result}


# # @app.get("/price/{value}")
# # async def price(value: str):

# #     """docstring"""

# #     result = function2(value)

# #     return {"result": result}


# # @app.get("/participants/{value}")
# # async def participants(value: str):

# #     """docstring"""

# #     result = function3(value)

# #     return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
