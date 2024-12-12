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
1. Run an Docker image
2. Start the React frontend (in /frontend : npm start)
3. Go to localhost:3000
4. Enter a movie review and get its sentiment prediction

 
 ### To start MLflow:
 1. Command 'mlflow ui' in a Terminal
 2. Mlflow launched in http://localhost:5000

IMPORTANT: MLFLOW IS RAN ON PORT 5000, YOU CAN'T RUN MLFLOW WITH THE BACKEND (on port 5000 too)
