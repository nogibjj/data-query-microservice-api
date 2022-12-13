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
import random

def hello_world(to_whom = 'Eldians'):
    to_whom = str(to_whom)
    return f"Goodbye, {to_whom}, for raining the wrath of the Titans upon us."

def ESEP_fun_facts(member='pooja'):

    member = member.lower()
    E = ['hails from a Ugandan Kingdom', 'gives the best advice when drunk', 'trolls every human at all points in time']
    S = ['is a classic South Korean Noona',"ADORES SHINHWA and SHINHWA's CHAL SENGIN NAMJA", "was a South Korean Empress in the past life"]
    P = ['is way too easy to kidnap and take to Broadhead, Gross Hall, and Perkins', "has total turtle + grandma + Bengaluru energy", "is this team's guiding star, for better or worse"]

    fun_facts = {'emmanuel' : E, 'song' : S, 'pooja' : P}

    if member not in fun_facts:

        return "You are not our member, screw off"

    else:

        return member + ' ' + random.choice(fun_facts[member])