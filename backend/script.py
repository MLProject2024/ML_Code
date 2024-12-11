import joblib
import re
import spacy
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


# Load preprocessing functions
def rm_char(text):
    text = text.lower()
    text = re.sub(r'<.*?>', '', text) #HTML Tags
    text = re.sub(r'&\w+;', '', text) #HTML Entities
    text = re.sub(r'\d+', '', text) #Chiffres
    text = re.sub(r'\W', ' ', text) #Ponctuation
    text = re.sub(r'\s+', ' ', text).strip() #Espaces en trop
    return text

def identity_tokenizer(tokens):
    # This function must match exactly how it was defined when training
    return [token for token in tokens if len(token) > 2]

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    # Clean the text
    cleaned_text = rm_char(text)
    
    # Tokenize, lemmatize, and remove stopwords
    doc = nlp(cleaned_text)
    tokens = [token.lemma_ for token in doc if not token.is_stop and len(token.lemma_) > 2]
    
    return tokens

# Load the pre-trained model
try:
    model = joblib.load('model/sentiment_analysis_model.joblib')
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

@app.route('/predict-sentiment', methods=['POST'])
def predict_sentiment():
    # Check if model is loaded
    if model is None:
        return jsonify({'error': 'Model not loaded'}), 500
    
    # Get data from request
    data = request.json
    
    # Validate input
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    
    # Preprocess the input text
    try:
        preprocessed_text = preprocess_text(data['text'])
        
        # Predict sentiment
        sentiment = model.predict([preprocessed_text])[0]
        
        return jsonify({'sentiment': sentiment})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# For local testing
@app.route('/', methods=['GET'])
def home():
    return "Sentiment Analysis Backend is running!"

if __name__ == '__main__':
    app.run(debug=True, port=5000)