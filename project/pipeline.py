import pandas as pd
import os
from constants import urls
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

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
    
    #helper.cleanup()
    try:
        # Load and plot data from File 2-1-cpi-12-factors-monthly-levels
        df_cpi_12_factors = pd.read_csv(data_files_path[1])

        # Heatmap for correlation matrix (excluding 'year' and 'month' columns)
        columns_to_exclude_cpi = ['year', 'month', 'Consumer price index overall']
        correlation_matrix_cpi = df_cpi_12_factors.drop(columns=columns_to_exclude_cpi).corr()

        sns.heatmap(correlation_matrix_cpi, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title(f"Correlation Matrix - CPI 12 Factors")
        plt.show()

        # Load and plot data from File 4-1-cpi-sp-energy-data
        df_cpi_sp_energy_data = pd.read_csv(data_files_path[6])

        # Line plot for overall consumer price index over time
        fig = px.line(df_cpi_sp_energy_data, x="year", y="overall_index_excluding_energy", title="Overall Consumer Price Index Over Time")
        fig.show()

        # Bar chart for distribution of components
        fig = px.bar(df_cpi_sp_energy_data, x="year", y=["energy_household_and_fuels", "energy_household_electricity_gas_and_other_fuels", "heating_oil_and_fuels"],
                    title="Distribution of Components Over Years")
        fig.show()

        # Load and plot data from File 4-2-cpi-sp-energy-data-annual-avg
        df_cpi_sp_energy_data_avg = pd.read_csv(data_files_path[7])

        # Bar chart for overall consumer price index for each year
        fig = px.bar(df_cpi_sp_energy_data_avg, x="year", y="overall_index_excluding_energy", title="Yearly Overview of Consumer Price Index")
        fig.show()

        # Load and plot data from File 4-3-cpi-sp-energy-dist-data
        df_cpi_sp_energy_dist_data = pd.read_csv(data_files_path[8])

        # Convert percentage values to numeric
        for col in df_cpi_sp_energy_dist_data.columns[1:-1]:
            df_cpi_sp_energy_dist_data[col] = pd.to_numeric(df_cpi_sp_energy_dist_data[col].str.replace(',', '.'), errors='coerce')

        # Melt the dataframe for better plotting
        melted_df_cpi_sp_energy_dist = pd.melt(df_cpi_sp_energy_dist_data, id_vars=["distribution_of_energy_sources", "value_in_percentage"],
                            var_name="year", value_name="percentage")

        # Line plot for changes in the percentage distribution of each energy source over the years
        fig = px.line(melted_df_cpi_sp_energy_dist, x="year", y="percentage", color="distribution_of_energy_sources",
                      title="Changes in Percentage Distribution of Energy Sources Over Years",
                      labels={"percentage": "Percentage Distribution", "year": "Year"})
        fig.show()

    except FileNotFoundError as e:
        print(f"Error: {e}")