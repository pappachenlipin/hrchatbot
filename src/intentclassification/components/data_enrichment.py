from ..logging import logging
from datasets import load_from_disk
from ..entity import DataIngestion, DataEnrichment
from datasets import Dataset
import re, os, pickle
import ast


class DataEnrichmentProcess:
    def __init__(self,ingestion_config:Data_Ingestion, enrich_config:Data_Enrichment):
        self.ingestion_config = ingestion_config
        self.enrich_config = enrich_config
    def _load_file(self):
        #load raw data
        train_ds = load_from_disk(self.ingestion_config.train_root_dir)["train"]
        test_ds = load_from_disk(self.ingestion_config.test_root_dir)["test"]
        train_ds =train_ds.map(lambda x: {"utterance": ast.literal_eval(x["utterance"]),
                                        "service_list": ast.literal_eval(x["service"])[0]})
        return train_ds, test_ds
    def _getuniquelables(self, train_ds):
        labels = sorted(set(train_ds['service_list']))
        id2label = {id:value for id, value in enumerate(labels)}
        label2id = {value:id for id, value in enumerate(labels)}
        return id2label, label2id
    def _preprocesstraindata(self, train_ds,label2id):
        processed_batch = {}
        processed_batch["utterance"]=[]
        processed_batch["label"] = []
        for cur, items in enumerate(train_ds['utterance']):
            label = train_ds['service_list'][cur]
            for index in range(1,len(items), 2):
                match = re.search(r"Employee:\s*(.*)", items[index])
                if match:
                    processed_batch["utterance"].append(match.group(1))
                    processed_batch["label"].append(label2id[label])
        
        return Dataset.from_dict(processed_batch)
    def _preprocesstestdata(self, test_ds,label2id):
        test_ds = test_ds.map(lambda x: {"label": label2id[x["label"]]}, remove_columns = ['Unnamed: 0'])
        return test_ds
    def enrich_data(self):
        #create the ingestion directory
        os.makedirs(self.enrich_config.root_dir, exist_ok = True)
        #load the datasets
        train_ds, test_ds = self._load_file()
        #get unique lables
        id2label, label2id = self._getuniquelables(train_ds)
        #preprocess the training/testing data
        train_ds = self._preprocesstraindata(train_ds, label2id)
        test_ds = self._preprocesstestdata(test_ds,label2id )
        #save the clean data
        train_ds.save_to_disk(self.enrich_config.train_root_dir)
        test_ds.save_to_disk(self.enrich_config.test_root_dir)
        label_mapping = {
            "label2id" : label2id,
            "id2label" : id2label
        }
       return label_mapping

    




