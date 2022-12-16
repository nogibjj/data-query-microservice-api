# --server.enableCORS false --server.enableXsrfProtection false
import streamlit as st
import requests
import pandas as pd
import altair as alt
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt

# https://wx3ucb3jpz.us-east-1.awsapprunner.com/
host = "http://127.0.0.1:8000"

countries = requests.get(url=f'{host}/countries').json()["result"]

st.title("Analysis of Global Temperatures from 1750 to 2015")

# QUESTION 1
st.header("Question 1: For a given country, what is the trend of their average temperature?")
q1_country = st.selectbox("Select a country / region:", countries, index=0)
print("selected country question 1: ", q1_country)
q1_response = requests.get(url=f'{host}/trend/{q1_country}').json()["result"]
q1_df = pd.read_json(str(q1_response))
q1_lines = (
        alt.Chart(q1_df, title=f"Trend of average temperature of {q1_country}")
        .mark_line()
        .encode(
            alt.X("year",scale=alt.Scale(domain=(1750, 2015)),axis=alt.Axis( title='Year')),
            alt.Y('temperature',scale=alt.Scale(zero=False),axis=alt.Axis( title='Temperature in Celsius'))
        )
    )
st.altair_chart(
    (q1_lines).interactive(),
    use_container_width=True
)

# QUESTION 2
st.header("Question 2: For a given year and a given country, what is the max/min temperature?")
q2_country = st.selectbox("Select a country / region:", countries, index=0, key="q2_country")
q2_year = st.selectbox("Select a year:", list(range(1750, 2016)), index=0, key="q2_year")
print("selected country question 2: ", q2_country)
print("selected year question 2: ", q2_year)
q2_response = requests.get(url=f'{host}/year/{q2_country}/{q2_year}')
st.write(q2_response.json()["result"])

# QUESTION 3
st.header("Question 3: For a given year, which city has the highest/lowest temperature on average in a given country?")
q3_country = st.selectbox("Select a country / region:", countries, index=0, key="q3_country")
q3_year = st.selectbox("Select a year:", list(range(1750, 2016)), index=0, key="q3_year")
print("selected country question 3: ", q3_country)
print("selected year question 3: ", q3_year)
q3_response = requests.get(url=f'{host}/city/{q3_country}/{q3_year}')
print(q3_response.json())
st.write(q3_response.json()["result"])

# QUESTION 4
# st.header("Question 4: For a given country, what is the future trend of their average temperature?")
# q4_country = st.selectbox("Select a country / region:", countries, index=0, key="q4_country")
# print("selected country question 4: ", q4_country)
# q4_response = requests.get(url=f'{host}/prediction/{q4_country}').json()["result"]
# print(q4_response)
# q4_df = pd.read_json(str(q4_response))

# len = q4_df.shape[0]
# q4_df.index = pd.period_range(
#     start=np.min(q4_df["year"]), periods=len, freq="Y"
# )
# endog = q4_df["averagetemperature"]
# mod = sm.tsa.statespace.SARIMAX(
#     endog, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12)
# )
# res = mod.fit()
# fig, ax = plt.subplots(figsize=(12, 8))
# plt.title("Temperature Forecast until 2050 for {q4_country}")
# endog.loc["1824":].plot(ax=ax)
# fcast = res.get_forecast("2050").summary_frame()
# fcast["mean"].plot(ax=ax, style="k--", label="Forecast")
# ax.fill_between(
#     fcast.index,
#     fcast["mean_ci_lower"],
#     fcast["mean_ci_upper"],
#     color="k",
#     alpha=0.1,
# )
# st.pyplot(fig)

# QUESTION 5 - Decade
# TODO: Get year for x-axis
st.header("Question 5: For a given country, what is the trend of their average temperature?")
q5_response = requests.get(url=f'{host}/decade').json()["result"]
q5_df = pd.read_json(str(q5_response))
q5_lines = (
        alt.Chart(q5_df, title=f"Trend of average temperature")
        .mark_line()
        .encode(
            alt.X("dt",axis=alt.Axis( title='Year')),
            alt.Y('movingaverage',scale=alt.Scale(zero=False),axis=alt.Axis( title='Temperature in Celsius'))
        )
    )
st.altair_chart(
    (q5_lines).interactive(),
    use_container_width=True
)

# QUESTION 6
st.header("Question 6: For a given country, what is the trend of their average temperature?")
q6_response = requests.get(url=f'{host}/century').json()["result"]
q6_df = pd.read_json(str(q6_response))
q6_df = q6_df.reset_index()
print(q6_df.dtypes)
q6_lines = (
        alt.Chart(q6_df, title=f"Trend of average temperature")
        .mark_line()
        .encode(
            alt.X('index',axis=alt.Axis( title='Year')),
            alt.Y('landaveragetemperature',scale=alt.Scale(zero=False),axis=alt.Axis( title='Temperature in Celsius'))
        )
    )
st.altair_chart(
    (q6_lines).interactive(),
    use_container_width=True
)

# QUESTION 7
st.header("Question 7: For a given country, what is the trend of their average temperature?")
q7_response = requests.get(url=f'{host}/seasons').json()["result"]

seasons = ["winter", "spring", "summer", "autumn", "monsoon", "fall"]
def create_chart(df, season):
    chart = alt.Chart(df).mark_line().encode(
        x=alt.X('year', title='Year'),
        y=alt.Y('averagetemperature', scale=alt.Scale(zero=False), title='Temperature (Celsius)'),
        color=alt.Color('country', title='Country'),
        tooltip=['year', 'averagetemperature', 'country']
    ).properties(
        width=600,
        height=300,
        title=season)

    st.altair_chart(
    (chart).interactive(),
    use_container_width=True
)

for i in range(len(q7_response)):
    season_df = pd.read_json(str(q7_response[i]))
    create_chart(season_df, seasons[i])