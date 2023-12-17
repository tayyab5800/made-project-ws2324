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

    def test_download(self, data_extractor_instance, mocker):
        # Mock the download method to avoid actual file download
        mocker.patch.object(data_extractor_instance, 'download', return_value='mocked_file.csv')

        data_files_path = [data_extractor_instance.download(url) for url in test_urls]

        # Check that the mocked file is returned for each URL
        assert data_files_path == ['mocked_file.csv'] * len(test_urls)
        
    def test_transform(self, data_extractor_instance, mocker):
        # Mock the transform method to avoid actual transformation
        mocker.patch.object(data_extractor_instance, 'transform', side_effect=lambda x: None)

        # Mocking the read_csv function to avoid reading the actual file
        mocker.patch('pandas.read_csv', return_value=pd.DataFrame())

        # Perform the test
        data_files_path = [f for f in os.listdir('test_data') if os.path.isfile(os.path.join('test_data', f))]

        for file_path in data_files_path:
            data_extractor_instance.transform(os.path.join(os.getcwd(), 'test_data', file_path))
            df = pd.read_csv(os.getcwd() + "/test_data/" + file_path)
            assert not df.isnull().values.any()

    # system level test
    def test_data_extraction_pipeline(self, data_extractor_instance, mocker):
        # Mock the download method to avoid actual file download
        mocker.patch.object(data_extractor_instance, 'download', return_value='mocked_file.csv')

        # Mock the transform method to avoid actual transformation
        mocker.patch.object(data_extractor_instance, 'transform', side_effect=lambda x: None)

        # Mock the cleanup method to avoid actual cleanup
        mocker.patch.object(data_extractor_instance, 'cleanup', side_effect=lambda x: None)

        # Perform the test
        data_files_path = [data_extractor_instance.download(url) for url in test_urls]

        # Check that the mocked file is returned for each URL
        assert data_files_path == ['mocked_file.csv'] * len(test_urls)
        
        mocker.patch('pandas.read_csv', return_value=pd.DataFrame())

        # Perform the test
        data_files_path = [f for f in os.listdir('test_data') if os.path.isfile(os.path.join('test_data', f))]

        for file_path in data_files_path:
            data_extractor_instance.transform(os.path.join(os.getcwd(), 'test_data', file_path))
            df = pd.read_csv(os.getcwd() + "/test_data/" + file_path)
            assert not df.isnull().values.any()
        
        assert data_extractor_instance.cleanup(data_extractor_instance) == None

    def test_cleanup(self, data_extractor_instance):
        # Cleanup: Remove the test_data folder and its contents after the tests
        if os.path.exists(data_extractor_instance.output_folder):
            for file_name in os.listdir(data_extractor_instance.output_folder):
                file_path = os.path.join(data_extractor_instance.output_folder, file_name)
                os.remove(file_path)
            os.rmdir(data_extractor_instance.output_folder)
        assert not os.path.isdir(os.getcwd() + "/test_data/")