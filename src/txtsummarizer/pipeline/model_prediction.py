import os
os.environ['http_proxy'] = 'http://proxy1.bgc-jena.mpg.de:3128' 
os.environ['https_proxy'] = 'http://proxy1.bgc-jena.mpg.de:3128'

from txtsummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline


class ModelPredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config() # since, this has model and tokenizer path

    def predict(self, txt):
        # Load tokenizer
        tokenizer =  AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}

        pipln = pipeline('summarization', model=self.config.model_path, tokenizer=tokenizer)

        print('Input Text:')
        print(txt)

        out_summary = pipln(txt, **gen_kwargs)[0]["summary_text"]

        print("\nModel Summary:")
        print(out_summary)

        return out_summary
