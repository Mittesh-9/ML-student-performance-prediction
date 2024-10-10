from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the model
model = joblib.load('final_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract form data from the frontend
    features = [x for x in request.form.values()]

    # Convert the input into a pandas DataFrame (adjust according to your feature input)
    input_data = pd.DataFrame([features], columns=['gender', 'parental level of education', 'test preparation course'])  # Change these to actual feature names

    # Make prediction using the loaded model
    prediction = model.predict(input_data)[0]

    return render_template('index.html', prediction_text=f'Predicted performance: {prediction}')

if __name__ == "__main__":
    app.run(debug=True)
