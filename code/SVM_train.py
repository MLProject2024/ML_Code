from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC  # Use LinearSVC instead of SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import pandas as pd
import ast
import joblib

import mlflow
import mlflow.sklearn

# mlflow configuration of logs
mlflow.set_tracking_uri("mlruns")
mlflow.set_experiment("ML_Code-1")
from mlflow.models.signature import infer_signature

# Read the dataset
dataset = pd.read_csv('dataset/Dataset_cleaned.csv', nrows=50000)

# Preprocess the reviews (Assuming they are lists)
dataset['review'] = dataset['review'].apply(ast.literal_eval)

# Define features and labels
texts = dataset["review"]
labels = dataset["sentiment"]
test_size_ = 0.0
for i in range(4):
    test_size_ += 0.1
    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=test_size_, random_state=42)

    def identity_tokenizer(tokens):
        # Tokenize and remove tokens that are too short
        return [token for token in tokens if len(token) > 2]


    """
    # best known: c = 0.225
    var_c = 5

    # Pipeline with TF-IDF and Linear SVC (faster than rbf SVC)
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(tokenizer=identity_tokenizer, token_pattern=None, lowercase=False, max_features=50000)), 
        ('svm', LinearSVC(C=var_c))  # LinearSVC instead of SVC with rbf
    ])

    pipeline.fit(X_train, y_train)

    # Final evaluation on the test set
    y_pred = pipeline.predict(X_test)
    print(classification_report(y_test, y_pred))
    """
    var_c = 0
    for i in range (15):
        # best known: c = 0.375
        var_c = var_c + 0.075
        name = "SVC_" + str(test_size_) 

        # Pipeline with TF-IDF and Linear SVC (faster than rbf SVC)
        pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(tokenizer=identity_tokenizer, token_pattern=None, lowercase=False, max_features=50000)), 
            ('svm', LinearSVC(C=var_c))  # LinearSVC instead of SVC with rbf
        ])

        pipeline.fit(X_train, y_train)

        # Final evaluation on the test set
        y_pred = pipeline.predict(X_test)
        # ml flow log save
        with mlflow.start_run(run_name=name):
            mlflow.log_param("test_size", test_size_)
            mlflow.log_param("model_type", "LinearSVC")

            # log param and metric
            accuracy = accuracy_score(y_test, y_pred)
            accuracy = accuracy_score(y_test, y_pred)
            mlflow.log_metric("accuracy", accuracy)
            mlflow.log_metric("accuracy", accuracy)
            mlflow.log_param("Margin c", var_c)

            mlflow.sklearn.log_model(pipeline, "model")

            print(f"Run ID: {mlflow.active_run().info.run_id}")

            print(f"Accuracy: {accuracy}")
            print("Model and metrics logged with MLflow!")

print("fin de mlflow")
"""
joblib.dump(pipeline, 'public/model/sentiment_analysis_model.joblib')
print("Model saved!")
"""

"""
test = pd.read_csv('dataset/test.csv')

test['review'] = test['review'].apply(ast.literal_eval)

print(test['review'])
print(test['sentiment'])
prediction = pipeline.predict(test['review'])
print(prediction)
"""