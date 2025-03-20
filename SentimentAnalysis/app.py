from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)

sentiment_analyzer = pipeline("sentiment-analysis")

@app.route('/')
def home():
    return "Backend is working!"

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.json  # Get the JSON data sent by the frontend
        text = data.get('text')  # Extract the text input

        if not text:
            return jsonify({"error": "No text provided"}), 400  # Error if text is missing

        # Perform sentiment analysis
        result = sentiment_analyzer(text)
        return jsonify({"result": result})  # Send result as JSON response

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Error handling

if __name__ == "__main__":
    app.run(debug=True)
