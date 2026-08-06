import serial
import time
import json
import firebase_admin
from firebase_admin import credentials, db
import os
import sys

# Configuration
SERIAL_PORT = 'COM12'
BAUD_RATE = 9600
FIREBASE_DB_URL = os.environ.get('FIREBASE_URL', 'https://pj-sensopack-default-rtdb.asia-southeast1.firebasedatabase.app/')

print("=========================================")
print("  SensoPack Arduino -> Firebase Bridge   ")
print("=========================================")

# 1. Initialize Firebase
cred_path = os.path.join(os.path.dirname(__file__), "serviceAccountKey.json")
if not os.path.exists(cred_path):
    print("\n[ERROR] Missing serviceAccountKey.json!")
    print("Please download your Firebase Admin private key and place it in this folder.")
    sys.exit(1)

try:
    print(f"Connecting to Firebase: {FIREBASE_DB_URL}")
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred, {
        'databaseURL': FIREBASE_DB_URL
    })
    ref = db.reference('sensor_state')
    print("Firebase connected successfully.\n")
except Exception as e:
    print(f"\n[ERROR] Failed to connect to Firebase: {e}")
    sys.exit(1)

# 2. Connect to Arduino
try:
    print(f"Connecting to Arduino on {SERIAL_PORT}...")
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2)
    time.sleep(2) # Wait for Arduino to reset
    print("Arduino connected successfully.\n")
except Exception as e:
    print(f"\n[ERROR] Could not connect to Arduino on {SERIAL_PORT}.")
    print("Make sure it is plugged in, the port is correct, and the Arduino IDE Serial Monitor is CLOSED.")
    sys.exit(1)

# 3. Read loop
print("Bridge is active. Press Ctrl+C to stop.")
print("Waiting for data...")

try:
    while True:
        # Request data (SensoPack protocol expects 'R')
        ser.write(b'R')
        
        # Read response
        line = ser.readline().decode('utf-8').strip()
        
        if line and not line.startswith('#'):
            try:
                # Expected CSV: ammonia_ppm,temperature_c,humidity_pct
                parts = line.split(',')
                if len(parts) == 3:
                    ammonia = float(parts[0])
                    temp = float(parts[1])
                    humidity = float(parts[2])
                    
                    data = {
                        "ammonia_ppm": ammonia,
                        "temp_c": temp,
                        "humidity": humidity,
                        "timestamp": time.time()
                    }
                    
                    # Push to Firebase
                    ref.set(data)
                    print(f"[Pushed to Cloud] Ammonia: {ammonia}ppm | Temp: {temp}°C | Humidity: {humidity}%")
            except Exception as e:
                print(f"Error parsing data line: '{line}' - {e}")
                
        time.sleep(2) # Poll every 2 seconds

except KeyboardInterrupt:
    print("\nBridge stopped by user.")
    ser.close()
    sys.exit(0)
except Exception as e:
    print(f"\n[ERROR] Bridge crashed: {e}")
    if ser.is_open:
        ser.close()
    sys.exit(1)
