from ..logging import logging
from datasets import load_dataset
import pickle,os

class Data_IngestionProcess:
    def __init__(self, config):
        self.config = config
    def ingest_data(self):
        #create the ingestion directory
        os.makedirs(self.config.root_dir, exist_ok = True)
        #load the train, evaluation dataset
        train_ds = load_dataset(self.config.train_ds)
        test_ds = load_dataset(self.config.test_ds)
        #save the train_dataset to directory
        train_ds.save_to_disk(self.config.train_root_dir)
        test_ds.save_to_disk(self.config.test_root_dir)


    
