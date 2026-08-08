/**
 * SensoPack v2.0 — Automated Package Scanning System
 *
 * Modules:
 *  1. Camera Manager   — webcam preview + frame capture
 *  2. QR Decoder       — jsQR-based QR code reading + metadata extraction
 *  3. Biofilm Analyzer — color detection, RGB→HSV, Hue→pH calibration
 *  4. Arduino Serial   — Web Serial API for live sensor readings
 *  5. Prediction       — orchestrate all modules → POST /predict → render result
 */

const API_URL = window.location.origin.startsWith("http")
  ? `${window.location.origin}/predict`
  : "http://127.0.0.1:8000/predict";

// ═══════════════════════════════════════════════════════════
// DOM References
// ═══════════════════════════════════════════════════════════
const dom = {
  // Camera
  video:          document.getElementById("camera-video"),
  canvas:         document.getElementById("camera-canvas"),
  cameraOverlay:  document.getElementById("camera-overlay"),
  cameraPanel:    document.getElementById("camera-panel"),
  scanBtn:        document.getElementById("scan-btn"),

  // Arduino
  connectBtn:     document.getElementById("connect-btn"),
  arduinoDot:     document.getElementById("arduino-dot"),
  arduinoStatus:  document.getElementById("arduino-status-text"),
  valAmmonia:     document.getElementById("val-ammonia"),
  valTemp:        document.getElementById("val-temp"),
  valHumidity:    document.getElementById("val-humidity"),

  // Demo
  demoToggle:     document.getElementById("demo-mode-toggle"),

  // Steps
  step1:          document.getElementById("step-1"),
  step2:          document.getElementById("step-2"),
  step3:          document.getElementById("step-3"),

  // Summary - QR Info
  scanSummary:    document.getElementById("scan-summary"),
  sumBatch:       document.getElementById("sum-batch"),
  sumProduct:     document.getElementById("sum-product"),
  sumPacktime:    document.getElementById("sum-packtime"),
  sumInittemp:    document.getElementById("sum-inittemp"),
  sumLocation:    document.getElementById("sum-location"),
  sumNotes:       document.getElementById("sum-notes"),
  // Summary - Sensor Data
  sumStorage:     document.getElementById("sum-storage"),
  sumStorageDetail: document.getElementById("sum-storage-detail"),
  sumBiofilm:     document.getElementById("sum-biofilm"),
  sumBiofilmDetail: document.getElementById("sum-biofilm-detail"),
  sumPh:          document.getElementById("sum-ph"),
  sumPhDetail:    document.getElementById("sum-ph-detail"),
  sumAmmonia:     document.getElementById("sum-ammonia"),
  sumTemp:        document.getElementById("sum-temp"),
  sumHumidity:    document.getElementById("sum-humidity"),

  // Result
  resultPanel:    document.getElementById("result-panel"),
  statusBadge:    document.getElementById("status-badge"),
  statusIcon:     document.getElementById("status-icon"),
  statusLabel:    document.getElementById("status-label"),
  confSafe:       document.getElementById("conf-safe"),
  confCaution:    document.getElementById("conf-caution"),
  confUnsafe:     document.getElementById("conf-unsafe"),
  barSafe:        document.getElementById("bar-safe"),
  barCaution:     document.getElementById("bar-caution"),
  barUnsafe:      document.getElementById("bar-unsafe"),

  // Main layout
  mainView:       document.getElementById("main-view"),

  // Toasts
  errorToast:     document.getElementById("error-toast"),
  infoToast:      document.getElementById("info-toast"),
};

function resetApp() {
  dom.mainView.classList.remove("hidden");
  dom.resultPanel.classList.add("hidden");
  dom.step3.classList.remove("active");
  dom.scanBtn.disabled = false;
}

// ═══════════════════════════════════════════════════════════
// MODULE 1: Camera Manager
// ═══════════════════════════════════════════════════════════
const Camera = {
  stream: null,
  ready: false,

  async init() {
    try {
      this.stream = await navigator.mediaDevices.getUserMedia({
        video: { facingMode: "environment", width: { ideal: 1280 }, height: { ideal: 720 } }
      });
      dom.video.srcObject = this.stream;
      await dom.video.play();
      this.ready = true;
      dom.cameraOverlay.classList.add("camera-overlay--hidden");
      dom.scanBtn.disabled = false;
      showInfo("Camera ready");
    } catch (err) {
      console.warn("Camera init failed:", err);
      dom.cameraOverlay.innerHTML =
        '<div class="camera-overlay__icon">⚠️</div><div>Camera unavailable — use Demo Mode</div>';
    }
  },

  captureFrame() {
    const ctx = dom.canvas.getContext("2d");
    dom.canvas.width = dom.video.videoWidth;
    dom.canvas.height = dom.video.videoHeight;
    ctx.drawImage(dom.video, 0, 0);
    return ctx.getImageData(0, 0, dom.canvas.width, dom.canvas.height);
  }
};


