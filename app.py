import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="India Air Quality Dashboard",
    layout="wide"
)

st.title("India Air Quality Dashboard")

df = pd.read_csv("city_day_clean.csv")

city = st.sidebar.selectbox(
    "Select City",
    sorted(df["City"].unique())
)

filtered = df[df["City"] == city]

st.subheader(f"AQI Trend - {city}")

fig = px.line(
    filtered,
    x="Date",
    y="AQI"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

avg_aqi = round(filtered["AQI"].mean(),2)

worst_aqi = round(filtered["AQI"].max(),2)

good_days = len(
    filtered[filtered["AQI"] < 100]
)

c1,c2,c3 = st.columns(3)

c1.metric(
    "Average AQI",
    avg_aqi
)

c2.metric(
    "Worst AQI",
    worst_aqi
)

c3.metric(
    "Good Air Days",
    good_days
)