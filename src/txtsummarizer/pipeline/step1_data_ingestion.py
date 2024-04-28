from txtsummarizer.config.configuration import ConfigurationManager
from txtsummarizer.components.data_ingestion import DataIngestion
from txtsummarizer.logging import logger

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_data_from_url()
        data_ingestion.extract_zip_file()