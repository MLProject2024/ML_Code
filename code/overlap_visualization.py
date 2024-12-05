import pandas as pd
import ast
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

dataset = pd.read_csv('dataset/Dataset_cleaned.csv')

print("Dataset review update")

dataset["review"] = dataset["review"].apply(ast.literal_eval)

print("Splitting positive and negative")

positive_reviews = dataset[dataset["sentiment"] == "positive"]["review"]
negative_reviews = dataset[dataset["sentiment"] == "negative"]["review"]

print("Flattening the words")

positive_words = [word for review in positive_reviews for word in review]
negative_words = [word for review in negative_reviews for word in review]

print("Searching overlap words")

positive_word_counts = Counter(positive_words)
negative_word_counts = Counter(negative_words)

overlapping_words = set(positive_word_counts.keys()) & set(negative_word_counts.keys())
overlap_frequencies = { word : (positive_word_counts[word], negative_word_counts[word]) for word in overlapping_words}

print("Visualizing the top overlapping words")


#filtered_words -> dictionary, format : {word:(x,y)}
filtered_words = {
    word: (positive_word_counts[word], negative_word_counts[word]) 
    for word in overlapping_words 
    if positive_word_counts[word] > 1000 and negative_word_counts[word] > 1000
}

positive_freqs = [count[0] for count in filtered_words.values()]
negative_freqs = [count[1] for count in filtered_words.values()]
words = list(filtered_words.keys()) # create a list of the words to show them on the plot
print(len(words))

plt.figure(figsize=(12,8),dpi=300)

for word, x, y in zip(words, positive_freqs, negative_freqs):
    plt.text(x + 10, y + 10, word, fontsize=8, alpha=0.7)

plt.scatter(positive_freqs,negative_freqs,color="purple",alpha=0.7)
plt.xlabel("Positive frequency")
plt.ylabel("Negative frequency")
plt.title("Frequency of overlapping words")
plt.savefig("overlap.png")
plt.show()