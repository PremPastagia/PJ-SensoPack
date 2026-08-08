"""
SensoPack — Local FastAPI deployment for the shrimp spoilage classifier.

Run with:  uvicorn server:app --host 127.0.0.1 --port 8000 --reload
Requires shrimp_spoilage_model.joblib in the same directory (produced by sensopack_colab.py).
"""

import sys
from pathlib import Path

import joblib
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

MODEL_PATH = Path(__file__).parent / "shrimp_spoilage_model.joblib"

STATUS_LABELS = {0: "SAFE", 1: "CAUTION", 2: "UNSAFE"}

RECOMMENDED_ACTIONS = {
    "SAFE": "Product is within safe freshness bounds. Continue storing at recommended chill temperature.",
    "CAUTION": "Early spoilage indicators detected. Consume soon and keep refrigerated; re-check before sale/use.",
    "UNSAFE": "Spoilage thresholds exceeded. Do not consume or sell — discard and flag the batch.",
}

FEATURE_ORDER = ["ammonia_ppm", "ph_level", "temperature_c", "storage_time_hrs", "humidity_pct"]

if not MODEL_PATH.exists():
    sys.exit(
        f"ERROR: {MODEL_PATH.name} not found in {MODEL_PATH.parent}.\n"
        "Run sensopack_colab.py first to generate the trained model."
    )

model = joblib.load(MODEL_PATH)

app = FastAPI(title="SensoPack Spoilage Prediction API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class SensorReading(BaseModel):
    ammonia_ppm: float = Field(ge=0, le=200, description="Headspace ammonia concentration, ppm")
    ph_level: float = Field(ge=0, le=14, description="pH of shrimp tissue/exudate")
    temperature_c: float = Field(ge=-20, le=50, description="Storage temperature, degrees C")
    storage_time_hrs: float = Field(ge=0, le=2000, description="Elapsed storage time, hours")
    humidity_pct: float = Field(ge=0, le=100, description="Relative humidity, percent")


class PredictionResponse(BaseModel):
    prediction_code: int
    status_label: str
    confidence_scores: dict
    recommended_action: str


@app.get("/")
def root():
    return {"service": "SensoPack Spoilage Prediction API", "status": "running"}


@app.post("/predict", response_model=PredictionResponse)
def predict(reading: SensorReading):
    try:
        features = [[getattr(reading, col) for col in FEATURE_ORDER]]
        pred_code = int(model.predict(features)[0])
        proba = model.predict_proba(features)[0]
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Model inference failed: {exc}")

    status_label = STATUS_LABELS[pred_code]
    confidence_scores = {
        STATUS_LABELS[cls]: round(float(p), 4)
        for cls, p in zip(model.classes_, proba)
    }

    return PredictionResponse(
        prediction_code=pred_code,
        status_label=status_label,
        confidence_scores=confidence_scores,
        recommended_action=RECOMMENDED_ACTIONS[status_label],
    )


# Serve the frontend webapp from /app
WEBAPP_DIR = Path(__file__).parent / "webapp"
if WEBAPP_DIR.exists():
    app.mount("/app", StaticFiles(directory=str(WEBAPP_DIR), html=True), name="webapp")

