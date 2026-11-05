# Heart Disease Prediction API

A FastAPI application that predicts the presence of heart disease using a Random Forest classifier trained on the UCI Heart Disease dataset. The app is containerized with Docker and ready for deployment on Render.

## Features

- `GET /health` — Health check endpoint
- `GET /info` — Returns model type and feature list
- `POST /predict` — Predicts heart disease (`true`/`false`) with probability
- Interactive Swagger UI at `/docs`

## Project Structure

```
.
├── app/
│   ├── main.py
│   └── schemas.py
├── model/
│   └── heart_model.joblib
├── heart.csv
├── train_model.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Prerequisites

- Python 3.11+
- Docker Desktop (with WSL 2)

## Setup & Training

1. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Train the model (requires `heart.csv` in the project root):

   ```bash
   python train_model.py
   ```

   This creates `model/heart_model.joblib`.

## Run Locally (without Docker)

```bash
uvicorn app.main:app --reload
```

Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Run with Docker

1. Build the image:

   ```bash
   docker-compose build
   ```

2. Start the container:

   ```bash
   docker-compose up
   ```

   Or run in the background:

   ```bash
   docker-compose up -d
   ```

3. Access the API:

   - Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
   - Health: [http://localhost:8000/health](http://localhost:8000/health)
   - Info: [http://localhost:8000/info](http://localhost:8000/info)

### Stop the container

```bash
docker-compose down
```

## Example Prediction Request

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
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
  }'
```

## Deployment on Render

1. Push this project to a GitHub repository.
2. Go to [Render](https://render.com) and create a new **Web Service**.
3. Select **Docker** as the environment.
4. Connect your GitHub repository.
5. Deploy and test the endpoints using your Render URL.

## Model Details

| Item | Value |
|------|-------|
| Algorithm | Random Forest Classifier |
| Dataset | UCI Heart Disease (`heart.csv`) |
| Features | age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal |
| Target | Binary classification (presence / absence of heart disease) |
