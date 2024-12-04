import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plts
import spacy
import re
from tqdm import tqdm 


nlp = spacy.load("en_core_web_sm")
dataset = pd.read_csv('dataset/IMDB_Dataset.csv')

X = dataset["review"]
y = dataset["sentiment"]



def rm_char(text):
    text = text.lower()
    text = re.sub(r'<.*?>', '', text) #HTML Tags
    text = re.sub(r'&\w+;', '', text) #HTML Entities
    text = re.sub(r'\d+', '', text) #Chiffres
    text = re.sub(r'\W', ' ', text) #Ponctuation
    text = re.sub(r'\s+', ' ', text).strip() #Espaces en trop
    return text

X_cleaned = X.apply(rm_char)
global i
i = 0


def tokenize_batch(texts):
    global i
    tokens_list = []
    for doc in nlp.pipe(texts, batch_size=1000, disable=["ner","parser"]):
        i += 1
        print(i)
        tokens = [token.lemma_ for token in doc if not token.is_stop]
        tokens_list.append(tokens)
    return tokens_list #lemmatize, tokenize and remove stopwords

print("tokenizing")
X_tokenized = tokenize_batch(X_cleaned)

processed_dataset = pd.DataFrame({
    'review': X_tokenized,
    'sentiment': dataset['sentiment']
})

processed_dataset.to_csv('dataset/Dataset_cleaned.csv',index=False)


print("c bon !")
