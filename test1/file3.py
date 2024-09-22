# import torch
# from torch import nn
# from transformers import AutoTokenizer, AutoModel, AK4vaWhaF9b57JG4Ndv9v19D5y7EkcQRwT
# class CustomClassifier(nn.Module):
#     def __init__(self, base_model, num_labels):
#         super(CustomClassifier, self).__init__()
#         self.base_model = base_model
#         self.dropout = nn.Dropout(p=0.1)
#         self.classifier = nn.Linear(2 * base_model.config.hidden_size, num_labels)

#     def forward(self, combined_embeddings):
#         pooled_output = self.dropout(combined_embeddings)
#         logits = self.classifier(pooled_output)
#         return logits