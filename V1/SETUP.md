# SensoPack ML Pipeline — Local Setup

## 1. Environment

```bash
cd "/Users/virajvekariya/Desktop/Competition/PJ Comp/SensoPack_ML"
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn joblib scikit-learn requests pandas numpy seaborn matplotlib
```

## 2. Generate the model (run once, or whenever you change the data-generation logic)

```bash
python3 sensopack_colab.py
```

This prints the class distribution, correlation matrix, accuracy/confusion matrix/
classification report, and writes `shrimp_spoilage_model.joblib` and
`correlation_heatmap.png` into this folder. (Same script also runs unmodified in a
Google Colab cell.)

## 3. Start the API server

```bash
uvicorn server:app --host 127.0.0.1 --port 8000 --reload
```

Server will refuse to start with a clear error if `shrimp_spoilage_model.joblib` is missing —
run step 2 first.

## 4. Test it

In a second terminal (venv activated):

```bash
python3 test_client.py            # 3 canned cases: fresh / spoiled / boundary
python3 test_client.py --live     # then simulates a Pi polling every 3s
```

Or manually:

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"ammonia_ppm": 1.5, "ph_level": 6.7, "temperature_c": 2.0, "storage_time_hrs": 24, "humidity_pct": 85}'
```

Out-of-range spot check (should return HTTP 422, not a prediction):

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"ammonia_ppm": 1.5, "ph_level": 20, "temperature_c": 2.0, "storage_time_hrs": 24, "humidity_pct": 85}'
```

## 5. Wiring in the real Raspberry Pi later

Once the ammonia/pH/temp/humidity sensors are actually reading (see the hardware plan
discussed earlier — ADC/Arduino bridge, regulated GSM power, etc.), point the Pi's polling
loop at this same `POST /predict` endpoint (swap `127.0.0.1` for this machine's LAN IP, or
move the server onto the Pi itself) instead of `test_client.py`'s canned/random payloads.
