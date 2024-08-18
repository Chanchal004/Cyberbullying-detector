
# Cyberbullying Detection Using NLP

This project is a web application that detects cyberbullying in user comments. It uses Natural Language Processing (NLP) techniques to classify comments into categories such as hate speech, insults, threats, and other harmful language. The model is trained on labeled text data to identify and flag inappropriate content.

## Features

- **Text Input**: Users can input comments to be analyzed.
- **Prediction**: The application predicts the nature of the comment, indicating if it contains hate speech, insults, threats, or is benign.
- **Streamlit Interface**: The app uses Streamlit for a user-friendly web interface.

## How It Works

1. **Text Preprocessing**: The input comment is vectorized using `TfidfVectorizer` to convert it into numerical features.
2. **Model Prediction**: A trained machine learning model predicts the category of the comment based on the processed features.
3. **Result Display**: The predicted category is displayed to the user.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/cyberbullying-detection.git
   ```

2. Navigate to the project directory:

   ```bash
   cd cyberbullying-detection
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   streamlit run app.py
   ```

## Files

- **`app.py`**: The main application file containing the Streamlit interface and prediction logic.
- **`curse_123.pkl`**: The pre-trained machine learning model for cyberbullying detection.
- **`tfidf_vectorizer.pkl`**: The TF-IDF vectorizer used for text preprocessing.
- **`requirements.txt`**: The list of required Python packages.

## Usage

1. Run the application using Streamlit.
2. Enter a comment in the provided text box.
3. Click "Predict" to analyze the comment and get a prediction on its nature.

## Example

- Input: "You're amazing just the way you are!"
- Prediction: "not cyberbullying"

- Input: "Go kill yourself, the world would be better without you."
- Prediction: "other_cyber biullying"
- 
![Screenshot (25)](https://github.com/user-attachments/assets/9917df67-9f9b-474f-9e1d-5a6aa7c7e1b6)

![Screenshot (26)](https://github.com/user-attachments/assets/bc704304-87e8-4401-a09b-ec093013f46f)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
