import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './SentimentForm.css';

const SentimentForm = () => {
  const [text, setText] = useState('');
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);
  const [emoji, setEmoji] = useState(null);
  const [finalEmoji, setFinalEmoji] = useState(null);
  const [fallingMoney, setFallingMoney] = useState(false); // State to trigger falling money

  const handleSubmit = async (e) => {
    e.preventDefault();
    setResult(null);
    setError(null);
    setFinalEmoji(null);
    setLoading(true);

    try {
      const response = await axios.post('http://localhost:5000/predict-sentiment', { text });
      const sentiment = response.data.sentiment;

      // Start the gambling animation
      let toggle = true;
      const interval = setInterval(() => {
        setEmoji(toggle ? 'cool' : 'not_cool');
        toggle = !toggle;
      }, 150); // Switch emoji every 150ms

      // Stop the animation after 3 seconds and show the final emoji
      setTimeout(() => {
        clearInterval(interval);
        setEmoji(null);
        setFinalEmoji(sentiment.toLowerCase() === 'positive' ? 'cool' : 'not_cool'); // Show correct emoji
        setResult(sentiment);
        setLoading(false);

        if (sentiment.toLowerCase() === 'positive') {
          setFallingMoney(true); // Trigger falling money animation if sentiment is positive
          setTimeout(() => {
            setFallingMoney(false); // Stop falling money after 3 seconds
          }, 7000);
        }
      }, 3000);
    } catch (err) {
      setError(err.response?.data?.error || 'An error occurred');
      setLoading(false);
    }
  };

  // Function to create falling money elements dynamically
  const createFallingMoney = () => {
    const moneyArray = [];
    for (let i = 0; i < 50; i++) { // Number of money images
      const leftPosition = Math.random() * 100; // Random horizontal position (0% to 100%)
      const delay = Math.random() * 2; // Random delay for staggered falling effect
      moneyArray.push(
        <div
          key={i}
          className="falling-money"
          style={{
            left: `${leftPosition}%`, // Random horizontal position
            animationDelay: `${delay}s` // Random delay for each item
          }}
        >
          💰
        </div>
      );
    }
    return moneyArray;
  };

  return (
    <div className={`app-container ${loading ? 'suspense' : ''}`}>
      <h1>Sentiment Analysis</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Enter text to analyze..."
          style={{ width: '100%', height: '100px', marginBottom: '10px' }}
        />
        <button type="submit" disabled={loading}>
          {loading ? 'Analyzing...' : 'Analyze Sentiment'}
        </button>
      </form>
      {result && <p><strong>Sentiment:</strong> {result}</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}

      {/* Gambling Emoji Animation */}
      {emoji && (
        <img
          src={`/${emoji}.png`}
          alt="Gambling Emoji"
          className="gambling-emoji"
        />
      )}

      {/* Final Emoji */}
      {finalEmoji && (
        <img
          src={`/${finalEmoji}.png`}
          alt="Final Emoji"
          className="pop-out-emoji"
        />
      )}

      {/* Falling Money Triggered for Positive Sentiment */}
      {fallingMoney && (
        <div className="falling-money-container">
          {createFallingMoney()} {/* Creates falling money elements */}
        </div>
      )}
    </div>
  );
};

export default SentimentForm;
