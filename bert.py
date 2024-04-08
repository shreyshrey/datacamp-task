# Import necessary libraries
from transformers import BertModel, BertTokenizer
import torch

# Load pre-trained BERT base model and tokenizer
model = BertModel.from_pretrained('bert-base-uncased')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# sample email text
sample_email = "Dear user, your account has been compromised. Please update your password."

# tokensize the sample email
tokens = tokenizer(sample_email, return_tensors='pt', padding=True, truncation=True, max_length=512) 

# Pass tokenized input through BERT to extract features
with torch.no_grad(): # ensure model is in inference mode
    outputs = model(**tokens)

# Extract the last hidden states (features)
features = outputs.last_hidden_state

# take the mean of all the token embeddings as the email's feature

email_features = features.mean(dim=1)
print(email_features)