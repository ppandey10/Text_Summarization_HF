import os
from pathlib import Path
import urllib.request as rqst
import zipfile

from txtsummarizer.entity import DataIngestionConfig
from txtsummarizer.logging import logger
from txtsummarizer.utils.common import get_size

class DataIngestion:
    def __init__(
        self, 
        config: DataIngestionConfig
    ):
        self.config = config

    def download_data_from_url(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = rqst.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file
            )
            logger.info(f'{filename} downloaded! Information: \n{headers}')
        else:
            logger.info(f'{filename} already exists! Size: {get_size(Path(self.config.local_data_file))}')

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)