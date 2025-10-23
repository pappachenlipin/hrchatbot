from dataclasses import dataclass

@dataclass
class Data_Ingestion:
    root_dir:str
    train_ds:str
    test_ds:str
    train_root_dir:str
    test_root_dir:str
    