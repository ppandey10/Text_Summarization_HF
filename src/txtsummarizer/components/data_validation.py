import os

from txtsummarizer.entity import DataValidationConfig
from txtsummarizer.logging import logger
from txtsummarizer.utils.common import get_size

class DataValidation:
    def __init__(
        self, 
        config: DataValidationConfig
    ):
        self.config = config

    def data_availability(self) -> bool:
        try: 
            validation_status = None
            available_files = os.listdir(os.path.join('artifacts', 'data_ingestion', 'samsum_data'))

            for file in available_files:
                if file not in self.config.REQUIRED_FILES:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f'Validation Status: {validation_status}')
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f'Validation Status: {validation_status}')
        except Exception as e:
            raise e