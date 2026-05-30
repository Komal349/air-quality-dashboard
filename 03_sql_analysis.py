import pandas as pd
import sqlite3

df = pd.read_csv("city_day_clean.csv")

conn = sqlite3.connect("airquality.db")

df.to_sql(
    "air_data",
    conn,
    if_exists="replace",
    index=False
)

# Query 1
query1 = """
SELECT
    City,
    ROUND(AVG(AQI),2) as Avg_AQI,
    ROUND(MAX(AQI),2) as Worst_AQI,
    COUNT(*) as Records
FROM air_data
GROUP BY City
ORDER BY Avg_AQI DESC
"""

result1 = pd.read_sql(query1, conn)

print("\nTop Polluted Cities")
print(result1.head(10))

# Query 2
query2 = """
WITH yearly AS
(
SELECT
    City,
    Year,
    ROUND(AVG(AQI),2) as Avg_AQI
FROM air_data
GROUP BY City,Year
)

SELECT
    City,
    Year,
    Avg_AQI,
    LAG(Avg_AQI)
    OVER(
        PARTITION BY City
        ORDER BY Year
    ) as Previous_Year
FROM yearly
"""

result2 = pd.read_sql(query2, conn)

print(result2.head())

conn.close()

