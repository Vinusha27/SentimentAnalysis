from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import make_pipeline
import joblib

# Sample data (replace with your dataset)
data = [("I love this product!", 1), ("This is terrible.", 0)]
X_train = [x[0] for x in data]
y_train = [x[1] for x in data]

# Create a pipeline with CountVectorizer and Naive Bayes
model = make_pipeline(CountVectorizer(), MultinomialNB())

# Train the model
model.fit(X_train, y_train)

# Save the model to a file for deployment
joblib.dump(model, 'sentiment_model.pkl')

print("Model training complete and saved to sentiment_model.pkl")
