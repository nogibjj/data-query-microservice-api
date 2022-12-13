# import requests

# def get_random_activity():
#     """Get random activity from the Bored API"""
#     url = "https://www.boredapi.com/api/activity/"
#     response = requests.get(url)
#     return response.json()


# def get_activity_by_price(value):
#     """Get random activity according to price inputted"""

#     x = float(value)

#     if x < 0 and x > 1:
#         return "No activity found with that price. Your options are from 0 to 1."

#     response = requests.get(
#         f"https://www.boredapi.com/api/activity?price={x}", timeout=120
#     )

#     return response.json()


