import pandas as pd
from sqlalchemy import create_engine , types
import os

url = "https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV"
df = pd.read_csv(url, delimiter=';')

# Droping the "Status" column
df = df.drop(columns=["Status"])

df = df[df["Verkehr"].isin(["FV", "RV", "nur DPN"])]

# Convert "Laenge" and "Breite" columns to numeric, replacing commas with dots
df["Laenge"] = pd.to_numeric(df["Laenge"].str.replace(',', '.'), errors="coerce")
df["Breite"] = pd.to_numeric(df["Breite"].str.replace(',', '.'), errors="coerce")

df = df[(df["Laenge"] >= -90) & (df["Laenge"] <= 90) & (df["Breite"] >= -90) & (df["Breite"] <= 90)]

# check validity of IFOPT values
def check_ifopt_validity(value):
    if isinstance(value, str):
        chunks = value.split(":")
        if len(chunks) >= 3 and all(chunk.isdigit() for chunk in chunks[1:]):
            return True
    return False

df = df[df["IFOPT"].apply(check_ifopt_validity)]
df = df.dropna()

# Define SQLite types for each column
sqlite_types = {
    "EVA_NR": types.BIGINT(),
    "DS100": types.TEXT(),
    "IFOPT": types.TEXT(),
    "NAME": types.TEXT(),
    "Verkehr": types.TEXT(),
    "Laenge": types.FLOAT(),
    "Breite": types.FLOAT(),
    "Betreiber_Name": types.TEXT(),
    "Betreiber_Nr": types.TEXT()
}
path = os.getcwd()
db_path = os.path.join(path, "trainstops.sqlite")
engine = create_engine(f"sqlite:///{db_path}")# Write the DataFrame to the SQLite database
df.to_sql("trainstops", engine, index=False, if_exists="replace", dtype=sqlite_types)

print(f"Data is written to {db_path}")