from flask import Flask, jsonify
from quotes import get_random_quote

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Inspire API. Hit /api/quote for your daily dose of inspiration!"

@app.route("/api/quote")
def quote():
    return jsonify({"quote": get_random_quote()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
