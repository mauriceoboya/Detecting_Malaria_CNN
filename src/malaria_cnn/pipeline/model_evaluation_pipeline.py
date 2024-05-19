from malaria_cnn.config.configuraion import ConfigurationManager
from malaria_cnn.components.model_evaluation import Evaluation
from malaria_cnn import logger


class EvaluationPipeline:
    def __init__(self) -> None:
        pass
    def main(self):
        config=ConfigurationManager()
        eval=Evaluation(config.get_validation_config())
        eval.evaluation()
        eval.save_score()



STAGE4='model evaluation'

if __name__=='__main__':
    try:
        logger.info(f"Starting >>> {STAGE4} << stage")
        evaluation_pipeline=EvaluationPipeline()
        evaluation_pipeline.main()
    except Exception as e:
        logger.error(f"Error in {STAGE4} stage: {e}")
        raise e
    