from txtsummarizer.config.configuration import ConfigurationManager
from txtsummarizer.components.model_trainer import ModelTrainer
from txtsummarizer.logging import logger

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train_and_save_model()