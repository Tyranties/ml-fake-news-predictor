import React, { useState } from "react";
import axios from "axios";
import "./App.css";

const App: React.FC = () => {
  const [inputText, setInputText] = useState("");
  const [prediction, setPrediction] = useState<string | null>(null);
  const [loading, setLoading] = useState<boolean>(false);

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setInputText(event.target.value);
  };

  const handlePredict = async () => {
    setLoading(true);
    fetch("https://ml-fake-news-detector-backend.vercel.app/api/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text: inputText }),
    })
      .then((response) => response.json())
      .then((data) => {
        setPrediction(
          data["This article is most likely"] === 1 ? "Fake News" : "True News"
        );
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error:", error);
        setLoading(false);
      });
  };

  return (
    <div className="App">
      <main>
        <h1>Fake News Detector</h1>
        <div className="input-field">
          <input
            type="text"
            value={inputText}
            onChange={handleInputChange}
            placeholder="Enter news title..."
          />
          <button onClick={handlePredict}>Predict</button>
        </div>

        {loading ? (
          <p className="prediction">Loading...</p>
        ) : prediction ? (
          <p
            className={`prediction ${
              prediction === "Real News" ? "true" : "fake"
            }`}
          >
            Prediction: {prediction}
          </p>
        ) : null}
      </main>

      <footer>
        <p>
          Disclaimer: This website is for demonstration purposes only and the
          predictions provided by the fake news detector may not be accurate. It
          should not be used as a reliable source for detecting fake news in
          real-world scenarios. Always verify information from credible sources
          before believing or sharing.
        </p>
      </footer>
    </div>
  );
};

export default App;