// ═══════════════════════════════════════════════════════════
// MODULE 2: QR Decoder
// ═══════════════════════════════════════════════════════════
const QRDecoder = {
  /**
   * Decode QR code from ImageData.
   * Returns { data: parsedJSON, location: {topLeft, topRight, bottomLeft, bottomRight}, raw: string }
   * or null if not found.
   */
  decode(imageData) {
    if (typeof jsQR === "undefined") {
      showError("QR decoder library (jsQR) not loaded. Check your internet connection.");
      return null;
    }
    const code = jsQR(imageData.data, imageData.width, imageData.height, {
      inversionAttempts: "dontInvert"
    });

    if (!code) return null;

    let parsed = null;
    try {
      parsed = JSON.parse(code.data);
    } catch {
      // QR contains non-JSON — treat the whole string as a simple identifier
      parsed = { raw_text: code.data };
    }

    return {
      data: parsed,
      location: code.location,
      raw: code.data
    };
  },

  /**
   * Compute storage time in hours from packaging_time ISO string.
   */
  computeStorageHours(packagingTimeISO) {
    const packTime = new Date(packagingTimeISO);
    if (isNaN(packTime.getTime())) return null;
    const now = new Date();
    return Math.max(0, (now - packTime) / 3600000); // ms → hrs
  }
};


