import os
import pytest
import pandas as pd
from pipeline import DataExtractor
from constants import urls as test_urls

# Test the DataExtractor class
class TestDataExtractor:
    @pytest.fixture(scope="class")
    def data_extractor_instance(self):
        return DataExtractor(output_folder='test_data')

    def test_download(self, data_extractor_instance):
        data_files_path = []
        for url in test_urls:
            data_files_path.append(data_extractor_instance.download(url))

        assert all(os.path.isfile(file_path) for file_path in data_files_path)
        
    def test_transform(self, data_extractor_instance):
        data_files_path = [f for f in os.listdir('test_data') if os.path.isfile(os.path.join('test_data', f))]

        for file_path in data_files_path:
            data_extractor_instance.transform(os.getcwd() + "/test_data/" + file_path)
            # Check if there are no null values in the DataFrame
            df = pd.read_csv(os.getcwd() + "/test_data/" + file_path)
            assert not df.isnull().values.any()

    # system level test
    def test_data_extraction_pipeline(self, data_extractor_instance):

        data_files_path = []
        for url in test_urls:
            data_files_path.append(data_extractor_instance.download(url))

        assert all(os.path.isfile(file_path) for file_path in data_files_path)

        data_files_path = [f for f in os.listdir('test_data') if os.path.isfile(os.path.join('test_data', f))]

        for file_path in data_files_path:
            data_extractor_instance.transform(os.getcwd() + "/test_data/" + file_path)

            df = pd.read_csv(os.getcwd() + "/test_data/" + file_path)
            assert not df.isnull().values.any()

        data_extractor_instance.cleanup(data_extractor_instance)

        assert not os.path.isdir(os.getcwd() + "/test_data/")
        
    def test_cleanup(self, data_extractor_instance):
        # Cleanup: Remove the test_data folder and its contents after the tests
        if os.path.exists(data_extractor_instance.output_folder):
            for file_name in os.listdir(data_extractor_instance.output_folder):
                file_path = os.path.join(data_extractor_instance.output_folder, file_name)
                os.remove(file_path)
            os.rmdir(data_extractor_instance.output_folder)
        assert not os.path.isdir(os.getcwd() + "/test_data/")