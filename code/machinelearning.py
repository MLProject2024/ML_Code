import pandas as pd
import numpy as np
import matplotlib.pyplot as plts
import spacy
import re


nlp = spacy.load("en_core_web_sm")





dataset = pd.read_csv('dataset/IMDB_Dataset.csv')

text = dataset.iloc[0]["review"]


'''def rm_words(text):
    stop_words = stopwords.words('english')
    words = text.split()
    new_text = ''
    for word in words:
        if word not in stop_words:
            new_text += word + ' '
    return new_text'''

def rm_char(text):
    text = text.lower()
    text = re.sub(r'<.*?>', '', text) #HTML Tags
    text = re.sub(r'&\w+;', '', text) #HTML Entities
    text = re.sub(r'\d+', '', text) #Chiffres
    text = re.sub(r'\W', ' ', text) #Ponctuation
    text = re.sub(r'\s+', ' ', text).strip() #Espaces en trop
    return text

def lemmatize(text):
    doc = nlp(text)
    lemmatized_text = ' '.join([token.lemma_ for token in doc if not token.is_stop])
    return lemmatized_text

def clean_text(text):
   return [token.text for token in nlp(lemmatize(rm_char(text)))]

cleaned_text = lemmatize(rm_char(text))
tokens = clean_text(text)

print(cleaned_text + '\n')
print(tokens)
