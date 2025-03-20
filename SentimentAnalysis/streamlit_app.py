import streamlit as st
import requests
import json

st.title("Sentiment Analysis App")
st.write("Enter text to analyze its sentiment:")

# Text input from user
user_input = st.text_area("Text to analyze")

# When the user clicks the "Analyze" button
if st.button("Analyze"):
    if user_input:
        try:
            # Send the input text to the backend for analysis
            response = requests.post(
                "http://127.0.0.1:5000/analyze",
                json={"text": user_input}
            )

            # Check if the request was successful
            if response.status_code == 200:
                result = response.json().get("result")
                sentiment = result[0]['label']
                score = result[0]['score']

                # Display the result
                st.success(f"Sentiment: {sentiment}")
                st.write(f"Confidence Score: {score:.2f}")
            else:
                st.error("Error: Could not retrieve results from the backend.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter text to analyze.")
