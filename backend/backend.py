from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os

app = Flask(__name__)
CORS(app)

# Load the trained model and TF-IDF vectorizer
ml_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'machine-learning-model'))
model_path = os.path.join(ml_folder, 'trained_model.pkl')
vectorizer_path = os.path.join(ml_folder, 'tfidf_vectorizer.pkl')

model = joblib.load(model_path)
tfidf_vectorizer = joblib.load(vectorizer_path)

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        # Get the user input (text) from the POST request
        data = request.get_json()
        user_input = data['text']

        # Preprocess the user input (e.g., convert to lowercase)
        user_input = user_input.lower()

        # Vectorize the user input using the loaded TF-IDF vectorizer
        vectorized_input = tfidf_vectorizer.transform([user_input])

        # Make the prediction using the loaded model
        prediction = model.predict(vectorized_input)

        # Return the prediction as a JSON response
        return jsonify({'Prediction': int(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)