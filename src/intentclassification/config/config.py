from ..utils import read_yamlfile
from ..constant import config_file_path
from ..entity.config import Data_Ingestion

class config:
    def __init__(self):
        self.config = read_yamlfile(config_file_path)
    def get_data_ingestion_config(self)->Data_Ingestion:
        data_ingestion_config = self.config.data_ingestion
        data_ingestion_config = Data_Ingestion(
            root_dir = data_ingestion_config.root_dir,
            train_ds = data_ingestion_config.train_ds,
            test_ds = data_ingestion_config.test_ds,
            train_root_dir = data_ingestion_config.train_root_dir,
            test_root_dir = data_ingestion_config.test_root_dir
        )
        return data_ingestion_config
    