// ═══════════════════════════════════════════════════════════
// MODULE 3: Biofilm Color Analyzer
// ═══════════════════════════════════════════════════════════
const BiofilmAnalyzer = {

  /**
   * pH ↔ Hue calibration points (Red Cabbage Anthocyanin basis).
   * Hue in degrees [0–360], pH values.
   */
  PH_CALIBRATION: [
    { hue: 200, ph: 8.5 }, // Blue-Green
    { hue: 230, ph: 7.8 }, // Blue (Spoiled)
    { hue: 260, ph: 7.3 }, // Purple-Blue (Caution)
    { hue: 290, ph: 6.8 }, // Purple (Fresh)
    { hue: 320, ph: 6.0 }, // Pink-Purple
    { hue: 350, ph: 5.0 }, // Pink/Red
  ],

  /**
   * Convert RGB [0-255] to HSV { h:[0-360], s:[0-100], v:[0-100] }
   */
  rgbToHsv(r, g, b) {
    r /= 255; g /= 255; b /= 255;
    const max = Math.max(r, g, b), min = Math.min(r, g, b);
    const d = max - min;
    let h = 0, s = max === 0 ? 0 : d / max, v = max;

    if (d !== 0) {
      switch (max) {
        case r: h = ((g - b) / d + (g < b ? 6 : 0)); break;
        case g: h = ((b - r) / d + 2); break;
        case b: h = ((r - g) / d + 4); break;
      }
      h /= 6;
    }
    return { h: h * 360, s: s * 100, v: v * 100 };
  },

  /**
   * Piecewise linear interpolation: Hue → pH
   */
  hueToPh(hue) {
    // Normalize red hue wrap-around: hues 0°-100° belong to the red/pink 350°+ range
    if (hue < 100) hue += 360;

    const pts = this.PH_CALIBRATION;
    if (hue <= pts[0].hue) return pts[0].ph;
    if (hue >= pts[pts.length - 1].hue) return pts[pts.length - 1].ph;

    for (let i = 0; i < pts.length - 1; i++) {
      if (hue >= pts[i].hue && hue <= pts[i + 1].hue) {
        const t = (hue - pts[i].hue) / (pts[i + 1].hue - pts[i].hue);
        return pts[i].ph + t * (pts[i + 1].ph - pts[i].ph);
      }
    }
    return 7.0; // fallback
  },

  /**
   * Detect the biofilm color region from the image using a 20-point grid.
   * Filters out the QR code area and white/grey background.
   */
  analyze(imageData, qrLocation) {
    const { data, width, height } = imageData;

    // Package alignment guide dimensions (must match CSS)
    const guideW = 380;
    const guideH = 180;
    const startX = Math.max(0, Math.floor((width - guideW) / 2));
    const startY = Math.max(0, Math.floor((height - guideH) / 2));

    // Build QR bounding box (with padding) to exclude
    let qrMinX = 0, qrMaxX = 0, qrMinY = 0, qrMaxY = 0;
    if (qrLocation) {
      const pts = [qrLocation.topLeftCorner, qrLocation.topRightCorner,
                   qrLocation.bottomLeftCorner, qrLocation.bottomRightCorner];
      const xs = pts.map(p => p.x), ys = pts.map(p => p.y);
      const pad = 30;
      qrMinX = Math.min(...xs) - pad;
      qrMaxX = Math.max(...xs) + pad;
      qrMinY = Math.min(...ys) - pad;
      qrMaxY = Math.max(...ys) + pad;
    }

    // Grid of 5x4 = 20 sampling points inside the guide box
    const cols = 5, rows = 4;
    const dx = guideW / cols;
    const dy = guideH / rows;

    let totalR = 0, totalG = 0, totalB = 0, validPoints = 0;

    for (let gy = 0; gy < rows; gy++) {
      for (let gx = 0; gx < cols; gx++) {
        const px = Math.floor(startX + gx * dx + dx / 2);
        const py = Math.floor(startY + gy * dy + dy / 2);

        // Skip if inside QR code region
        if (qrLocation && px >= qrMinX && px <= qrMaxX && py >= qrMinY && py <= qrMaxY) {
          continue;
        }

        // Average a 5x5 area around the point to avoid single-pixel noise
        let blockR = 0, blockG = 0, blockB = 0, count = 0;
        for (let y = py - 2; y <= py + 2; y++) {
          for (let x = px - 2; x <= px + 2; x++) {
            if (x < 0 || x >= width || y < 0 || y >= height) continue;
            const idx = (y * width + x) * 4;
            blockR += data[idx];
            blockG += data[idx + 1];
            blockB += data[idx + 2];
            count++;
          }
        }

        if (count > 0) {
          const ptR = blockR / count;
          const ptG = blockG / count;
          const ptB = blockB / count;
          const ptHsv = this.rgbToHsv(ptR, ptG, ptB);
          
          // Only include points with actual color (skip white background, s > 15)
          if (ptHsv.s > 15) {
            totalR += ptR;
            totalG += ptG;
            totalB += ptB;
            validPoints++;
          }
        }
      }
    }

    if (validPoints === 0) return null;

    const avgR = Math.round(totalR / validPoints);
    const avgG = Math.round(totalG / validPoints);
    const avgB = Math.round(totalB / validPoints);

    const hsv = this.rgbToHsv(avgR, avgG, avgB);
    const ph = this.hueToPh(hsv.h);

    return {
      rgb: { r: avgR, g: avgG, b: avgB },
      hsv: { h: Math.round(hsv.h), s: Math.round(hsv.s), v: Math.round(hsv.v) },
      ph: Math.round(ph * 100) / 100
    };
  }
};


