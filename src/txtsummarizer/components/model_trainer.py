import os
os.environ['http_proxy'] = 'http://proxy1.bgc-jena.mpg.de:3128' 
os.environ['https_proxy'] = 'http://proxy1.bgc-jena.mpg.de:3128'

import torch

from transformers import TrainingArguments, Trainer
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from transformers import DataCollatorForSeq2Seq
from datasets import load_dataset, load_from_disk

from txtsummarizer.entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(
        self,
        config: ModelTrainerConfig
    ):
        self.config = config

    # training func
    def train_and_save_model(self):
        device = 'cuda' if torch.cuda.is_available() else 'cpu'

        tokenizer = AutoTokenizer.from_pretrained(self.config.model_name)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_name).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=model)

        # load the data
        samsum_dataset_pt = load_from_disk(self.config.data_path)

        # Set training args
        training_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=self.config.num_train_epochs, 
            warmup_steps=self.config.warmup_steps,
            per_device_train_batch_size=self.config.per_device_train_batch_size, 
            per_device_eval_batch_size=self.config.per_device_train_batch_size,
            weight_decay=self.config.weight_decay, 
            logging_steps=self.config.logging_steps,
            evaluation_strategy=self.config.evaluation_strategy, 
            eval_steps=self.config.eval_steps, 
            save_steps=1e6,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps,
        )

        trainer = Trainer(
            model=model,
            args=training_args,
            tokenizer=tokenizer,
            data_collator=seq2seq_data_collator,
            train_dataset=samsum_dataset_pt['test'], # TODO: CHANGE TO 'train'
            eval_dataset=samsum_dataset_pt['validation']
        )

        trainer.train()

        # Save the model
        model.save_pretrained(os.path.join(self.config.root_dir, self.config.save_model_name))

        # Save tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, 'tokenizer'))