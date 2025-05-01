import joblib
import numpy as np
import os

model_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'gold_price_model.pkl')
model = joblib.load(model_path)

def predict_price(features: list):
    input_array = np.array([features])
    prediction = model.predict(input_array)
    return prediction[0]
