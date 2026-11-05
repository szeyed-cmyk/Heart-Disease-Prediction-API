from pydantic import BaseModel, Field

class HeartDiseaseInput(BaseModel):
    age: float = Field(..., example=52, description="Age in years")
    sex: float = Field(..., example=1, description="Sex (1 = male, 0 = female)")
    cp: float = Field(..., example=0, description="Chest pain type (0-3)")
    trestbps: float = Field(..., example=125, description="Resting blood pressure")
    chol: float = Field(..., example=212, description="Serum cholesterol in mg/dl")
    fbs: float = Field(..., example=0, description="Fasting blood sugar > 120 mg/dl (1 = true)")
    restecg: float = Field(..., example=1, description="Resting ECG results (0-2)")
    thalach: float = Field(..., example=168, description="Maximum heart rate achieved")
    exang: float = Field(..., example=0, description="Exercise induced angina (1 = yes)")
    oldpeak: float = Field(..., example=1.0, description="ST depression induced by exercise")
    slope: float = Field(..., example=2, description="Slope of peak exercise ST segment")
    ca: float = Field(..., example=2, description="Number of major vessels (0-3)")
    thal: float = Field(..., example=3, description="Thalassemia (0 = normal, 1 = fixed, 2 = reversible)")

    class Config:
        json_schema_extra = {
            "example": {
                "age": 52,
                "sex": 1,
                "cp": 0,
                "trestbps": 125,
                "chol": 212,
                "fbs": 0,
                "restecg": 1,
                "thalach": 168,
                "exang": 0,
                "oldpeak": 1.0,
                "slope": 2,
                "ca": 2,
                "thal": 3
            }
        }