// ═══════════════════════════════════════════════════════════
// MODULE 4: Arduino Serial (Web Serial API)
// ═══════════════════════════════════════════════════════════
const Arduino = {
  port: null,
  reader: null,
  connected: false,
  latestValues: { ammonia_ppm: null, temperature_c: null, humidity_pct: null },
  buffer: "",

  onDataReceived: null,

  async connect() {
    if (!("serial" in navigator)) {
      showError("Web Serial API not supported. Use Chrome or Edge browser.");
      return;
    }

    try {
      this.port = await navigator.serial.requestPort();
      await this.port.open({ baudRate: 9600 });
      this.connected = true;
      this.updateUI(true);
      showInfo("Arduino connected! Waiting for scan...");
      updateSteps();
      this.startReading();
    } catch (err) {
      if (err.name !== "NotFoundError") { // User cancelled port picker
        showError("Arduino connection failed: " + err.message);
      }
    }
  },

  async requestData() {
    if (!this.port) return false;
    try {
      // Send "R\n" to request data
      const writer = this.port.writable.getWriter();
      const encoder = new TextEncoder();
      await writer.write(encoder.encode("R\n"));
      writer.releaseLock();

      // Wait up to 3 seconds for the response
      return new Promise((resolve) => {
        let timer = setTimeout(() => {
          this.onDataReceived = null;
          resolve(false);
        }, 3000);

        this.onDataReceived = () => {
          clearTimeout(timer);
          resolve(true);
        };
      });
    } catch (err) {
      console.error("Failed to request data:", err);
      return false;
    }
  },

  async startReading() {
    const decoder = new TextDecoderStream();
    const readable = this.port.readable.pipeTo(decoder.writable);
    this.reader = decoder.readable.getReader();

    try {
      while (true) {
        const { value, done } = await this.reader.read();
        if (done) break;
        this.buffer += value;
        this.processBuffer();
      }
    } catch (err) {
      console.error("Serial read error:", err);
    } finally {
      this.connected = false;
      this.updateUI(false);
    }
  },

  /**
   * Parse incoming serial data.
   * Expected format: "ammonia_ppm,temperature_c,humidity_pct\n"
   * Example: "8.5,4.2,82\n"
   */
  processBuffer() {
    const lines = this.buffer.split("\n");
    // Keep the last incomplete line in the buffer
    this.buffer = lines.pop() || "";

    for (const line of lines) {
      const trimmed = line.trim();
      if (!trimmed) continue;

      const parts = trimmed.split(",").map(s => parseFloat(s.trim()));
      if (parts.length >= 3 && parts.every(v => !isNaN(v))) {
        this.latestValues.ammonia_ppm = parts[0];
        this.latestValues.temperature_c = parts[1];
        this.latestValues.humidity_pct = parts[2];
        this.displayValues();
        if (this.onDataReceived) {
          this.onDataReceived();
          this.onDataReceived = null;
        }
      }
    }
  },

  displayValues() {
    const { ammonia_ppm, temperature_c, humidity_pct } = this.latestValues;

    if (ammonia_ppm !== null) {
      dom.valAmmonia.textContent = ammonia_ppm.toFixed(1) + " ppm";
      dom.valAmmonia.classList.remove("sensor-readout__value--waiting");
      flashReadout("readout-ammonia");
    }
    if (temperature_c !== null) {
      dom.valTemp.textContent = temperature_c.toFixed(1) + " °C";
      dom.valTemp.classList.remove("sensor-readout__value--waiting");
      flashReadout("readout-temp");
    }
    if (humidity_pct !== null) {
      dom.valHumidity.textContent = humidity_pct.toFixed(0) + " %";
      dom.valHumidity.classList.remove("sensor-readout__value--waiting");
      flashReadout("readout-humidity");
    }
  },

  updateUI(connected) {
    if (connected) {
      dom.arduinoDot.classList.add("status-dot--connected");
      dom.arduinoStatus.textContent = "Connected";
      dom.connectBtn.textContent = "✅ Arduino Connected";
      dom.connectBtn.classList.add("connect-btn--connected");
    } else {
      dom.arduinoDot.classList.remove("status-dot--connected");
      dom.arduinoStatus.textContent = "Disconnected";
      dom.connectBtn.textContent = "🔌 Connect Arduino";
      dom.connectBtn.classList.remove("connect-btn--connected");
    }
  },

  hasData() {
    return this.latestValues.ammonia_ppm !== null;
  }
};


