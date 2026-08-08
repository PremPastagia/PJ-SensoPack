"""
SensoPack — simulates an IoT device (e.g. Raspberry Pi) posting sensor readings
to the local FastAPI server.

Usage:
  python3 test_client.py            # sends 3 canned cases (fresh / spoiled / boundary)
  python3 test_client.py --live     # then loops, posting a new perturbed reading every 3s
"""

import sys
import time
import random

import requests

SERVER_URL = "http://127.0.0.1:8000/predict"

CANNED_CASES = {
    "clearly fresh": {
        "ammonia_ppm": 1.5,
        "ph_level": 6.7,
        "temperature_c": 2.0,
        "storage_time_hrs": 24,
        "humidity_pct": 85,
    },
    "clearly spoiled": {
        "ammonia_ppm": 28.0,
        "ph_level": 7.9,
        "temperature_c": 22.0,
        "storage_time_hrs": 200,
        "humidity_pct": 80,
    },
    "boundary / ambiguous": {
        "ammonia_ppm": 9.0,
        "ph_level": 7.3,
        "temperature_c": 8.0,
        "storage_time_hrs": 130,
        "humidity_pct": 88,
    },
}


def send_reading(label, payload):
    try:
        resp = requests.post(SERVER_URL, json=payload, timeout=5)
    except requests.exceptions.ConnectionError:
        sys.exit(
            "ERROR: could not reach the server at "
            f"{SERVER_URL}. Is it running? (uvicorn server:app --reload)"
        )

    print(f"\n--- {label} ---")
    print("Payload:", payload)
    if resp.status_code != 200:
        print(f"HTTP {resp.status_code}: {resp.text}")
        return
    result = resp.json()
    print(f"Prediction: {result['status_label']} (code {result['prediction_code']})")
    print(f"Confidence: {result['confidence_scores']}")
    print(f"Action:     {result['recommended_action']}")


def random_perturbed_reading():
    base = random.choice(list(CANNED_CASES.values()))
    return {k: round(v * random.uniform(0.9, 1.1), 2) for k, v in base.items()}


def main():
    for label, payload in CANNED_CASES.items():
        send_reading(label, payload)

    if "--live" in sys.argv:
        print("\nEntering live simulation mode (Ctrl+C to stop)...")
        try:
            while True:
                time.sleep(3)
                reading = random_perturbed_reading()
                send_reading("live sensor poll", reading)
        except KeyboardInterrupt:
            print("\nStopped.")


if __name__ == "__main__":
    main()
