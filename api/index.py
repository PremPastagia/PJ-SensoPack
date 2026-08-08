import os
import json
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
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load Pure Python Random Forest Model
import sys
sys.path.append(os.path.dirname(__file__))

try:
    from rf_model import score as predict_proba
except ImportError:
    try:
        from api.rf_model import score as predict_proba
    except ImportError as e:
        print(f"Model Import Error: {e}")
        predict_proba = None

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
    ammonia_ppm: float
    time_exposed_hours: float = 0.5
    ph_level: float

@app.get("/api/health")
def health_check():
    return {"status": "ok", "firebase": firebase_initialized, "model_loaded": predict_proba is not None}

@app.post("/api/predict")
def predict(req: PredictRequest):
    if not predict_proba:
        raise HTTPException(status_code=500, detail="ML Model not loaded")
        
    try:
        # 1. Determine Temperature and Humidity (Sandbox vs Sensor)
        if req.temp is not None and req.humidity is not None:
            temp = req.temp
            humidity = req.humidity
            ammonia_ppm = req.ammonia_ppm
            sensor_data_used = {
                "temp_c": temp,
                "humidity": humidity,
                "ammonia_ppm": ammonia_ppm,
                "temp_source": "sandbox",
                "humidity_source": "sandbox",
                "ammonia_source": "sandbox"
            }
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
            
            # Ammonia is always sourced from the manual slider for upload/scan mode
            ammonia_ppm = req.ammonia_ppm
            ammonia_source = "manual"
                
            sensor_data_used = {
                "temp_c": temp,
                "humidity": humidity,
                "ammonia_ppm": ammonia_ppm,
                "temp_source": "sensor",
                "humidity_source": "sensor",
                "ammonia_source": ammonia_source
            }

        time_exposed = req.time_exposed_hours
        ph_level = req.ph_level

        # 2. BIOLOGICAL OVERRIDE (Failsafe)
        # Thresholds match the literature-grounded "Spoiled" bounds (see
        # PHASE1_LITERATURE.md): ammonia headspace >15ppm, pH >7.5. Storage
        # temp >32C is just above the training data's abuse-band ceiling
        # (-2 to 30C), i.e. clearly outside the model's trained domain.
        if ammonia_ppm >= 15.0 or temp >= 32.0 or ph_level >= 7.5:
            return {
                "prediction": "UNSAFE",
                "status": "Spoiled",
                "spoilage_probability": 0.99,
                "reason": "Critical biological threshold breached.",
                "sensor_data_used": sensor_data_used,
                "confidence_scores": {
                    "SAFE": 0.0,
                    "CAUTION": 0.01,
                    "UNSAFE": 0.99
                }
            }

        # Features matching V1 model: ["ammonia_ppm", "ph_level", "temperature_c", "storage_time_hrs", "humidity_pct"]
        features = [ammonia_ppm, ph_level, temp, time_exposed, humidity]
        
        # 4. ML INFERENCE
        probs = predict_proba(features)
        safe_score = float(probs[0])
        caution_score = float(probs[1])
        unsafe_score = float(probs[2])
        
        # Determine main prediction based on highest probability
        max_prob = max(safe_score, caution_score, unsafe_score)
        if max_prob == unsafe_score:
            status = "UNSAFE"
        elif max_prob == caution_score:
            status = "CAUTION"
        else:
            status = "SAFE"

        return {
            "prediction": status,
            "status": "Spoiled" if status == "UNSAFE" else ("Caution" if status == "CAUTION" else "Fresh"),
            "spoilage_probability": round(unsafe_score, 4),
            "sensor_data_used": sensor_data_used,
            "confidence_scores": {
                "SAFE": safe_score,
                "CAUTION": caution_score,
                "UNSAFE": unsafe_score
            }
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
