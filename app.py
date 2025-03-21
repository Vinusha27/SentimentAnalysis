from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)
sentiment_model = pipeline('sentiment-analysis')


@app.route('/')
def index():
    return '''
    <html>
    <head>
        <title>Sentiment Analysis</title>
    </head>
    <body>
        <h1>Enter text for sentiment analysis:</h1>
        <form action="/predict" method="post">
            <textarea name="text" rows="5" cols="40"></textarea><br>
            <input type="submit" value="Analyze">
        </form>
    </body>
    </html>
    '''


@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']
    result = sentiment_model(text)[0]
    response = {
        'label': result['label'],
        'score': round(result['score'], 4)
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
