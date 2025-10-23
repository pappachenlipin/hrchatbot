from datasets import load_from_disk
ds = load_from_disk("artifacts/data_ingestion/test")
print(ds)