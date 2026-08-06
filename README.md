# SensoPack v2.0

SensoPack v2.0 is an AI-powered smart packaging system for fresh perishable food (such as *L. vannamei* shrimp). It combines a biodegradable bioactive film, a colorimetric pH indicator (Anthocyanin), and live sensor data (Ammonia, Temperature, Humidity) to predict food freshness in real time.

This project is structured for a **distributed cloud architecture** where a mobile phone acts as the scanner, the laptop acts as a sensor bridge, and a Vercel serverless backend runs the ML model.

## System Architecture

1. **Mobile Frontend (Vercel)**: A static HTML/JS web app accessed via a mobile phone. It uses the phone camera to scan a QR code for metadata (batch ID, packaging time) and the color of the bioactive film (for pH).
2. **Laptop Bridge**: A Python script (`arduino_bridge.py`) running on the computer connected to the Arduino via USB (`COM12`). It continuously reads sensor data (AHT20 Temp/Humidity and MQ-137 Ammonia) and pushes it to Firebase Realtime Database.
3. **Cloud Backend (Vercel Serverless API)**: A Python FastAPI application running on Vercel. When the mobile app requests a prediction, the backend fetches the latest sensor data from Firebase, runs it through a Random Forest Classifier (`shrimp_spoilage_model.joblib`), and returns the freshness score.

## Directory Structure

```text
SensoPack_ML/
├── api/
│   ├── index.py                  # Vercel Serverless Backend (FastAPI)
│   └── requirements.txt          # Python dependencies for Vercel
├── webapp/                       # Static Frontend Files (HTML, JS, CSS)
│   ├── index.html
│   ├── app.js
│   ├── style.css
│   └── qr-generator.html
├── arduino_bridge.py             # Laptop script to bridge Arduino to Firebase
├── shrimp_spoilage_model.joblib  # Pre-trained Random Forest ML Model
├── PJSketch/                     # Production Arduino Sketch (MQ-137 + AHT20)
├── PJSketch_Simulator/           # Simulator Arduino Sketch (No sensors needed)
└── Sensor_Test/                  # Hardware testing Arduino Sketch
```

## Setup & Deployment

### 1. Firebase Setup
1. Create a Firebase project at [console.firebase.google.com](https://console.firebase.google.com).
2. Enable the **Realtime Database** and start it in "Test Mode".
3. Note your Database URL (e.g., `https://your-project.firebaseio.com/`).
4. Go to Project Settings -> Service Accounts, and click **Generate New Private Key**. Save the JSON file as `serviceAccountKey.json` in the root of this project (do not commit it to Git!).

### 2. Vercel Deployment (Frontend + Backend)
1. Initialize a Git repository, commit your code, and push to GitHub.
2. Go to Vercel and import your GitHub repository.
3. In Vercel's Environment Variables, add:
   - `FIREBASE_URL`: Your Realtime Database URL.
   - `FIREBASE_CREDENTIALS`: The raw JSON string of your `serviceAccountKey.json`.
4. Deploy! Vercel will automatically serve `/webapp` as static files and `/api/index.py` as the Python backend.

### 3. Laptop Bridge Setup
1. Ensure your Arduino is connected to `COM12` and flashed with `PJSketch.ino`.
2. Install dependencies: `pip install pyserial firebase-admin`
3. Make sure `serviceAccountKey.json` is in the folder.
4. Run: `python arduino_bridge.py`

## Usage Workflow
1. Start `arduino_bridge.py` on your laptop.
2. Generate and print a QR code using `/webapp/qr-generator.html`.
3. Open the Vercel app URL on your mobile phone.
4. Tap **Scan Package**, align the QR code and biofilm within the frame.
5. The phone grabs the visual data, queries the Vercel backend, which grabs the live sensor data from Firebase, and displays the prediction on your phone!
