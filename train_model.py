import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import os

# Create model folder if it doesn't exist
os.makedirs("model", exist_ok=True)

# Load dataset from GitHub (or local file if available)
print("Loading dataset...")
url = "D:/Module 17 Assignment/heart-disease-api/heart-disease-api/heart.csv"
try:
    df = pd.read_csv(url)
    print("Loaded from GitHub")
except:
    df = pd.read_csv("heart.csv")
    print("Loaded from local file")

print(f"Dataset shape: {df.shape}")
print(df.head())
print("\nColumns:", df.columns.tolist())

# Features and target
feature_cols = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
    "thalach", "exang", "oldpeak", "slope", "ca", "thal"
]

X = df[feature_cols]
y = df["target"]

# Train / test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train Random Forest classifier
print("\nTraining model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(f"\nAccuracy: {accuracy_score(y_test, y_pred):.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save the model
model_path = "model/heart_model.joblib"
joblib.dump(model, model_path)
print(f"\nModel saved successfully to: {model_path}")

# Optional: also save feature list
#joblib.dump(feature_cols, "model/feature_list.joblib")
#print("Feature list also saved.")
