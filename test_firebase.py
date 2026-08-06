import json
import firebase_admin
from firebase_admin import credentials, db
import os

cred_path = os.path.join(os.path.dirname(__file__), "serviceAccountKey.json")
FIREBASE_DB_URL = 'https://pj-sensopack-default-rtdb.asia-southeast1.firebasedatabase.app/'

cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred, {
    'databaseURL': FIREBASE_DB_URL
})

ref = db.reference('sensor_state')
try:
    print("Testing Firebase GET...")
    print(ref.get())
    
    print("Testing Firebase SET...")
    ref.set({
        "ammonia_ppm": 12.5,
        "temp_c": 4.5,
        "humidity": 82,
        "timestamp": 123456789
    })
    print("SET successful! Checking GET again...")
    print(ref.get())
except Exception as e:
    print(f"Error: {e}")
