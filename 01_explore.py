import pandas as pd

df = pd.read_csv("city_day.csv")

print("\nFIRST 5 ROWS")
print(df.head())

print("\nDATASET SHAPE")
print(df.shape)

print("\nCOLUMN NAMES")
print(df.columns.tolist())

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nDATA TYPES")
print(df.dtypes)

print("\nCITIES")
print(df["City"].unique())
