
from malaria_cnn.config.configuraion import ConfigurationManager
from malaria_cnn.components.dataingestion import DataIngestion



class DataIngestionPipeline:
    def __init__(self) :
        pass
    def main(self):
        try:
            config=ConfigurationManager()
            data_ingestion_config=config.get_data_ingestion_config()
            data_ingestion=DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise e