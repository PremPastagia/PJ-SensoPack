import os
import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import firebase_admin
from firebase_admin import credentials, db

app = FastAPI()

# Allow CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ═══════════════════════════════════════════════════════════════════════════
# Dynamic Model Loader & Intelligence Pipeline
# ═══════════════════════════════════════════════════════════════════════════
import joblib
import pandas as pd

model = None
model_type = None

# Search candidate paths for Joblib models dynamically
base_dir = os.path.dirname(__file__)
project_root = os.path.dirname(base_dir)

candidate_paths = [
    os.path.join(base_dir, "shrimp_spoilage_model.joblib"),
    os.path.join(project_root, "shrimp_spoilage_model.joblib"),
    os.path.join(project_root, "shrimp_spoilage_model_rf.joblib"),
    os.path.join(project_root, "shrimp_spoilage_model_xgb.joblib"),
    os.path.join(project_root, "V1", "shrimp_spoilage_model.joblib")
]

for path in candidate_paths:
    if os.path.exists(path):
        try:
            model = joblib.load(path)
            model_type = "joblib"
            print(f"[SUCCESS] Dynamically loaded ML Model from: {path}")
            break
        except Exception as e:
            print(f"[WARN] Failed to load joblib model at {path}: {e}")

# Fallback to pure Python transpiled models if joblib is unavailable
if model is None:
    import sys
    sys.path.append(base_dir)
    try:
        from xgb_model import predict_proba as xgb_predict
        model = xgb_predict
        model_type = "pure_python_xgb"
        print("[SUCCESS] Loaded pure-Python XGBoost model.")
    except ImportError:
        try:
            from rf_model import score as rf_predict
            model = rf_predict
            model_type = "pure_python_rf"
            print("[SUCCESS] Loaded pure-Python Random Forest model.")
        except ImportError:
            print("[ERROR] No ML Model could be loaded.")

# Configurable Failsafe Biological Overrides
FAILSAFE_AMMONIA_PPM = float(os.environ.get("FAILSAFE_AMMONIA_PPM", 15.0))
FAILSAFE_TEMP_C = float(os.environ.get("FAILSAFE_TEMP_C", 32.0))
FAILSAFE_PH_LEVEL = float(os.environ.get("FAILSAFE_PH_LEVEL", 7.5))

# Initialize Firebase
try:
    cred_json = os.environ.get('FIREBASE_CREDENTIALS')
    db_url = os.environ.get('FIREBASE_URL', 'https://pj-sensopack-default-rtdb.asia-southeast1.firebasedatabase.app/')
    
    if not firebase_admin._apps:
        if cred_json:
            cred_json_clean = cred_json.replace('\\n', '\n')
            cred_dict = json.loads(cred_json_clean)
            if "private_key" in cred_dict:
                cred_dict["private_key"] = cred_dict["private_key"].replace('\\n', '\n')
            cred = credentials.Certificate(cred_dict)
        else:
            # Local fallback
            cred_path = os.path.join(project_root, "serviceAccountKey.json")
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
    return {
        "status": "ok", 
        "firebase": firebase_initialized, 
        "model_loaded": model is not None,
        "model_type": model_type
    }

@app.post("/api/predict")
def predict(req: PredictRequest):
    if not model:
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

        # 2. DYNAMIC BIOLOGICAL OVERRIDE (Failsafe)
        if ammonia_ppm >= FAILSAFE_AMMONIA_PPM or temp >= FAILSAFE_TEMP_C or ph_level >= FAILSAFE_PH_LEVEL:
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

        # 3. DYNAMIC FEATURE ALIGNMENT
        # Map all available input datapoints into an alias dictionary
        datapoint_map = {
            'ammonia_ppm': ammonia_ppm,
            'mq_raw': ammonia_ppm,
            'ph_level': ph_level,
            'temp': temp,
            'temp_c': temp,
            'temperature_c': temp,
            'time_exposed_hours': time_exposed,
            'storage_time_hrs': time_exposed,
            'humidity': humidity,
            'humidity_pct': humidity,
            'degree_hours': temp * time_exposed
        }

        # 4. ML INFERENCE
        if model_type == "joblib":
            # Dynamically extract feature names expected by the trained model
            if hasattr(model, "feature_names_in_"):
                expected_cols = list(model.feature_names_in_)
                row = [datapoint_map.get(col, 0.0) for col in expected_cols]
                df_features = pd.DataFrame([row], columns=expected_cols)
            else:
                # Default feature list fallback
                expected_cols = ['ammonia_ppm', 'ph_level', 'temperature_c', 'storage_time_hrs', 'humidity_pct']
                row = [datapoint_map.get(col, 0.0) for col in expected_cols]
                df_features = pd.DataFrame([row], columns=expected_cols)
            
            raw_probs = model.predict_proba(df_features)[0]
            
            # Map probabilities dynamically based on model classes
            classes = getattr(model, "classes_", [0, 1, 2])
            if len(raw_probs) == 3:
                safe_score = float(raw_probs[0])
                caution_score = float(raw_probs[1])
                unsafe_score = float(raw_probs[2])
            elif len(raw_probs) == 2:
                spoilage_prob = float(raw_probs[1])
                safe_score = max(0.0, 1.0 - spoilage_prob)
                unsafe_score = spoilage_prob
                caution_score = 0.4 - abs(spoilage_prob - 0.4) if 0.2 < spoilage_prob < 0.6 else 0.0
                tot = safe_score + caution_score + unsafe_score
                safe_score /= tot
                caution_score /= tot
                unsafe_score /= tot
            else:
                safe_score, caution_score, unsafe_score = 0.33, 0.33, 0.34
                
        else:
            # Pure Python model invocation
            # Features order: [temp, humidity, ammonia_ppm, time_exposed, ph_level, degree_hours] or [ammonia_ppm, ph_level, temp, time_exposed, humidity]
            try:
                features = [ammonia_ppm, ph_level, temp, time_exposed, humidity]
                raw_probs = model(features)
            except Exception:
                features = [temp, humidity, ammonia_ppm, time_exposed, ph_level, temp * time_exposed]
                raw_probs = model(features)
                
            if len(raw_probs) == 3:
                safe_score = float(raw_probs[0])
                caution_score = float(raw_probs[1])
                unsafe_score = float(raw_probs[2])
            else:
                spoilage_prob = float(raw_probs[1]) if len(raw_probs) > 1 else float(raw_probs[0])
                safe_score = 1.0 - spoilage_prob
                unsafe_score = spoilage_prob
                caution_score = 0.0

        # Determine main prediction dynamically based on highest confidence
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
