import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [quote, setQuote] = useState("");

  const getQuote = async () => {
    const response = await fetch("http://127.0.0.1:5000/quote");
    const data = await response.json();
    setQuote(data.quote);
  };

  useEffect(() => {
    getQuote();
  }, []);

  return (
    <div className="app">
      <h1>Quote of the Day</h1>
      <p>{quote}</p>
      <button onClick={getQuote}>Get New Quote</button>
    </div>
  );
}

export default App;