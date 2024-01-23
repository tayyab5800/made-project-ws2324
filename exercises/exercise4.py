import urllib.request
import zipfile
import pandas as pd
from sqlalchemy import create_engine , types
import os

url = "https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip"  
local_zip_filename = "data.zip" 
extracted_folder = os.getcwd()
print(f"Extracted Folder is {extracted_folder}")

# Download the zip file
urllib.request.urlretrieve(url, local_zip_filename)

# Unzip the file
with zipfile.ZipFile(local_zip_filename, 'r') as zip_ref:
    zip_ref.extractall(extracted_folder)
    
csv_file_path = os.getcwd() + '/data.csv'

# Read only the specified columns
df = pd.read_csv(csv_file_path, delimiter=';', decimal=',', usecols=["Geraet"])

df.to_clipboard(sep=",")

# Specify first 11 columns to rename the dataset header
columns_to_read = ["Geraet","Hersteller","Model","Monat",
                    "Temperatur in °C (DWD)","Latitude (WGS84)",
                    "Longitude (WGS84)","Verschleierung (m)",
                    "Aufenthaltsdauer im Freien (ms)",
                    "Batterietemperatur in °C", 
                    "Geraet aktiv","extra"]

df = pd.read_clipboard(sep=",")
df.columns = columns_to_read
df.drop(columns=["extra","Latitude (WGS84)",
                    "Longitude (WGS84)","Verschleierung (m)",
                    "Aufenthaltsdauer im Freien (ms)"], inplace=True)
column_mapping = {"Temperatur in °C (DWD)":"Temperatur",
                    "Batterietemperatur in °C":"Batterietemperatur"}

df.rename(columns=column_mapping, inplace=True)
df['Temperatur'] = df['Temperatur'].apply(lambda x: (x * 9/5) + 32)
df['Batterietemperatur'] = df['Batterietemperatur'].apply(lambda x: (x * 9/5) + 32)

# Define SQLite types for each column
sqlite_types = {
    "Geraet": types.BIGINT(),
    "Hersteller": types.TEXT(),
    "Model": types.TEXT(),
    "Monat": types.BIGINT(),
    "Temperatur": types.FLOAT(),
    "Batterietemperatur": types.FLOAT(),
    "Geraet aktiv": types.TEXT()
}

path = os.getcwd()
db_path = os.path.join(path, "temperatures.sqlite")
engine = create_engine(f"sqlite:///{db_path}")
df.to_sql("temperatures", engine, index=False, if_exists="replace", dtype=sqlite_types)

print(f"Data is written to {db_path}")

