from malaria_cnn.config.configuraion import ConfigurationManager
from malaria_cnn.components.model_training import PrepareCallbacks,Training
from malaria_cnn import logger


class TrainingPipeline:
    def __init__(self) -> None:
        pass
    def main(self):
        config=ConfigurationManager()
        prepare_callbacks_config=config.get_prepare_callbacks_config()
        prepare_callbacks=PrepareCallbacks(config=prepare_callbacks_config)
        callbacks_list=prepare_callbacks.get_tb_ckpt_callbacks()

        training_config=config.get_training_config()
        training=Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(callback_list=callbacks_list)


STAGE3='model training'

if __name__=='__main__':
    try:
        logger.info(f"Starting >>> {STAGE3} << stage")
        training_pipeline=TrainingPipeline()
        training_pipeline.main()
    except Exception as e:
        logger.error(f"Error in {STAGE3} stage: {e}")
        raise e
    