// ═══════════════════════════════════════════════════════════
// MODULE 5: Demo Mode (for presentations without hardware)
// ═══════════════════════════════════════════════════════════
const DemoMode = {
  enabled: false,

  toggle(on) {
    this.enabled = on;
    if (on) {
      // Simulate Arduino data
      Arduino.latestValues = {
        ammonia_ppm: 3.2 + Math.random() * 2,
        temperature_c: 2.0 + Math.random() * 3,
        humidity_pct: 78 + Math.random() * 10
      };
      Arduino.connected = true;
      Arduino.updateUI(true);
      Arduino.displayValues();
      dom.scanBtn.disabled = false;
      showInfo("Demo mode active — sensors simulated");
      updateSteps();
    } else {
      if (!Arduino.port) {
        Arduino.connected = false;
        Arduino.latestValues = { ammonia_ppm: null, temperature_c: null, humidity_pct: null };
        Arduino.updateUI(false);
        dom.valAmmonia.textContent = "waiting...";
        dom.valAmmonia.classList.add("sensor-readout__value--waiting");
        dom.valTemp.textContent = "waiting...";
        dom.valTemp.classList.add("sensor-readout__value--waiting");
        dom.valHumidity.textContent = "waiting...";
        dom.valHumidity.classList.add("sensor-readout__value--waiting");
      }
      updateSteps();
    }
  },

  /**
   * Generate simulated scan results (QR + biofilm).
   * Randomly picks from fresh, boundary, or spoiled scenarios.
   */
  generateScanData() {
    const scenarios = [
      {
        name: "fresh",
        qr: { batch_id: "SP-2026-0042", product_id: "PKG-001",
               packaging_time: new Date(Date.now() - 24 * 3600000).toISOString(),
               initial_temp_c: 2.0, location: "Mumbai Cold Storage, Dock 4",
               notes: "Whiteleg shrimp, 500g" },
        biofilm: { rgb: { r: 120, g: 40, b: 160 }, hsv: { h: 280, s: 75, v: 62 }, ph: 6.9 },
        sensors: { ammonia_ppm: 2.1, temperature_c: 2.5, humidity_pct: 83 }
      },
      {
        name: "boundary",
        qr: { batch_id: "SP-2026-0038", product_id: "PKG-015",
               packaging_time: new Date(Date.now() - 130 * 3600000).toISOString(),
               initial_temp_c: 4.0, location: "Kochi Fish Market, Unit 2",
               notes: "Whiteleg shrimp, 300g" },
        biofilm: { rgb: { r: 80, g: 60, b: 180 }, hsv: { h: 250, s: 66, v: 70 }, ph: 7.4 },
        sensors: { ammonia_ppm: 9.5, temperature_c: 7.8, humidity_pct: 88 }
      },
      {
        name: "spoiled",
        qr: { batch_id: "SP-2026-0031", product_id: "PKG-022",
               packaging_time: new Date(Date.now() - 200 * 3600000).toISOString(),
               initial_temp_c: 8.0, location: "Chennai Aqua Processing, Bay 7",
               notes: "Whiteleg shrimp, 500g" },
        biofilm: { rgb: { r: 40, g: 80, b: 200 }, hsv: { h: 225, s: 80, v: 78 }, ph: 7.9 },
        sensors: { ammonia_ppm: 25.0, temperature_c: 18.0, humidity_pct: 78 }
      }
    ];

    const pick = scenarios[Math.floor(Math.random() * scenarios.length)];

    // Update displayed sensor values
    Arduino.latestValues = { ...pick.sensors };
    Arduino.displayValues();

    return {
      qr: { data: pick.qr, raw: JSON.stringify(pick.qr) },
      biofilm: pick.biofilm,
      storageHrs: QRDecoder.computeStorageHours(pick.qr.packaging_time)
    };
  }
};


// ═══════════════════════════════════════════════════════════
// MODULE 6: Prediction Pipeline
// ═══════════════════════════════════════════════════════════

