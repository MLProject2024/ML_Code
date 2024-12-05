import pandas as pd
import ast
import matplotlib.pyplot as plt
from wordcloud import WordCloud

dataset = pd.read_csv('dataset/Dataset_cleaned.csv')

print("Dataset review update")

dataset["review"] = dataset["review"].apply(ast.literal_eval)

positive_reviews = dataset[dataset["sentiment"] == "positive"]["review"]
negative_reviews = dataset[dataset["sentiment"] == "negative"]["review"]

positive_text = ' '.join([' '.join(review) for review in positive_reviews])

positive_wordcloud = WordCloud(width=800,height=800).generate(positive_text)

plt.figure(figsize=(10, 5))
plt.imshow(positive_wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Positive Review Word Cloud")
plt.show()

negative_text = ' '.join([' '.join(review) for review in negative_reviews])

negative_wordcloud = WordCloud(width=800,height=800).generate(negative_text)

plt.figure(figsize=(10, 5))
plt.imshow(negative_wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Negative Review Word Cloud")
plt.show()