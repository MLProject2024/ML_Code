import pandas as pd
import numpy as np
import matplotlib.pyplot as plts
from nltk.corpus import stopwords
import re






dataset = pd.read_csv('dataset/IMDB_Dataset.csv')

text = dataset.iloc[0]["review"]


def rm_words(text):
    stop_words = stopwords.words('english')
    words = text.split()
    new_text = ''
    for word in words:
        if word not in stop_words:
            new_text += word + ' '
    return new_text

def rm_char(text):
    text = text.lower()
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

print(rm_char(rm_words(text)))
