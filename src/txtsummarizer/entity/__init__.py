from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionConfig: # not normal python class
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    REQUIRED_FILES: list

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer: Path

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    data_path: Path
    model_name: Path
    save_model_name: str
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    per_device_eval_batch_size: int
    weight_decay: float
    logging_steps: int
    evaluation_strategy: str
    eval_steps: int
    save_steps: float
    gradient_accumulation_steps: int