async function runScan() {
  const btn = dom.scanBtn;
  btn.disabled = true;
  btn.textContent = "⏳ Scanning...";
  dom.cameraPanel.classList.add("scan-active");

  // Hide previous results
  dom.scanSummary.classList.add("hidden");
  dom.resultPanel.classList.add("hidden");

  try {
    let qrResult, biofilmResult, storageHrs;

    if (DemoMode.enabled) {
      // Demo mode — simulate everything
      await sleep(1200); // Fake processing delay
      const sim = DemoMode.generateScanData();
      qrResult = sim.qr;
      biofilmResult = sim.biofilm;
      storageHrs = sim.storageHrs;
    } else {
      // Real mode — capture and process
      if (!Camera.ready) { showError("Camera not available"); return; }
      if (!Arduino.connected) {
        showError("Arduino not connected");
        return;
      }
      
      btn.textContent = "⏳ Scanning Package...";
      let imageData = null;
      qrResult = null;
      
      // Try scanning for up to 5 seconds to allow for auto-focus
      const startTime = Date.now();
      while (Date.now() - startTime < 5000) {
        imageData = Camera.captureFrame();
        qrResult = QRDecoder.decode(imageData);
        if (qrResult) break;
        await new Promise(resolve => setTimeout(resolve, 150));
      }

      if (!qrResult) { 
        showError("No QR code detected — ensure it is in focus and well-lit"); 
        return; 
      }

      // Compute storage time
      if (qrResult.data.packaging_time) {
        storageHrs = QRDecoder.computeStorageHours(qrResult.data.packaging_time);
      }
      if (storageHrs === null || storageHrs === undefined) {
        showError("QR code missing packaging_time field");
        return;
      }

      // Analyze biofilm color from the successful frame
      biofilmResult = BiofilmAnalyzer.analyze(imageData, qrResult.location);
      if (!biofilmResult) {
        showError("Could not detect biofilm color — ensure the indicator is visible");
        return;
      }

      // Request fresh data from Arduino (after visual is done)
      btn.textContent = "⏳ Reading Sensors...";
      const gotData = await Arduino.requestData();
      if (!gotData || !Arduino.hasData()) {
        showError("Failed to get fresh sensor data from Arduino.");
        return;
      }
    }

    // ── Populate scan summary ──
    populateSummary(qrResult, biofilmResult, storageHrs);
    dom.scanSummary.classList.remove("hidden");

    // ── Build ML payload ──
    const payload = {
      ammonia_ppm:      Arduino.latestValues.ammonia_ppm,
      ph_level:         biofilmResult.ph,
      temperature_c:    Arduino.latestValues.temperature_c,
      storage_time_hrs: storageHrs,
      humidity_pct:     Arduino.latestValues.humidity_pct
    };

    console.log("ML Payload:", payload);

    // ── Call prediction API ──
    btn.textContent = "🧠 Predicting...";
    const response = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    if (!response.ok) {
      const err = await response.json().catch(() => ({}));
      throw new Error(err.detail || `Server returned ${response.status}`);
    }

    const result = await response.json();
    renderResult(result);
    dom.resultPanel.classList.remove("hidden");

    // Update steps
    setStep(3);
    showInfo("Prediction complete!");

  } catch (err) {
    console.error("Scan error:", err);
    if (err.message.includes("Failed to fetch") || err.message.includes("NetworkError")) {
      showError("Cannot reach API server. Is the backend running on port 8000?");
    } else {
      showError(err.message);
    }
  } finally {
    btn.disabled = false;
    btn.textContent = "📷 Scan Package";
    dom.cameraPanel.classList.remove("scan-active");
  }
}


// ═══════════════════════════════════════════════════════════
// UI Helpers
// ═══════════════════════════════════════════════════════════

const STATUS_CONFIG = {
  SAFE:    { css: "status-badge--safe",    icon: "✅", border: "var(--safe-border)" },
  CAUTION: { css: "status-badge--caution", icon: "⚠️", border: "var(--caution-border)" },
  UNSAFE:  { css: "status-badge--unsafe",  icon: "🚫", border: "var(--unsafe-border)" },
};

function populateSummary(qr, biofilm, storageHrs) {
  const d = qr.data;

  // ── Package Info from QR ──
  dom.sumBatch.textContent     = d.batch_id   || "—";
  dom.sumProduct.textContent   = d.product_id || "—";
  dom.sumLocation.textContent  = d.location   || d.origin || "—";
  dom.sumNotes.textContent     = d.notes      || "—";

  // Packaging time — display human-readable
  if (d.packaging_time) {
    const pt = new Date(d.packaging_time);
    dom.sumPacktime.textContent = pt.toLocaleString();
  } else {
    dom.sumPacktime.textContent = "—";
  }

  // Initial temp
  if (d.initial_temp_c !== undefined && d.initial_temp_c !== null) {
    dom.sumInittemp.textContent = d.initial_temp_c + " °C";
  } else {
    dom.sumInittemp.textContent = "—";
  }

  // Storage time
  dom.sumStorage.textContent = storageHrs.toFixed(1) + " hrs";
  const days = (storageHrs / 24).toFixed(1);
  dom.sumStorageDetail.textContent = `≈ ${days} days since packaging`;

  // Biofilm
  const { r, g, b } = biofilm.rgb;
  dom.sumBiofilm.innerHTML =
    `<span class="biofilm-swatch" style="background:rgb(${r},${g},${b})"></span>` +
    `RGB(${r}, ${g}, ${b})`;
  dom.sumBiofilmDetail.textContent = `HSV(${biofilm.hsv.h}°, ${biofilm.hsv.s}%, ${biofilm.hsv.v}%)`;

  // pH
  dom.sumPh.textContent = biofilm.ph.toFixed(2);
  const phStatus = biofilm.ph <= 7.2 ? "Fresh range" : biofilm.ph <= 7.5 ? "Caution range" : "Spoiled range";
  dom.sumPhDetail.textContent = phStatus;

  // Sensor values (null-safe)
  const lv = Arduino.latestValues;
  dom.sumAmmonia.textContent  = lv.ammonia_ppm !== null ? lv.ammonia_ppm.toFixed(1) + " ppm" : "—";
  dom.sumTemp.textContent     = lv.temperature_c !== null ? lv.temperature_c.toFixed(1) + " °C" : "—";
  dom.sumHumidity.textContent = lv.humidity_pct !== null ? lv.humidity_pct.toFixed(0) + " %" : "—";
}

