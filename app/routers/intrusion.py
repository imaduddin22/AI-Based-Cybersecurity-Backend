from fastapi import APIRouter
import joblib
import numpy as np

router = APIRouter()

model = joblib.load("app/models/intrusion_detection_model.pkl")

@router.post("/predict_intrusion")
def predict_intrusion(data: dict):
    features = np.array(data["features"]).reshape(1, -1)
    prediction = model.predict(features)
    return {"prediction": int(prediction[0])}