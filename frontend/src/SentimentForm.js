import React, { useState } from 'react';
import axios from 'axios';
import './SentimentForm.css'; // Create this CSS file for animations

const SentimentForm = () => {
  const [text, setText] = useState('');
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const [showEmoji, setShowEmoji] = useState(false); // Controls emoji visibility

  const handleSubmit = async (e) => {
    e.preventDefault();
    setResult(null);
    setError(null);
    setShowEmojiPositive(false); // Reset emoji state
    setShowEmoji

    try {
      const response = await axios.post('http://localhost:5000/predict-sentiment', { text });
      const sentiment = response.data.sentiment;

      setResult(sentiment);

      if (sentiment.toLowerCase() === 'positive') {
        setShowEmoji(true); // Show emoji for positive sentiment
        setTimeout(() => setShowEmoji(false), 3000); // Hide after 3 seconds
      }
      else if(sentiment.toLowerCase() === 'negative'){
        setEm
      }
    } catch (err) {
      setError(err.response?.data?.error || 'An error occurred');
    }
  };

  return (
    <div style={{ maxWidth: '500px', margin: '0 auto', padding: '20px' }}>
      <h1>Sentiment Analysis</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Enter text to analyze..."
          style={{ width: '100%', height: '100px', marginBottom: '10px' }}
        />
        <button type="submit">Analyze Sentiment</button>
      </form>
      {result && <p><strong>Sentiment:</strong> {result}</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}

      {/* Pop-out Emoji */}
      {showEmoji && (
        <img
          src="/cool.png"
          alt="Positive Sentiment"
          className="pop-out-emoji"
        />
      )}
    </div>
  );
};

export default SentimentForm;
