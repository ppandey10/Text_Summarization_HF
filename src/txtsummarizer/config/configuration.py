from txtsummarizer.utils.common import read_yaml, create_directories
from txtsummarizer.constants import *
from txtsummarizer.entity import DataIngestionConfig, DataValidationConfig

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILEPATH,
        params_filepath = PARAMS_FILEPATH
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # Create artifacts folder
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        # Create directory
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        # Create directory
        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            REQUIRED_FILES=config.REQUIRED_FILES
        )

        return data_validation_config