import pandas as pd

dataset = pd.read_csv('dataset/IMDB_Dataset.csv')
print(dataset.shape)
print(dataset.head(10))
print(dataset.describe())