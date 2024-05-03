from malaria_cnn.components.prepare_basemodel import PrepareBaseModel
from malaria_cnn.config.configuraion import ConfigurationManager
from malaria_cnn import logger


class PrepareBaseModelPipeline:
    def __init__(self) :
        pass
    def main(self):
        try:
            config=ConfigurationManager()
            prepare_base_model_config=config.get_prepare_model_config()
            prepare_base_model=PrepareBaseModel(config=prepare_base_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()
        except Exception as e:
            raise e
        
    

STAGE2='Preparing Base Model'

if __name__=="__main__":
    try:
        logger.info(f"Starting >>> {STAGE2} << stage")
        prepare_base_model_pipeline=PrepareBaseModelPipeline()
        prepare_base_model_pipeline.main()
        logger.info(f"Completed >>> {STAGE2} << stage")
    except Exception as e :
        logger.error(f"Error in {STAGE2} stage")
        raise e