function renderResult(data) {
  const cfg = STATUS_CONFIG[data.status_label] || STATUS_CONFIG.SAFE;

  // Badge
  dom.statusBadge.className = "status-badge " + cfg.css;
  dom.statusBadge.style.animation = "none";
  dom.statusBadge.offsetHeight; // reflow
  dom.statusBadge.style.animation = "";
  dom.statusIcon.textContent = cfg.icon;
  dom.statusLabel.textContent = data.status_label;

  // Confidence
  const s = data.confidence_scores;
  dom.confSafe.textContent    = ((s.SAFE    || 0) * 100).toFixed(1) + "%";
  dom.confCaution.textContent = ((s.CAUTION || 0) * 100).toFixed(1) + "%";
  dom.confUnsafe.textContent  = ((s.UNSAFE  || 0) * 100).toFixed(1) + "%";

  dom.barSafe.style.width = dom.barCaution.style.width = dom.barUnsafe.style.width = "0%";
  requestAnimationFrame(() => requestAnimationFrame(() => {
    dom.barSafe.style.width    = ((s.SAFE    || 0) * 100) + "%";
    dom.barCaution.style.width = ((s.CAUTION || 0) * 100) + "%";
    dom.barUnsafe.style.width  = ((s.UNSAFE  || 0) * 100) + "%";
  }));

  // Hide camera view, show results
  dom.mainView.classList.add("hidden");
  dom.resultPanel.classList.remove("hidden");
  window.scrollTo(0, 0); // Scroll to top since we swapped views
  
  // Mark Step 3 as completed (green)
  setStep(4);
}

function setStep(num) {
  [dom.step1, dom.step2, dom.step3].forEach((el, i) => {
    el.classList.remove("step--active", "step--done");
    if (i + 1 < num) el.classList.add("step--done");
    else if (i + 1 === num) el.classList.add("step--active");
  });
}

function updateSteps() {
  if (Arduino.connected || DemoMode.enabled) {
    setStep(2);
  } else {
    setStep(1);
  }
}

function flashReadout(id) {
  const el = document.getElementById(id);
  el.classList.add("sensor-readout--updated");
  setTimeout(() => el.classList.remove("sensor-readout--updated"), 600);
}

// ── Toasts ──
let errorTimeout = null, infoTimeout = null;

function showError(msg) {
  dom.errorToast.textContent = msg;
  dom.errorToast.classList.add("error-toast--visible");
  if (errorTimeout) clearTimeout(errorTimeout);
  errorTimeout = setTimeout(() => dom.errorToast.classList.remove("error-toast--visible"), 5000);
}

function showInfo(msg) {
  dom.infoToast.textContent = msg;
  dom.infoToast.classList.add("info-toast--visible");
  if (infoTimeout) clearTimeout(infoTimeout);
  infoTimeout = setTimeout(() => dom.infoToast.classList.remove("info-toast--visible"), 3000);
}

function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }


function resetScanner() {
  // Hide results
  dom.scanSummary.classList.add("hidden");
  dom.resultPanel.classList.add("hidden");
  
  // Show camera view
  dom.mainView.classList.remove("hidden");
  
  // Reset steps and button
  updateSteps();
  dom.scanBtn.disabled = false;
  dom.scanBtn.textContent = "📷 Scan Package";
  dom.cameraPanel.classList.remove("scan-active");
  
  window.scrollTo(0, 0);
}

// ═══════════════════════════════════════════════════════════
// Event Listeners & Initialization
// ═══════════════════════════════════════════════════════════

dom.connectBtn.addEventListener("click", () => Arduino.connect());
// Expose for inline onclick handler
window.resetScanner = resetScanner;
dom.scanBtn.addEventListener("click", () => runScan());
dom.demoToggle.addEventListener("change", (e) => DemoMode.toggle(e.target.checked));

// Initialize camera on page load
Camera.init();

console.log(
  "%c🦐 SensoPack v2.0 — Smart Package Scanner",
  "color: #818cf8; font-size: 14px; font-weight: bold;"
);
