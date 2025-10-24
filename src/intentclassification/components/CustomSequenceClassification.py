from torch import nn
from transformers.modeling_outputs import SequenceClassifierOutput
from transformers import PreTrainedModel


class CustomSequenceClassificationModel(PreTrainedModel):
    def __init__(self, base_model,config,droprate=0.1):
        super().__init__(config)
        self.base_model = base_model
        self.num_labels = config.num_labels
        self.dropout = nn.Dropout(droprate)
        self.classifier = nn.Linear(self.base_model.config.hidden_size, self.num_labels)
        self.post_init()
        
    def forward(self, input_ids=None, attention_mask=None, token_type_ids =None,labels=None, **kwargs):
        output = self.base_model(input_ids,attention_mask,return_dict=True, output_hidden_states = True, output_attentions = True)
        output = self.dropout(output.last_hidden_state[:, 0, :])
        logits = self.classifier(output)
        loss = None
        if labels is not None:
            loss_fn = nn.CrossEntropyLoss()
            loss = loss_fn(logits.view(-1, self.num_labels), labels.view(-1))

        return SequenceClassifierOutput(
            loss=loss,
            logits=logits,
            hidden_states=output.hidden_states,
            attentions=output.attentions
        )
        
    