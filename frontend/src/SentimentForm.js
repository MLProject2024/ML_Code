import React, { useState } from 'react';
import axios from 'axios';
import confetti from 'canvas-confetti';
import './SentimentForm.css';

const SentimentForm = () => {
  const [text, setText] = useState('');
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);
  const [emoji, setEmoji] = useState(null);
  const [finalEmoji, setFinalEmoji] = useState(null);
  const [fallingMoney, setFallingMoney] = useState(false); // State to trigger falling money

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

  const launchConfetti = ()=>{
    confetti({
      particleCount: 100, // Nombre de particules
      spread: 70, // Angle de dispersion
      origin: { x: 0.5, y: 0.5 }, // Position centrale
      zIndex: 2000, // S'assurer qu'il est visible
    })
  }

  const symbols = ['✨', '🔥', '💥', '💫', '🌟']; // Symboles cartoonesques

  const renderSymbols = (popout = false) => {
    const symbolElements = [];
    const totalSymbols = 16;
    const radius = 350;
    for (let i = 0; i < totalSymbols; i++) {
      const angle = (i * (360 / totalSymbols)) * (Math.PI / 180); // Convert degrees to radians
      const x = Math.cos(angle) * radius - 25; // X position
      const y = Math.sin(angle) * radius - 200; // Y position
      const randomSymbol = symbols[Math.floor(Math.random() * symbols.length)];

      symbolElements.push(
        <span
          key={i}
          className="symbol"
          style={{
            '--x': `${x}px`,
            '--y': `${y}px`,
            animationDelay: popout ? '0s' : `${i * 0.1}s`,
          }}
        >
          {randomSymbol}
        </span>
      );
    }
    return symbolElements;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setResult(null);
    setError(null);
    setFinalEmoji(null);
    setLoading(true);

    try {
      console.log("send the request");
      const response = await axios.post('http://localhost:5000/predict-sentiment', { text });
      console.log("got the sentiment");
      const sentiment = response.data.sentiment;
      console.log("in sentimentForm.js: l85");
      // Start the gambling animation
      let toggle = true;
      const interval = setInterval(() => {
        setEmoji(toggle ? 'cool' : 'not_cool');
        toggle = !toggle;
      }, 150); // Switch emoji every 150ms
      console.log("after gambling");
      // Stop the animation after 3 seconds and show the final emoji
      setTimeout(() => {
        clearInterval(interval);
        setEmoji(null);
        setFinalEmoji(sentiment.toLowerCase() === 'positive' ? 'cool' : 'not_cool'); // Show correct emoji
        setResult(sentiment);
        setLoading(false);

        if (sentiment.toLowerCase() === 'positive') {
          launchConfetti();
          setFallingMoney(true);
          setTimeout(() => {
            setFallingMoney(false); 
          }, 7000);
        }
      }, 2000);
    } catch (err) {
      setError(err.response?.data?.error || 'An error occurred');
      setLoading(false);
    }
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
        <div className="symbol-container">
          <img
            src={`/${emoji}.png`}
            alt="Gambling Emoji"
            className="gambling-emoji"
          />
          {renderSymbols()}
        </div>
      )}
      {/* Final Emoji */}
      {finalEmoji && (
        <div classname="symbol-container">
        <img
          src={`/${finalEmoji}.png`}
          alt="Final Emoji"
          className="pop-out-emoji"
        />
        {renderSymbols(true)}
        </div>
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
