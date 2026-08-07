import os
import json
import joblib
import numpy as np
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import firebase_admin
from firebase_admin import credentials, db

app = FastAPI()

# Allow CORS for mobile app access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load Model
MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "shrimp_spoilage_model.joblib")
try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    model = None
    print(f"Failed to load model: {e}")

# Initialize Firebase
try:
    cred_json = os.environ.get('FIREBASE_CREDENTIALS')
    db_url = os.environ.get('FIREBASE_URL', 'https://pj-sensopack-default-rtdb.asia-southeast1.firebasedatabase.app/')
    
    if not firebase_admin._apps:
        if cred_json:
            cred_dict = json.loads(cred_json)
            cred = credentials.Certificate(cred_dict)
        else:
            # Local fallback
            cred_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "serviceAccountKey.json")
            if os.path.exists(cred_path):
                cred = credentials.Certificate(cred_path)
            else:
                raise Exception("No serviceAccountKey.json found and FIREBASE_CREDENTIALS env var not set.")
            
        firebase_admin.initialize_app(cred, {
            'databaseURL': db_url
        })
    firebase_initialized = True
except Exception as e:
    print(f"Firebase Init Error: {e}")
    firebase_initialized = False

class PredictRequest(BaseModel):
    ph_level: float
    storage_time_hrs: float
    ammonia_ppm: float

@app.get("/api/health")
def health_check():
    return {"status": "ok", "firebase": firebase_initialized, "model_loaded": model is not None}

@app.post("/api/predict")
def predict(req: PredictRequest):
    if not model:
        raise HTTPException(status_code=500, detail="ML Model not loaded")
    if not firebase_initialized:
        raise HTTPException(status_code=500, detail="Firebase not configured")
        
    try:
        # 1. Fetch latest sensor data from Firebase
        ref = db.reference('sensor_state')
        sensor_data = ref.get()
        
        if not sensor_data:
            raise HTTPException(status_code=404, detail="No sensor data found in Firebase. Ensure the Arduino is connected and running.")
            
        if 'temp_c' not in sensor_data or 'humidity' not in sensor_data:
            raise HTTPException(status_code=400, detail="Missing temperature or humidity data from Arduino.")
            
        temp = float(sensor_data['temp_c'])
        humidity = float(sensor_data['humidity'])
        ammonia = req.ammonia_ppm
        
        # Model expects: ['ammonia_ppm' 'ph_level' 'temperature_c' 'storage_time_hrs' 'humidity_pct']
        features = np.array([[ammonia, req.ph_level, temp, req.storage_time_hrs, humidity]])
        
        # 3. Predict
        prediction_val = int(model.predict(features)[0])
        probabilities = model.predict_proba(features)[0]
        
        STATUS_MAP = {0: "SAFE", 1: "CAUTION", 2: "UNSAFE"}
        prediction_str = STATUS_MAP.get(prediction_val, "CAUTION")
        
        # Determine recommended action
        if prediction_str == "UNSAFE":
            action = "Product shows definitive spoilage markers. Discard immediately."
        elif prediction_str == "CAUTION":
            action = "Product is nearing end of shelf life. Prioritize for immediate sale or test physically."
        else:
            action = "Product is within safe freshness bounds. Continue storing at recommended chill temperature."
            
        return {
            "prediction": prediction_str,
            "confidence_scores": {
                "SAFE": float(probabilities[0]),
                "CAUTION": float(probabilities[1]),
                "UNSAFE": float(probabilities[2])
            },
            "sensor_data_used": {
                "ammonia_ppm": ammonia,
                "temp_c": temp,
                "humidity": humidity
            },
            "recommended_action": action
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
