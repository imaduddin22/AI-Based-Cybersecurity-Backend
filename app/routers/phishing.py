from fastapi import APIRouter
import joblib
import numpy as np
import os

router = APIRouter()

model_path = os.path.join("app", "models", "phishing_detection_model.pkl")
model = joblib.load(model_path)

@router.post("/predict_phishing")
def predict_phishing(data: dict):
    try:
        features = np.array(data["features"]).reshape(1, -1)
        prediction = model.predict(features)[0]
        return {"prediction": int(prediction)}
    except Exception as e:
        return {"error": str(e)}