import pandas as pd
import ast
import matplotlib.pyplot as plt

print("exporting dataset")
# Import dataset and preprocess reviews
dataset = pd.read_csv('dataset/Dataset_cleaned.csv')
dataset["review"] = dataset["review"].apply(ast.literal_eval)

print("plot")
# Plot sentiment distribution
sentiment_counts = dataset['sentiment'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Sentiment Distribution')
plt.axis('equal')
plt.show()
