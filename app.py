import streamlit as st
import joblib

# Load the model and vectorizer
model = joblib.load('curse_123.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Streamlit app title
st.title('Cyberbullying Detection')

# Input text box for user to enter a comment
user_input = st.text_area("Enter a comment to analyze:")

# Preprocess and predict when button is clicked
if st.button("Predict"):
    if user_input:
        # Preprocess and vectorize the input
        processed_input = vectorizer.transform([user_input])
        prediction = model.predict(processed_input)[0]  # Get the predicted label

        # Debugging: Print the raw prediction
        st.write(f"Raw Prediction: {prediction}")

        # Assuming these are the classes used during training
        labels = ['None', 'Insult', 'Threat', 'Hate Speech', 'Other']

        # Map the prediction to the corresponding label
        if isinstance(prediction, int):
            result = labels[prediction] if 0 <= prediction < len(labels) else "Unknown"
            st.write(f"Prediction: {result}")
        else:
            st.write(f"Prediction: {prediction}")
    else:
        st.write("Please enter a comment to analyze.")
