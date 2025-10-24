
from ..entity import DataPreprocess, DataEnrichment
from ..logging import logging
from datasets import load_from_disk
from transformers import AutoTokenizer

class DataPreProcess:
    def __init__(self, data_enrichment_config:DataEnrichment, data_preprocess_config:DataPreprocess ):
        self.data_enrichment_config = data_enrichment_config
        self.data_preprocess_config = data_preprocess_config
        self.tokenizer = AutoTokenizer.from_pretrained(self.data_preprocess_config.tokenizer)
    def tokenize_text(batch):
        batched_ds = self.tokenizer(batch["utterance"])
        batched_ds["label"] = batch["label"]
        return batched_ds
    def preprocessdata(self):
        #load the training, testing data from enriched folder
        train_ds = load_from_disk(self.data_enrichment_config.train_root_dir)
        test_ds = load_from_disk(self.data_enrichment_config.test_root_dir)
        #tokenize the text
        tokenized_train_ds = train_ds.map(self.tokenize_text, batched = True)
        tokenized_test_ds = test_ds.map(self.tokenize_text, batched = True)
        #return the labels and tokenized data
        return tokenized_train_ds, tokenized_test_ds
