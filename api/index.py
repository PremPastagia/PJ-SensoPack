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
MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "shrimp_spoilage_model_xgb.joblib")
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
    temp: float = None
    humidity: float = None
    mq_raw: float
    time_exposed_hours: float = 0.5
    ph_level: float

@app.get("/api/health")
def health_check():
    return {"status": "ok", "firebase": firebase_initialized, "model_loaded": model is not None}

@app.post("/api/predict")
def predict(req: PredictRequest):
    if not model:
        raise HTTPException(status_code=500, detail="ML Model not loaded")
        
    try:
        # 1. Determine Temperature and Humidity (Sandbox vs Sensor)
        if req.temp is not None and req.humidity is not None:
            temp = req.temp
            humidity = req.humidity
            sensor_data_used = None
        else:
            if not firebase_initialized:
                raise HTTPException(status_code=500, detail="Firebase not configured")
            ref = db.reference('sensor_state')
            sensor_data = ref.get()
            if not sensor_data:
                raise HTTPException(status_code=404, detail="No sensor data in Firebase.")
            if 'temp_c' not in sensor_data or 'humidity' not in sensor_data:
                raise HTTPException(status_code=400, detail="Missing sensor data.")
            temp = float(sensor_data['temp_c'])
            humidity = float(sensor_data['humidity'])
            mq_raw_fb = float(sensor_data.get('mq_raw', req.mq_raw))
            sensor_data_used = {"temp_c": temp, "humidity": humidity, "mq_raw": mq_raw_fb}
            
        mq_raw = req.mq_raw if (req.temp is not None) else mq_raw_fb
        time_exposed = req.time_exposed_hours
        ph_level = req.ph_level

        # 2. BIOLOGICAL OVERRIDE (Failsafe)
        if mq_raw >= 600 or temp >= 35.0 or ph_level >= 8.0:
            return {
                "prediction": "UNSAFE",
                "status": "Spoiled",
                "spoilage_probability": 0.99,
                "reason": "Critical biological threshold breached.",
                "sensor_data_used": sensor_data_used
            }

        # 3. FEATURE ENGINEERING
        degree_hours = temp * time_exposed
        
        # Features matching train_xgboost.py: ['temp', 'humidity', 'mq_raw', 'time_exposed_hours', 'ph_level', 'degree_hours']
        features = np.array([[temp, humidity, mq_raw, time_exposed, ph_level, degree_hours]])
        
        # 4. ML INFERENCE
        spoilage_prob = float(model.predict_proba(features)[0][1]) # Prob of Class 1
        
        if spoilage_prob > 0.40:
            status = "UNSAFE"
            action = "Product shows spoilage markers. Discard immediately."
        else:
            status = "SAFE"
            action = "Product is within safe freshness bounds."

        return {
            "prediction": status,
            "status": "Spoiled" if status == "UNSAFE" else "Fresh",
            "spoilage_probability": round(spoilage_prob, 4),
            "sensor_data_used": sensor_data_used,
            "recommended_action": action
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
