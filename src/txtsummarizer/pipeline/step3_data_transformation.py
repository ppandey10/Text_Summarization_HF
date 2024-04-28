from txtsummarizer.config.configuration import ConfigurationManager
from txtsummarizer.components.data_transformation import DataTransformation
from txtsummarizer.logging import logger

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.preprocess_and_save_data()