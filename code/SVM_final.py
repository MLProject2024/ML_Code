from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC  # Use LinearSVC instead of SVC
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import classification_report
import pandas as pd
import ast

# Read the dataset
dataset = pd.read_csv('dataset/Dataset_cleaned.csv', nrows=50000)

# Preprocess the reviews (Assuming they are lists)
dataset['review'] = dataset['review'].apply(ast.literal_eval)

# Define features and labels
texts = dataset["review"]
labels = dataset["sentiment"]





# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

print(X_test)

def identity_tokenizer(tokens):
    # Tokenize and remove tokens that are too short
    return [token for token in tokens if len(token) > 2]

print("Pipeline")

# Pipeline with TF-IDF and Linear SVC (faster than rbf SVC)
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(tokenizer=identity_tokenizer, token_pattern=None, lowercase=False, max_features=50000)), 
    ('svm', LinearSVC(C=0.225))  # LinearSVC instead of SVC with rbf
])

pipeline.fit(X_train, y_train)

# Final evaluation on the test set
y_pred = pipeline.predict(X_test)
print(classification_report(y_test, y_pred))

test = pd.read_csv('dataset/test.csv')

test['review'] = test['review'].apply(ast.literal_eval)

print(test['review'])
print(test['sentiment'])
prediction = pipeline.predict(test['review'])
print(prediction)