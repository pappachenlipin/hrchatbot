from ..utils import read_yamlfile
from ..constant import config_file_path
from ..entity import DataIngestion, DataEnrichment, DataPreprocess, ModelConfig, TrainingConfig

class config:
    def __init__(self):
        self.config = read_yamlfile(config_file_path)
    def get_data_ingestion_config(self)->DataIngestion:
        data_ingestion_config = self.config.data_ingestion
        data_ingestion_config = DataIngestion(
            root_dir = data_ingestion_config.root_dir,
            train_ds = data_ingestion_config.train_ds,
            test_ds = data_ingestion_config.test_ds,
            train_root_dir = data_ingestion_config.train_root_dir,
            test_root_dir = data_ingestion_config.test_root_dir
        )
        return data_ingestion_config
    def get_data_enrichment_config(self)->DataEnrichment:
        data_enrichment_config = self.config.data_enrichment
        data_enrichment_config = DataEnrichment(
            root_dir = data_enrichment_config.root_dir,
            train_root_dir = data_enrichment_config.train_root_dir,
            test_root_dir = data_enrichment_config.test_root_dir
        )
        return data_enrichment_config
    def get_preprocess_config(self)->DataPreprocess:
        data_preprocess_config = self.config.data_preprocess
        data_preprocess_config = DataPreprocess(
            root_dir = data_preprocess_config.root_dir,
            tokenizer = data_preprocess_config.tokenizer,
            labels2id = data_preprocess_config.labels2id

        )
        return data_preprocess_config
    def get_model_config(self)->ModelConfig:
        model_config = self.config.model
        model_config = ModelConfig(
            basemodel = model_config.basemodel,
            freezeto = model_config.freezeto
                )
        return model_config
    def get_training_config(self)->TrainingConfig:
        training_config = self.config.training
        training_config = TrainingConfig(
            output_dir: training_config.output_dir,
            checkpoints_dir: training_config.checkpoints_dir,
            per_device_train_batch_size: training_config.per_device_train_batch_size,
            learning_rate: training_confignum_train_epochs,
            num_train_epochs: training_config.num_train_epochs,
            save_strategy: training_config.save_strategy,
            logging_strategy: training_config.logging_strategy,
            evaluation_strategy: training_config.evaluation_strategy,
            load_best_model_at_end: training_config.load_best_model_at_end,
            report_to: training_config.report_to,
            early_stopping_patience: training_config.early_stopping_patience

            
        )
        return training_config


    

    




