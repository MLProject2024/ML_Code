## Model Details
- Dataset: IMDB Movie Reviews
- Preprocessing: 
  - Lowercase conversion
  - HTML tag removal
  - Punctuation removal
  - Lemmatization
  - Stopword removal
- Vectorization: TF-IDF
- Classifier: Linear SVM

## Usage
1. Start the backend server (in /backend : python script.py)
2. Start the React frontend (in /frontend : npm start)
3. Enter a movie review and get its sentiment prediction
 
 ### To start MLflow:
 1. Command 'mlflow ui' in a Terminal
 2. Mlflow launched in http://localhost:5000