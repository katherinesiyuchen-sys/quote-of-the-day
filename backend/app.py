from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "In the middle of every difficulty lies opportunity. - Einstein",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
]

@app.route("/")
def home():
    return jsonify({"quote": random.choice(quotes)})

@app.route("/quote")
def quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == "__main__":
    app.run(debug=True)
