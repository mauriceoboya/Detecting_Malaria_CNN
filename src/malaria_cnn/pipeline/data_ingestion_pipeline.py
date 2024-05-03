
from malaria_cnn.config.configuraion import ConfigurationManager
from malaria_cnn.components.dataingestion import DataIngestion
from malaria_cnn import logger
STAGE1='Data Ingestion'

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
            logger.error(f"Error in {STAGE1} stage")
            raise e
        
    
if __name__=='__main__':
    try:
        data_ingestion_pipeline=DataIngestionPipeline()
        logger.info(f"Starting >>> {STAGE1} << stage")
        data_ingestion_pipeline.main()
        logger.info(f"Completed >>> {STAGE1} << stage")
    except Exception as e:
        logger.error(f"Error in {STAGE1} stage")
        raise e