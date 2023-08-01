import joblib

# Load the trained model
model = joblib.load('trained_model.pkl')
# Load the TF-IDF vectorizer (if you saved it during training)
tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')

def main():
    while True:
        input_title = input()
        input_title = input_title.lower()

        vectorized_title = tfidf_vectorizer.transform([input_title])
        prediction = model.predict(vectorized_title)

        # Map the prediction to its label
        if prediction[0] == 1:
            print("The title is likely true news.")
        else:
            print("The title is likely fake news.")

if __name__ == "__main__":
    main()