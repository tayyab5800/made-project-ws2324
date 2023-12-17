import pandas as pd
import os
from constants import urls

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
        
    def cleanup(self, data_extractor_instance='data'):
        # Cleanup: Remove the test_data folder and its contents after the tests
        if os.path.exists(data_extractor_instance):
            for file_name in os.listdir(data_extractor_instance):
                file_path = os.path.join(data_extractor_instance, file_name)
                os.remove(file_path)
            os.rmdir(data_extractor_instance)
            return True

if __name__ == "__main__":

    data_files_path = []
    helper = DataExtractor()

    for url in urls:
        try:
            data_files_path.append(helper.download(url))
        except ValueError as e:
            print(f"Error for URL {url}: {e}")

    for file_path in data_files_path:
        helper.transform(file_path)
    
    helper.cleanup()