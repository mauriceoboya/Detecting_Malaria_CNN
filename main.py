from malaria_cnn.pipeline import data_ingestion_pipeline
from malaria_cnn import logger

STAGE1='Data Ingestion'


try:
    logger.info(f"Starting >>> {STAGE1} << stage")
    data_ingestion=data_ingestion_pipeline.DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f"Completed >>> {STAGE1} << stage")

except Exception as e :
    logger.error(f"Error in {STAGE1} stage")
    raise e