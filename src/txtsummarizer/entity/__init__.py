from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionConfig: # not normal python class
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path