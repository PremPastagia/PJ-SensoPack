# 🦐 SensoPack — AI-Powered Smart Shrimp Packaging System

> An end-to-end IoT + Machine Learning system that predicts shrimp freshness by scanning a smart package. Combines a biofilm color indicator, QR code tracking, and Arduino sensors to deliver an instant SAFE / CAUTION / UNSAFE freshness verdict.

---

## 📋 Table of Contents

- [What Is SensoPack?](#what-is-sensopack)
- [How It Works](#how-it-works)
- [System Architecture](#system-architecture)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
- [QR Code Generation](#qr-code-generation)
- [Arduino Setup](#arduino-setup)
- [ML Model Details](#ml-model-details)
- [Tech Stack](#tech-stack)
- [Calibration Notes](#calibration-notes)

---

## What Is SensoPack?

SensoPack is a **smart packaging system** for monitoring shrimp (*Litopenaeus vannamei*) freshness in real-time. Each package contains:

1. **A Biofilm Color Indicator** — A strip made with **Red Cabbage Anthocyanin** that changes color based on the pH of gases released by the shrimp. As the shrimp spoils, volatile amines (like ammonia and trimethylamine) increase the pH, causing the strip to shift from **Pink/Red (Fresh) → Purple (Caution) → Blue (Spoiled)**.

2. **A QR Code** — Encodes package metadata: batch ID, product ID, packaging time, initial storage temperature, facility location, and product notes.

3. **Arduino Sensors** — An Arduino Uno connected to an **MQ-137 ammonia gas sensor** (and optionally a DHT11 for temperature/humidity) that measures the headspace gas concentration inside the package.

A web application scans the package, reads all inputs automatically, and feeds them to a trained **Random Forest Classifier** that predicts freshness as **SAFE**, **CAUTION**, or **UNSAFE** with confidence scores.

---

## How It Works

The entire workflow requires **one user action** — clicking the "Scan Package" button:

```
Step 1: CONNECT
  User connects the Arduino via the "Connect Arduino" button
  (uses the Web Serial API in Chrome/Edge)

Step 2: SCAN
  User places the package (QR code + biofilm strip) in front of the webcam
  and clicks "📷 Scan Package"

  The system automatically:
  ├── Captures a camera frame
  ├── Decodes the QR code → extracts batch info + computes storage time
  ├── Detects the biofilm color → samples 20 points → estimates pH
  ├── Sends "R" command to Arduino → receives fresh ammonia/temp/humidity data
  └── Assembles all 5 ML model inputs

Step 3: PREDICT
  The system sends the 5 parameters to the ML model and displays:
  ├── Freshness verdict: SAFE ✅ / CAUTION ⚠️ / UNSAFE 🚫
  ├── Confidence scores for each class
  └── Recommended action
```

---

## System Architecture

```
┌──────────────────────────────────────────────────┐
│               BROWSER (Frontend)                 │
│                                                  │
│  Camera ──► jsQR Decode ──► QR Metadata          │
│          ──► Biofilm Color ──► RGB→HSV→pH        │
│                                                  │
│  Web Serial API ──► Arduino ──► NH₃, Temp, Humid │
│                                                  │
│  All 5 params assembled ──► POST /predict        │
├──────────────────────────────────────────────────┤
│           FastAPI Backend (Python)                │
│                                                  │
│  /predict endpoint                               │
│  Random Forest Classifier (.joblib)              │
│  → Returns: SAFE / CAUTION / UNSAFE              │
├──────────────────────────────────────────────────┤
│           Arduino Uno (Hardware)                  │
│                                                  │
│  MQ-137 (Ammonia) ──► Analog A0                  │
│  DHT11 (Temp/Humidity) ──► Digital D2 (optional) │
│  Waits for 'R' command, then sends CSV           │
└──────────────────────────────────────────────────┘
```

**Key Design Decision:** All image processing (QR decoding, color analysis, pH estimation) happens **in the browser** using JavaScript. No OpenCV or server-side image processing is needed. The backend only handles ML inference.

---

## Project Structure

```
SensoPack_ML/
├── server.py                          # FastAPI backend (ML prediction API + static file serving)
├── shrimp_spoilage_model.joblib       # Trained Random Forest model
├── sensopack_colab.py                 # Model training script (Arrhenius kinetics + synthetic data)
├── run.bat                            # One-click launcher (starts server + opens browser)
│
├── webapp/                            # Frontend web application
│   ├── index.html                     # Main dashboard — camera, sensors, scan, results
│   ├── style.css                      # Dark glassmorphism theme
│   ├── app.js                         # 6 JS modules: Camera, QR, Biofilm, Arduino, Demo, Prediction
│   └── qr-generator.html             # Tool to generate + print package QR codes
│
└── arduino/                           # Arduino firmware
    ├── sensopack_sensor_hub/
    │   └── sensopack_sensor_hub.ino   # Production: MQ-137 + DHT11 (on-demand reading)
    └── sensopack_simulator/
        └── sensopack_simulator.ino    # Testing: Simulates sensor data (no hardware needed)
```

---

## Quick Start

### Prerequisites

- **Python 3.8+** with packages: `fastapi`, `uvicorn`, `joblib`, `scikit-learn`, `numpy`
- **Chrome or Edge browser** (required for Web Serial API)
- **Arduino IDE** (for uploading sensor firmware)

### Install Python Dependencies

```bash
pip install fastapi uvicorn joblib scikit-learn numpy
```

### Run the Application

**Option A — Double-click the launcher:**
```
run.bat
```

**Option B — Manual start:**
```bash
cd SensoPack_ML
python -m uvicorn server:app --host 127.0.0.1 --port 8000
```

Then open: **http://127.0.0.1:8000/app**

### Demo Mode (No Hardware Needed)

1. Open the dashboard
2. Check ✅ **Demo Mode** in the Arduino panel
3. Click **📷 Scan Package**
4. The system simulates a random scenario (fresh / boundary / spoiled) and shows the full prediction

---

## QR Code Generation

### Generator Tool

Access at: **http://127.0.0.1:8000/app/qr-generator.html**

Fill in the fields and click **Generate QR Code**. You can download the PNG or print it directly.

### QR Code JSON Format

Each QR code encodes the following JSON:

```json
{
  "batch_id": "SP-2026-0042",
  "product_id": "PKG-001",
  "packaging_time": "2026-08-05T10:30:00.000Z",
  "initial_temp_c": 2.0,
  "location": "Mumbai Cold Storage, Dock 4",
  "notes": "Whiteleg shrimp, 500g"
}
```

| Field | Purpose |
|---|---|
| `batch_id` | Unique batch identifier |
| `product_id` | Individual package ID |
| `packaging_time` | ISO 8601 timestamp — used to auto-compute storage duration |
| `initial_temp_c` | Temperature at time of packaging |
| `location` | Processing facility or origin |
| `notes` | Product description (species, weight, etc.) |

The **storage time** (hours since packaging) is computed automatically as:
```
storage_time_hrs = (current_time − packaging_time) / 3600000
```

---

## Arduino Setup

### Wiring (MQ-137 Only — Minimum Setup)

| Component | Arduino Pin |
|---|---|
| MQ-137 AOUT | **A0** |
| MQ-137 VCC | **5V** |
| MQ-137 GND | **GND** |

### Wiring (Full Setup with DHT11)

| Component | Arduino Pin |
|---|---|
| MQ-137 AOUT | **A0** |
| DHT11 DATA | **D2** |
| Both VCC | **5V** |
| Both GND | **GND** |
| 10kΩ resistor | Between DHT11 DATA and VCC |

If using only the MQ-137, set `#define USE_DHT false` in the sketch (this is the default). The system uses safe defaults for temperature (4°C) and humidity (85%).

### Serial Protocol

The Arduino uses an **on-demand** protocol:
1. Web app sends `R\n` over serial
2. Arduino reads sensors and replies with: `ammonia_ppm,temperature_c,humidity_pct\n`
3. Example: `8.5,4.2,82\n`

Baud rate: **9600**

### Available Sketches

| Sketch | Use Case |
|---|---|
| `sensopack_sensor_hub.ino` | **Production** — reads real MQ-137 + optional DHT11 |
| `sensopack_simulator.ino` | **Testing** — sends fake data, no sensors needed |

---

## ML Model Details

### Algorithm
**Random Forest Classifier** (scikit-learn) — trained on 1500 synthetic samples generated using Arrhenius kinetics modeling for *L. vannamei* spoilage.

### Input Features (5 parameters)

| Feature | Unit | Source | Range |
|---|---|---|---|
| `ammonia_ppm` | ppm | MQ-137 sensor | 0–200 |
| `ph_level` | pH | Biofilm color (camera) | 5.0–9.0 |
| `temperature_c` | °C | DHT11 sensor (or default) | -20–50 |
| `storage_time_hrs` | hours | QR code (computed) | 0–500 |
| `humidity_pct` | % | DHT11 sensor (or default) | 0–100 |

### Output Classes

| Class | Code | Meaning |
|---|---|---|
| **SAFE** | 0 | Product is within safe freshness bounds |
| **CAUTION** | 1 | Product is approaching spoilage threshold |
| **UNSAFE** | 2 | Product has exceeded safe freshness limits |

### API Endpoint

```
POST http://127.0.0.1:8000/predict
Content-Type: application/json

{
  "ammonia_ppm": 2.1,
  "ph_level": 6.8,
  "temperature_c": 2.5,
  "storage_time_hrs": 24,
  "humidity_pct": 83
}
```

Response:
```json
{
  "prediction_code": 0,
  "status_label": "SAFE",
  "confidence_scores": {
    "SAFE": 1.0,
    "CAUTION": 0.0,
    "UNSAFE": 0.0
  },
  "recommended_action": "Product is within safe freshness bounds. Continue storing at recommended chill temperature."
}
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | Vanilla HTML/CSS/JavaScript, jsQR (CDN), qrcodejs (CDN) |
| **Backend** | Python, FastAPI, Uvicorn |
| **ML** | scikit-learn (Random Forest), joblib |
| **Hardware** | Arduino Uno, MQ-137, DHT11, Web Serial API |
| **Design** | Dark glassmorphism, Inter font, responsive layout |

---

## Calibration Notes

### Biofilm pH ↔ Color (Red Cabbage Anthocyanin)

The system converts the biofilm color to pH using this calibration curve:

| pH | Indicator Color | HSV Hue (°) |
|---|---|---|
| 5.0 | Pink / Red | 350° |
| 6.0 | Pink-Purple | 320° |
| 6.8 | Purple (Fresh) | 290° |
| 7.3 | Blue-Purple (Caution) | 260° |
| 7.8 | Blue (Spoiled) | 230° |
| 8.5 | Blue-Green | 200° |

The system uses **piecewise linear interpolation** between these points and handles HSV hue wrap-around (red hues at 0°–30° are treated as 360°+).

### MQ-137 Ammonia Sensor

The MQ-137 analog reading is converted to ppm using:
```
Rs = RL × (1023 − analogReading) / analogReading
ratio = Rs / R0
log₁₀(ppm) = slope × log₁₀(ratio) + intercept
```

Default calibration constants (tune R0 for your sensor):
- `RL = 10 kΩ`, `R0 = 30 kΩ` (calibrate in clean air)
- `slope = -3.32`, `intercept = 1.0`

---

## License

This project was developed for academic/research purposes as part of a smart packaging study for *Litopenaeus vannamei* freshness monitoring.
