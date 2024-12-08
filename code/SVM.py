from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import classification_report
import pandas as pd


dataset = pd.read_csv('dataset/Dataset_cleaned.csv', nrows=20000)


# Texte et labels
texts = dataset["review"]
labels = dataset["sentiment"]

# Division des données
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

# Pipeline TF-IDF + SVM
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=5000)),  # Conversion en vecteurs TF-IDF
    ('svm', SVC(kernel='rbf'))  # SVM with rbf
])


# Recherche des hyperparamètres
param_grid = {
    'tfidf__max_features': [15000],  # Nombre de mots considérés
    'svm__C': [0.83],  # Valeurs de C
}
grid_search = GridSearchCV(pipeline, param_grid, cv=10, scoring='accuracy')
grid_search.fit(X_train, y_train)

# Meilleurs paramètres et évaluation
print("Meilleurs paramètres :", grid_search.best_params_)
print("Meilleure précision (validation) :", grid_search.best_score_)

# Évaluation finale sur le test set
y_pred = grid_search.best_estimator_.predict(X_test)
print(classification_report(y_test, y_pred))

