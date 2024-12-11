# preprocess.py
import spacy
import re
import pandas as pd

nlp = spacy.load("en_core_web_sm")

# Function to clean the input text
def rm_char(text):
    text = text.lower()
    text = re.sub(r'<.*?>', '', text)  # Remove HTML Tags
    text = re.sub(r'&\w+;', '', text)  # Remove HTML Entities
    text = re.sub(r'\d+', '', text)  # Remove digits
    text = re.sub(r'\W', ' ', text)  # Remove punctuation
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra spaces
    return text

# Function to tokenize the input text (remove stopwords and lemmatize)
def preprocess_review(user_review):
    cleaned_review = rm_char(user_review)
    doc = nlp(cleaned_review)
    return [token.lemma_ for token in doc if not token.is_stop]  # Lemmatize and remove stopwords


choosing = True
while(choosing == True):
    if int(input("Voulez vous ajouter une review (1 - oui \n 2 - non )")) == 2:
        choosing = False
    else:
        print(preprocess_review(input("Votre review : ")))