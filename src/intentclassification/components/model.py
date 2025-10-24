from transformers import AutoModel, AutoConfig
from torch.nn import Module
from ..entity import DataPreprocess, ModelConfig
from ..logging import logging

class IntentClassificationModel:
    def __init__(self,datapreprocessconfig:DataPreprocess, model_config:ModelConfig):
        self.datapreprocessconfig = datapreprocessconfig
        self.model_config = model_config
    def load_basemodel(self):
        base_model = AutoModel.from_pretrained(self.model_config.basemodel)
        return base_model 
    def load_labels(self):
        labels = []
        with open(self.datapreprocessconfig.labels2id, "rb") as f:
            labels = pickle.load(f)  
        return labels
    def update_basemodel(self, basemodel,labels):
        #Update Model and Config
        updated_config = AutoConfig.from_pretrained(self.model_config.basemodel, id2label = labels[0],label2id =labels[1]  )
        updated_model = my_model(basemodel,updated_config)
        return updated_model
    def freeze_modelparams(self,updated_model):
        for name, param in updated_model.base_model.named_parameters():
            for i, layer in enumerate(hf_model.bert.encoder.layer):
                requires_grad = i >= self.model_config.freezeto
                for param in layer.parameters():
                    param.requires_grad = requires_grad
        return updated_model
    def get_model(self):
        logging.info("Import the Base Model")
        model = self.load_basemodel()
        logging.info("Initialize the labels for the Classification Model")
        labels = self.load_labels()
        logging.info("Update the Base Model with classification head")
        model = self.update_basemodel(model,labels)
        logging.info("Freeze the Base Model parameters")
        model = self.freeze_modelparams(model)
        return model