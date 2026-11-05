from fastapi import FastAPI, HTTPException
from app.schemas import HeartDiseaseInput
import joblib
import numpy as np
import os

app = FastAPI(
    title="Heart Disease Prediction API",
    description="API that predicts presence of heart disease",
    version="1.0.0"
)

# Load model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "model", "heart_model.joblib")
model = joblib.load(MODEL_PATH)

FEATURE_ORDER = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
    "thalach", "exang", "oldpeak", "slope", "ca", "thal"
]


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/info")
def info():
    return {
        "model_type": "RandomForestClassifier",
        "features": FEATURE_ORDER,
        "target": "heart_disease (true = presence, false = absence)"
    }


@app.post("/predict")
def predict(data: HeartDiseaseInput):
    try:
        features = np.array([[
            data.age, data.sex, data.cp, data.trestbps, data.chol,
            data.fbs, data.restecg, data.thalach, data.exang,
            data.oldpeak, data.slope, data.ca, data.thal
        ]])

        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0][1]

        return {
            "heart_disease": bool(prediction),
            "probability": float(probability)
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
