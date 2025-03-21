from transformers import pipeline

# Load the pre-trained sentiment analysis model
classifier = pipeline("sentiment-analysis")

# Sample text to analyze
sample_text = "I love this product. It's amazing!"

# Make prediction
result = classifier(sample_text)

# Print the result
print(f"Text: {sample_text}")
print(f"Sentiment: {result[0]['label']}, Score: {result[0]['score']}")
