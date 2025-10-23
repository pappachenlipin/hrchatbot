from src.intentclassification.components.data_ingestion import Data_IngestionProcess
from src.intentclassification.config.config import config
from src.intentclassification.logging import logging


logging.info("Starting the process")
print("starting the process")
config_obj = config()
print(f"config the {config_obj}")
data_ingestion = Data_IngestionProcess(config_obj.get_data_ingestion_config())
print(f"data ingestion config {data_ingestion}")
data_ingestion.ingest_data()



