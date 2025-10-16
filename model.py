import joblib
import numpy as np
import os
from typing import Optional

_loaded_model: Optional[object] = None

def _resolve_model_path() -> str:
    current_dir = os.path.dirname(__file__)
    # Check common relative locations
    candidate_paths = [
        os.path.join(current_dir, 'model', 'gold_price_model.pkl'),
        os.path.join(current_dir, '..', 'model', 'gold_price_model.pkl'),
        os.path.join(current_dir, 'gold_price_model.pkl'),
    ]
    for path in candidate_paths:
        if os.path.isfile(path):
            return path
    raise FileNotFoundError("Model file 'gold_price_model.pkl' not found in expected locations")

def _get_model():
    global _loaded_model
    if _loaded_model is None:
        model_path = _resolve_model_path()
        _loaded_model = joblib.load(model_path)
    return _loaded_model

def predict_price(features: list):
    model = _get_model()
    input_array = np.array([features], dtype=float)
    prediction = model.predict(input_array)
    # Ensure JSON-serializable float
    value = prediction[0]
    try:
        return float(value)
    except Exception:
        # Fallback: convert numpy types
        return float(np.asarray(value).item())
