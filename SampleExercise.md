The exercise below will aim to fulfill the following learning objective:

Lesson 3.2: Applying BERT for Phishing Email Detection

- Learner will be able to load a pre-trained BERT model to use it to extract features from email text data.

Exercise - Context  

You are part of cybersecurity team, aiming to improve your company's email filtering system by identifying phishing attempting using deep learning. The first step is to understand how to extract features from email texts using pre-trained BERT model. These features are vital as they capture the essence of the text data, which can later be used for classification.

Instructions

- Load the pre-trained BERT model <code>bert-base-uncased</code> and its tokensizer <code>BertTokenizer</code> from transformer library.
- Use the tokenizer to process the given <code>sample_email</code> text, convert it into a suitable format.
- Pass the dictionary of tokens through the BERT model <code>**token</code>
- Extract the features <code>last_hidden_state</code> from the model output


```python
# Import necessary libraries
from transformers import BertModel, BertTokenizer
import torch

# Load pre-trained BERT base model and tokenizer
model = BertModel.from_pretrained('____')
tokenizer = ____.from_pretrained('bert-base-uncased')

# sample email text
sample_email = "Dear user, your account has been compromised. Please update your password."

# tokensize the sample email
tokens = tokenizer(____, return_tensors='pt', padding=True, truncation=True, max_length=512) 

# Pass tokenized input through BERT to extract features
with torch.no_grad(): # ensure model is in inference mode
    outputs = model(____)

# Extract the last hidden states (features)
features = outputs.____

# take the mean of all the token embeddings as the email's feature
email_features = features.mean(dim=1)
print(email_features)
```

<code>BertForSequenceClassification</code> can be introduced to classify the text data, further explaining the effectiveness of the model can be improved by fine-tuning it on a labeled dataset of emails text, where it can learn the specific characteristics of phishing vs. legitimate emails.  

Going forward, learners can be encouraged to try out the fine tuned BERT model which was trained on phishing dataset, this model is capable of detecting phishing in its four most common forms: URLs, Emails, SMS messages and websites.

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
tokenizer = AutoTokenizer.from_pretrained("ealvaradob/bert-finetuned-phishing")
model = AutoModelForSequenceClassification.from_pretrained("ealvaradob/bert-finetuned-phishing")
```
Read more on the model: [ealvaradob/bert-finetuned-phishing](https://huggingface.co/ealvaradob/bert-finetuned-phishing#:~:text=Framework%20versions-,BERT%20FINETUNED%20ON%20PHISHING%20DETECTION,Loss%3A%200.1953 "phishing model title")
