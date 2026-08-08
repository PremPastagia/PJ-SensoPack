import serial
import serial.tools.list_ports
import time
import json
import firebase_admin
from firebase_admin import credentials, db
import os
import sys

print("=========================================")
print("  SensoPack Arduino -> Firebase Bridge   ")
print("=========================================")

# Configuration
BAUD_RATE = 9600
FALLBACK_PORT = 'COM12'
FIREBASE_DB_URL = os.environ.get('FIREBASE_URL', 'https://pj-sensopack-default-rtdb.asia-southeast1.firebasedatabase.app/')

def find_serial_port():
    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        desc = port.description.lower()
        hwid = port.hwid.lower()
        if any(x in desc or x in hwid for x in ["arduino", "ch340", "usb", "serial", "ftdi", "cp210"]):
            print(f"[Auto-detect] Found microcontroller on port: {port.device} ({port.description})")
            return port.device
    return None

detected_port = find_serial_port()
SERIAL_PORT = detected_port if detected_port else FALLBACK_PORT
if not detected_port:
    print(f"[Warning] No microcontroller auto-detected. Falling back to: {FALLBACK_PORT}")

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

# Room default fallbacks if hardware sensors fail or report ERROR
DEFAULT_ROOM_TEMP = float(os.environ.get('DEFAULT_ROOM_TEMP', 25.0))
DEFAULT_ROOM_HUMIDITY = float(os.environ.get('DEFAULT_ROOM_HUMIDITY', 60.0))

def parse_sensor_reading(line):
    temp = DEFAULT_ROOM_TEMP
    humidity = DEFAULT_ROOM_HUMIDITY
    ammonia_ppm = 2.0
    valid = False

    # 1. Try JSON parsing
    try:
        payload = json.loads(line)
        if isinstance(payload, dict):
            t_val = payload.get("temp")
            h_val = payload.get("humidity")
            a_val = payload.get("ammonia_ppm") or payload.get("mq_raw")

            if t_val is not None and str(t_val).upper() != "ERROR":
                temp = float(t_val)
            if h_val is not None and str(h_val).upper() != "ERROR":
                humidity = float(h_val)
            if a_val is not None and str(a_val).upper() != "ERROR":
                val = float(a_val)
                ammonia_ppm = (val / 1023.0 * 30.0) if val > 30 else val

            return temp, humidity, round(ammonia_ppm, 2), True
    except Exception:
        pass

    # 2. Try Tabular parsing (e.g., '15s  ERROR  ERROR  283')
    parts = line.split()
    if len(parts) >= 4 and (parts[0].endswith('s') or parts[0].isdigit()):
        t_str, h_str, a_str = parts[1], parts[2], parts[3]

        if t_str.upper() != "ERROR":
            try: temp = float(t_str)
            except ValueError: pass
        
        if h_str.upper() != "ERROR":
            try: humidity = float(h_str)
            except ValueError: pass

        if a_str.upper() != "ERROR":
            try:
                val = float(a_str)
                ammonia_ppm = (val / 1023.0 * 30.0) if val > 30 else val
            except ValueError: pass

        return temp, humidity, round(ammonia_ppm, 2), True

    return None, None, None, False

# 3. Read loop
print("Bridge is active. Press Ctrl+C to stop.")
print(f"Fallback active: Room Temp = {DEFAULT_ROOM_TEMP}°C, Room Humidity = {DEFAULT_ROOM_HUMIDITY}%\n")

try:
    while True:
        try:
            ser.write(b'R')
        except Exception as e:
            print(f"Error writing to serial: {e}")
            time.sleep(2)
            continue
        
        try:
            raw_line = ser.readline()
            line = raw_line.decode('utf-8', errors='ignore').strip()
        except Exception as e:
            print(f"Error reading serial: {e}")
            continue
        
        if line and not line.startswith('#') and not line.startswith('TIME') and not line.startswith('---') and not line.startswith('SensoPack'):
            temp, humidity, ammonia_ppm, ok = parse_sensor_reading(line)
            if ok:
                data = {
                    "temp_c": temp,
                    "humidity": humidity,
                    "ammonia_ppm": ammonia_ppm,
                    "timestamp": time.time()
                }

                # Push to Firebase
                ref.set(data)
                print(f"[Pushed to Cloud] Temp: {temp}°C | Humidity: {humidity}% | Ammonia: {ammonia_ppm} ppm")
            else:
                if not line.startswith('Checking') and not line.startswith('->') and not line.startswith('Starting'):
                    print(f"[Serial Received]: {line}")
                
        time.sleep(2)

except KeyboardInterrupt:
    print("\nBridge stopped by user.")
    ser.close()
    sys.exit(0)
except Exception as e:
    print(f"\n[ERROR] Bridge crashed: {e}")
    if ser.is_open:
        ser.close()
    sys.exit(1)
