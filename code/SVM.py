from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC  # Use LinearSVC instead of SVC
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import classification_report
import pandas as pd
import ast
import joblib

# Read the dataset
dataset = pd.read_csv('dataset/Dataset_cleaned.csv')

# Preprocess the reviews (Assuming they are lists)
dataset['review'] = dataset['review'].apply(ast.literal_eval)

# Define features and labels
texts = dataset["review"]
labels = dataset["sentiment"]

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

def identity_tokenizer(tokens):
    # Tokenize and remove tokens that are too short
    return [token for token in tokens if len(token) > 2]

print("Pipeline")

# Pipeline with TF-IDF and Linear SVC (faster than rbf SVC)
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(tokenizer=identity_tokenizer, token_pattern=None, lowercase=False, max_features=5000)), 
    ('svm', LinearSVC(C=0.225))  # LinearSVC instead of SVC with rbf
])

print("Grid Search")    

# Define the parameter grid (reduce it for faster search)
param_grid = {
    'tfidf__max_features': [50000],  # Limit max_features for faster testing
    'svm__C': [0.225],  # Test a range of values for C
}

# GridSearchCV with parallelization (use all CPU cores)
grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='accuracy', verbose=3, n_jobs=3)
grid_search.fit(X_train, y_train)

# Print best parameters and validation accuracy
print("Meilleurs paramètres :", grid_search.best_params_)
print("Meilleure précision (validation) :", grid_search.best_score_)

# Final evaluation on the test set
y_pred = grid_search.best_estimator_.predict(X_test)
print(classification_report(y_test, y_pred))

joblib.dump(grid_search.best_estimator_, 'sentiment_analysis_model.joblib')
print("Success")
