import pandas as pd
import plotly.express as px

df = pd.read_csv("city_day_clean.csv")

# Top polluted cities

city_aqi = (
    df.groupby("City")["AQI"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

fig = px.bar(
    x=city_aqi.index,
    y=city_aqi.values,
    title="Top 10 Polluted Cities"
)

fig.show()

