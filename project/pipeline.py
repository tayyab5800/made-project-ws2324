import pandas as pd
import os

class DataExtractor:
    def __init__(self, output_folder='data'):
        self.output_folder = output_folder
        os.makedirs(self.output_folder, exist_ok=True)

    def download(self, url: str):
        df = pd.read_csv(url, delimiter=";", on_bad_lines='skip', encoding="unicode_escape")
        file_path = os.path.join(self.output_folder, url.split("/")[-1])
        df.to_csv(file_path, index=False)
        return file_path
    
    def transform(self, file_path: str):
        df = pd.read_csv(file_path)
        
        # remove all special characters from all csv files
        df.columns = df.columns.str.replace(r'[^a-zA-Z0-9_ ]', '', regex=True)
        
        # Perform transformation (example: drop null values)
        if file_path.startswith(f"{self.output_folder}/1"):
            # drop first row, replicated months
            df = df.drop(0)
            df = df.rename(columns={'Unnamed: 0': 'id', 'Unnamed: 1': 'title'})
            # making pivot table for data analysis
            df = pd.melt(df, id_vars= df.columns.tolist()[0:2], value_vars= df.columns.tolist()[2:])    

        elif file_path.startswith(f"{self.output_folder}/4-3"):
            df = df.fillna(0)
            
        elif file_path.startswith(f"{self.output_folder}/5"):
            df = df.rename(columns={'Unnamed 0': 'title'})
            
        else:
            df = df.dropna()

        # Save the transformed DataFrame back to the same file
        df.to_csv(file_path, index=False)
        

if __name__ == "__main__":
    # link to all data sources
    urls = [
        "https://raw.githubusercontent.com/tayyab5800/german-housing-prices-drop/main/1-cpi-germany-individual-consumption-by-purpose-61111-0004.csv",
        "https://raw.githubusercontent.com/tayyab5800/german-housing-prices-drop/main/2-1-cpi-12-factors-monthly-levels.csv",
        "https://raw.githubusercontent.com/tayyab5800/german-housing-prices-drop/main/2-2-cpi-12-factors-change-on-previous-months.csv",
        "https://raw.githubusercontent.com/tayyab5800/german-housing-prices-drop/main/2-3-cpi-12-factors-annual-avg.csv",
        "https://raw.githubusercontent.com/tayyab5800/german-housing-prices-drop/main/2-4-cpi-12-factors-change_on_prev_years.csv",
        "https://raw.githubusercontent.com/tayyab5800/german-housing-prices-drop/main/3-interest-rate.csv",
        "https://raw.githubusercontent.com/tayyab5800/german-housing-prices-drop/main/4-1-cpi-sp-energy-data.csv",
        "https://raw.githubusercontent.com/tayyab5800/german-housing-prices-drop/main/4-2-cpi-sp-energy-data-annual-avg.csv",
        "https://raw.githubusercontent.com/tayyab5800/german-housing-prices-drop/main/4-3-cpi-sp-energy-dist-data.csv",
        "https://raw.githubusercontent.com/tayyab5800/german-housing-prices-drop/main/5-housing-prices-6-quarters-61262-0002.csv",
        "https://raw.githubusercontent.com/tayyab5800/german-housing-prices-drop/main/6-1-property-price-indices-district-types.csv",
        "https://raw.githubusercontent.com/tayyab5800/german-housing-prices-drop/main/6-2-property-price-indices-rate-of-change.csv"
        ]

    data_files_path = []
    helper = DataExtractor()

    for url in urls:
        try:
            data_files_path.append(helper.download(url))
        except ValueError as e:
            print(f"Error for URL {url}: {e}")

    for file_path in data_files_path:
        helper.transform(file_path)