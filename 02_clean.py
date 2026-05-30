import pandas as pd

df = pd.read_csv("city_day.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Create Year column
df["Year"] = df["Date"].dt.year

# Create Month column
df["Month"] = df["Date"].dt.month

# Create Season column
df["Season"] = df["Month"].map({
    12:"Winter",1:"Winter",2:"Winter",
    3:"Spring",4:"Spring",5:"Spring",
    6:"Summer",7:"Summer",8:"Summer",
    9:"Monsoon",10:"Monsoon",11:"Monsoon"
})

# Remove rows with missing AQI
df = df.dropna(subset=["AQI"])

# Numeric columns
num_cols = [
    "PM2.5",
    "PM10",
    "NO2",
    "CO",
    "SO2",
    "O3"
]

# Fill missing values with median
for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

# Save cleaned file
df.to_csv("city_day_clean.csv", index=False)

print("Cleaning Complete")
print("Rows Remaining:", len(df))
