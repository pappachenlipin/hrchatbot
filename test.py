from src.intentclassification.components.data_ingestion import DataIngestionProcess
from src.intentclassification.components.data_enrichment import DataEnrichmentProcess
from src.intentclassification.components.data_enrichment import DataPreProcess
from src.intentclassification.config.config import config
from src.intentclassification.logging import logging
import pickle

logging.info("Starting the process")

config_obj = config()
print(f"config the {config_obj}")
print("starting the Ingestion process")
data_ingestion = DataIngestionProcess(config_obj.get_data_ingestion_config())
print(f"data ingestion config {data_ingestion}")
data_ingestion.ingest_data()
print("Ending the Ingestion process")
print("starting the Enrich process")
data_enrich = DataEnrichmentProcess(config_obj.get_data_ingestion_config(),config_obj.get_data_enrichment_config())
labelmapping = data_enrich.enrich_data()
labels_file = os.path.join(config_obj.artifacts_root,"labelmapping.pkl")
with open(labels_file, "wb") as f:
    pickle.dump(labelmapping, f)
print("Ending the Enrich process")
print("Starting the preprocessing")
data_preprocess = DataPreProcess(config_obj.get_data_enrichment_config(),config_obj.get_preprocess_config())
tokenized_train, tokenized_test = data_preprocess.preprocessdata()
print("Preprocess Completed")
print("Load the Model")

print("Model Load completed")






