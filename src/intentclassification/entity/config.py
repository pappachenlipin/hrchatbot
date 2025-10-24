from dataclasses import dataclass

@dataclass
class DataIngestion:
    root_dir:str
    train_ds:str
    test_ds:str
    train_root_dir:str
    test_root_dir:str

@dataclass
class DataEnrichment:
    root_dir:str
    train_root_dir:str
    test_root_dir:str
@dataclass
class DataPreprocess:
    root_dir:str
    tokenizer:str
    labels2id:str
@dataclass
class ModelConfig:
    basemodel:str
    freezeto:int
@dataclass
class TrainingConfig:
    output_dir: str
    checkpoints_dir: str
    per_device_train_batch_size: int
    learning_rate: float
    num_train_epochs: int
    save_strategy: str
    logging_strategy: str
    evaluation_strategy: str
    load_best_model_at_end: bool
    report_to: list
    early_stopping_patience: int
        