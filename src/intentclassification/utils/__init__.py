import yaml
from box import ConfigBox
def read_yamlfile(file_path)->ConfigBox:
    """
    reads the yaml file
    args: file_path: path to the config file
    returns the contents in configbox"""
    with open(file_path, "rb") as f:
        data = yaml.safe_load(f)
    return ConfigBox(data)
    
