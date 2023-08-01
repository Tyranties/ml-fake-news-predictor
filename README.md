# Fake News Predictor Web Application

This project is a web application that uses machine learning to detect whether a given news article title is fake or not. The application consists of two main parts: the frontend and the backend.

## Frontend

The frontend of the application is built using React and TypeScript. It allows users to input a news article title and sends it to the backend API for prediction. The prediction result (whether the article is likely fake or true) is then displayed to the user.

### Setup

To run the frontend locally, follow these steps:

1. Make sure you have Node.js and npm installed on your machine.

2. Clone this repository and navigate to the frontend directory.

3. Install the required dependencies by running:

```bash
npm install
```

4. Start the development server by running:

```bash
npm start
```
This will launch the app at http://localhost:3000 in your web browser.

### Deployed Version
The frontend of this application is deployed using Vercel and can be accessed at https://ml-fake-news-detector.vercel.app/.

## Backend
The backend of the application is built using Python and Flask. It hosts a machine learning model trained to predict whether a news article title is fake or true.
### Setup
To run the backend locally, follow these steps:

1. Make sure you have Python and pip installed on your machine.

2. Clone this repository and navigate to the backend directory.

3. Create a virtual environment (optional but recommended) and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

4. Install the required dependencies by running:

```bash
pip install -r requirements.txt
```

5. Start the Flask server by running:

```bash
python backend.py
```

The server will start at http://localhost:5000.


## How it Works
1. Enter a news article title in the input field on the frontend.

2. Click the "Predict" button to send the input to the backend API.

3. The backend uses a machine learning model to predict whether the title is fake or true.

4. The prediction result is displayed on the frontend.

## Disclaimer
Please note that the accuracy of the predictions may vary and that this application is for educational purposes only. The predictions should not be used as the sole basis for determining the authenticity of news articles.

## Credits
The dataset used for this project can be found here: https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset
