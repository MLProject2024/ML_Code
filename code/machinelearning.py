import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plts
import spacy
import ast
from tqdm import tqdm 


nlp = spacy.load("en_core_web_sm")
dataset = pd.read_csv('dataset/Dataset_cleaned.csv')

dataset["review"] = dataset["review"].apply(ast.literal_eval)

print(dataset["review"][1][1:10])

