# Sentiment Analysis Web Application

## Setup and Installation

### Python Backend

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

2. Install dependencies:
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

3. Train the model (if not already trained):
```bash
python preprocessing.py
python SVM.py
```

4. Save the trained model:
```bash
import joblib
joblib.dump(grid_search.best_estimator_, 'svm_model.joblib')
```

### React Frontend Setup

1. Install Node.js dependencies:
```bash
npm install
```

2. Create a backend API endpoint:
You'll need to create a backend service (Flask/FastAPI/Django) that:
- Loads the saved SVM model
- Provides a `/predict-sentiment` endpoint
- Preprocesses the input text
- Returns the sentiment prediction

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
1. Start the backend server
2. Start the React frontend
3. Enter a movie review and get its sentiment prediction
