# --server.enableCORS false --server.enableXsrfProtection false
import streamlit as st
import requests

st.title("Analysis of Global Temperatures from 1750 to 2015")

# TODO: Get list of countries from api
st.header("Question 4")
country = st.selectbox("Select a country:", ["Afghanistan", "Europe"], index=0)
st.write(country)
# response = requests.get(url=f'http://127.0.0.1:8000/init/{country}')
# print(response)
# st.write(response)