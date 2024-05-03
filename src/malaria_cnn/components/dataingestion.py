import os
import zipfile
from malaria_cnn import logger
from kaggle.api.kaggle_api_extended import KaggleApi
from malaria_cnn.utils.common import get_size
from malaria_cnn.entity.config_entity import DataIngestionConfig


class DataIngestion:

    def __init__(self,config=DataIngestionConfig):
        self.config=config
        os.environ['KAGGLE_USERNAME'] = "KAGGLE_USERNAME"
        os.environ['KAGGLE_KEY'] = "KAGGLE_KEY"
        self.api = KaggleApi()
        self.api.authenticate()
    def download_file(self):
        try:
            dataset_id = "iarunava/cell-images-for-detecting-malaria"
            zip_download_dir = os.path.dirname(self.config.local_data_file)  # Extract directory path
            os.makedirs(zip_download_dir, exist_ok=True)  # Ensure directory exists
            logger.info(f"Downloading data from {dataset_id} into directory {zip_download_dir}")
            self.api.dataset_download_files(dataset =dataset_id, path=zip_download_dir, unzip=False)
            logger.info(f"Downloaded data from {dataset_id} into directory {zip_download_dir}")
        except Exception as e:
            logger.error(f"Error downloading data from {dataset_id} into directory {zip_download_dir}")
            raise e

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
