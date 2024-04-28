import os
from pathlib import Path

from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk

from txtsummarizer.entity import DataTransformationConfig
from txtsummarizer.logging import logger

class DataTransformation:
    def __init__(
        self,
        config: DataTransformationConfig
    ):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer)

    def tokenize_and_prepare_data(self, example_batch):
        input_encodings = self.tokenizer(example_batch['dialogue'] , max_length = 1024, truncation = True )
        
        # switch the tokenizer mode to target tokenization.
        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], max_length = 128, truncation = True )
            
        return {
            'input_ids' : input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'], # indicates to the model which tokens are real and which are padding
            'labels': target_encodings['input_ids']
        }
    
    def preprocess_and_save_data(self):
        samsum_dataset = load_from_disk(self.config.data_path)
        samsum_dataset_pt = samsum_dataset.map(self.tokenize_and_prepare_data, batched=True)
        # Save data
        samsum_dataset_pt.save_to_disk(os.path.join(self.config.root_dir, 'samsum_data'))