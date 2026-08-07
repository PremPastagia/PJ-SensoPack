/**
 * SensoPack v2.0 — Automated Package Scanning System (Cloud Architecture)
 *
 * Modules:
 *  1. Camera Manager   — webcam preview + frame capture
 *  2. QR Decoder       — jsQR-based QR code reading + metadata extraction
 *  3. Biofilm Analyzer — color detection, RGB→HSV, Hue→pH calibration
 *  4. Prediction       — orchestrate scanning → POST /api/predict → render result
 */

const API_URL = window.location.origin.startsWith("http")
  ? `${window.location.origin}/api/predict`
  : "http://127.0.0.1:8000/api/predict";

// ═══════════════════════════════════════════════════════════
// DOM References
// ═══════════════════════════════════════════════════════════
const dom = {
  // Camera
  video:          document.getElementById("camera-video"),
  canvas:         document.getElementById("camera-canvas"),
  cameraOverlay:  document.getElementById("camera-overlay"),
  cameraPanel:    document.getElementById("camera-wrapper"),
  scanBtn:        document.getElementById("scan-btn"),

  // File Upload
  imageUpload:    document.getElementById("image-upload"),

  // Manual Inputs
  ammoniaSlider:  document.getElementById("ammonia-slider"),
  ammoniaVal:     document.getElementById("ammonia-val-text"),
  ammoniaTooltip: document.getElementById("ammonia-tooltip"),

  // Summary Fields
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
  recAction:      document.getElementById("recommended-action"),

  // Main layout
  mainView:       document.getElementById("main-view"),

  // Toasts
  errorToast:     document.getElementById("error-toast"),
  infoToast:      document.getElementById("info-toast"),
};

function resetScanner() {
  dom.mainView.classList.remove("hidden");
  dom.resultPanel.classList.add("hidden");
  dom.scanSummary.classList.add("hidden");
  dom.scanBtn.disabled = false;
  dom.scanBtn.textContent = "📷 Scan Package";
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
      parsed = { raw_text: code.data };
    }

    return {
      data: parsed,
      location: code.location,
      raw: code.data
    };
  },

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
  PH_CALIBRATION: [
    { hue: 200, ph: 8.5 },
    { hue: 230, ph: 7.8 },
    { hue: 260, ph: 7.3 },
    { hue: 290, ph: 6.8 },
    { hue: 320, ph: 6.0 },
    { hue: 350, ph: 5.0 },
  ],

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

  hueToPh(hue) {
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
    return 7.0;
  },

  analyze(imageData, qrLocation) {
    const { data, width, height } = imageData;
    const guideW = 380;
    const guideH = 180;
    const startX = Math.max(0, Math.floor((width - guideW) / 2));
    const startY = Math.max(0, Math.floor((height - guideH) / 2));

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

    const cols = 5, rows = 4;
    const dx = guideW / cols;
    const dy = guideH / rows;

    let totalR = 0, totalG = 0, totalB = 0, validPoints = 0;

    for (let gy = 0; gy < rows; gy++) {
      for (let gx = 0; gx < cols; gx++) {
        const px = Math.floor(startX + gx * dx + dx / 2);
        const py = Math.floor(startY + gy * dy + dy / 2);

        if (qrLocation && px >= qrMinX && px <= qrMaxX && py >= qrMinY && py <= qrMaxY) {
          continue;
        }

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
// UI Event Handlers
// ═══════════════════════════════════════════════════════════
const UIManager = {
  init() {
    const slider = document.getElementById("ammonia-slider");
    const valDisplay = document.getElementById("ammonia-val");
    if (slider && valDisplay) {
      dom.ammoniaSlider.addEventListener("input", (e) => {
      const val = parseFloat(e.target.value).toFixed(1);
      dom.ammoniaVal.textContent = `${val} ppm`;
      
      if (dom.ammoniaTooltip) {
        dom.ammoniaTooltip.textContent = `${val} ppm`;
        const percent = (e.target.value - e.target.min) / (e.target.max - e.target.min);
        // Map 0-1 to something like 2% - 98% to stay within thumb bounds
        const mappedPos = percent * 96 + 2;
        dom.ammoniaTooltip.style.left = `calc(${mappedPos}% - 0px)`;
      }
    });
    }

    const fileInput = document.getElementById("image-upload");
    if (fileInput) {
      fileInput.addEventListener("change", async (e) => {
        if (e.target.files && e.target.files[0]) {
          await this.processImageUpload(e.target.files[0]);
        }
      });
    }
  },

  /**
   * Processes a manually uploaded image file to extract QR and biofilm data.
   * @param {File} file 
   */
  async processImageUpload(file) {
    dom.scanBtn.disabled = true;
    dom.scanBtn.textContent = "⏳ Processing Image...";
    dom.scanSummary.classList.add("hidden");
    dom.resultPanel.classList.add("hidden");

    try {
      const img = new Image();
      img.src = URL.createObjectURL(file);
      await new Promise((res, rej) => { img.onload = res; img.onerror = rej; });

      const ctx = dom.canvas.getContext("2d");
      dom.canvas.width = img.width;
      dom.canvas.height = img.height;
      ctx.drawImage(img, 0, 0);
      const imageData = ctx.getImageData(0, 0, dom.canvas.width, dom.canvas.height);

      const qrResult = QRDecoder.decode(imageData);
      if (!qrResult) throw new Error("No QR code detected in the uploaded image.");

      const storageHrs = QRDecoder.computeStorageHours(qrResult.data.packaging_time);
      if (storageHrs === null || storageHrs === undefined) {
        throw new Error("QR code missing packaging_time field.");
      }

      const biofilmResult = BiofilmAnalyzer.analyze(imageData, qrResult.location);
      if (!biofilmResult) throw new Error("Could not detect biofilm color in the uploaded image.");

      await executeScanPayload(qrResult, biofilmResult, storageHrs);

    } catch (err) {
      console.error("Upload error:", err);
      showError(err.message);
    } finally {
      dom.scanBtn.disabled = false;
      dom.scanBtn.textContent = "📷 Scan Package";
    }
  }
};

/**
 * Executes a continuous live scan using the webcam feed.
 */
async function runScan() {
  const btn = dom.scanBtn;
  btn.disabled = true;
  btn.textContent = "⏳ Scanning...";
  dom.cameraPanel.classList.add("scan-active");

  dom.scanSummary.classList.add("hidden");
  dom.resultPanel.classList.add("hidden");

  try {
    if (!Camera.ready) throw new Error("Camera not available. Please upload a photo instead.");
    
    btn.textContent = "⏳ Scanning Package...";
    let imageData = null, qrResult = null;
    
    const startTime = Date.now();
    while (Date.now() - startTime < 3000) {
      imageData = Camera.captureFrame();
      qrResult = QRDecoder.decode(imageData);
      if (qrResult) break;
      await new Promise(resolve => setTimeout(resolve, 150));
    }

    if (!qrResult) throw new Error("No QR code detected — ensure it is in focus and well-lit.");

    const storageHrs = QRDecoder.computeStorageHours(qrResult.data.packaging_time);
    if (storageHrs === null || storageHrs === undefined) {
      throw new Error("QR code missing packaging_time field");
    }

    const biofilmResult = BiofilmAnalyzer.analyze(imageData, qrResult.location);
    if (!biofilmResult) {
      throw new Error("Could not detect biofilm color — ensure the indicator is visible");
    }

    await executeScanPayload(qrResult, biofilmResult, storageHrs);

  } catch (err) {
    console.error("Scan error:", err);
    showError(err.message);
  } finally {
    btn.disabled = false;
    btn.textContent = "📷 Scan Package";
    dom.cameraPanel.classList.remove("scan-active");
  }
}

/**
 * Packages the extracted data and sends it to the API backend.
 * @param {Object} qrResult 
 * @param {Object} biofilmResult 
 * @param {number} storageHrs 
 */
async function executeScanPayload(qrResult, biofilmResult, storageHrs) {
  const ammoniaSlider = document.getElementById("ammonia-slider");
  const ammoniaVal = ammoniaSlider ? parseFloat(ammoniaSlider.value) : 0.0;

  const payload = {
    ph_level: biofilmResult.ph,
    storage_time_hrs: storageHrs,
    ammonia_ppm: ammoniaVal
  };

  console.log("Payload to API:", payload);
  dom.scanBtn.textContent = "🧠 Fetching Live Data & Predicting...";

  const response = await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  });

  if (!response.ok) {
    const err = await response.json().catch(() => ({}));
    throw new Error(err.detail || `Server error (HTTP ${response.status}). Is Arduino live?`);
  }

  const result = await response.json();
  dom.mainView.classList.add("hidden");
  populateSummary(qrResult, biofilmResult, storageHrs, result.sensor_data_used);
  renderResult(result);
  
  dom.scanSummary.classList.remove("hidden");
  dom.resultPanel.classList.remove("hidden");
}

// ═══════════════════════════════════════════════════════════
// UI Helpers
// ═══════════════════════════════════════════════════════════
const STATUS_CONFIG = {
  SAFE:    { css: "status-badge--safe",    icon: "✅", border: "var(--safe-border)" },
  CAUTION: { css: "status-badge--caution", icon: "⚠️", border: "var(--caution-border)" },
  UNSAFE:  { css: "status-badge--unsafe",  icon: "🚫", border: "var(--unsafe-border)" },
};

function populateSummary(qr, biofilm, storageHrs, sensorData) {
  const d = qr.data;

  // Package Info
  dom.sumBatch.textContent     = d.batch_id   || "—";
  dom.sumProduct.textContent   = d.product_id || "—";
  dom.sumLocation.textContent  = d.location   || d.origin || "—";
  dom.sumNotes.textContent     = d.notes      || "—";
  if (d.packaging_time) {
    dom.sumPacktime.textContent = new Date(d.packaging_time).toLocaleString();
  } else {
    dom.sumPacktime.textContent = "—";
  }
  dom.sumInittemp.textContent = (d.initial_temp_c !== undefined) ? d.initial_temp_c + " °C" : "—";

  // Visual Analysis
  dom.sumStorage.textContent = storageHrs.toFixed(1) + " hrs";
  dom.sumStorageDetail.textContent = `≈ ${(storageHrs / 24).toFixed(1)} days`;

  const { r, g, b } = biofilm.rgb;
  dom.sumBiofilm.innerHTML =
    `<span class="biofilm-swatch" style="background:rgb(${r},${g},${b})"></span>` +
    `RGB(${r}, ${g}, ${b})`;
  dom.sumBiofilmDetail.textContent = `HSV(${biofilm.hsv.h}°, ${biofilm.hsv.s}%, ${biofilm.hsv.v}%)`;

  dom.sumPh.textContent = biofilm.ph.toFixed(2);
  dom.sumPhDetail.textContent = biofilm.ph <= 7.2 ? "Fresh range" : biofilm.ph <= 7.5 ? "Caution range" : "Spoiled range";

  // Cloud Sensor Data
  if (sensorData) {
    dom.sumAmmonia.textContent = sensorData.ammonia_ppm.toFixed(1) + " ppm";
    dom.sumTemp.textContent = sensorData.temp_c.toFixed(1) + " °C";
    dom.sumHumidity.textContent = sensorData.humidity ? sensorData.humidity.toFixed(0) + " %" : "—";
  }
}

function renderResult(result) {
  const statusKey = result.prediction.toUpperCase();
  const config = STATUS_CONFIG[statusKey] || STATUS_CONFIG.CAUTION;

  dom.statusBadge.className = "status-badge " + config.css;
  dom.statusIcon.textContent = config.icon;
  dom.statusLabel.textContent = result.prediction;
  
  dom.recAction.textContent = result.recommended_action || "—";

  const scores = result.confidence_scores;
  updateBar(dom.barSafe, dom.confSafe, scores.SAFE);
  updateBar(dom.barCaution, dom.confCaution, scores.CAUTION);
  updateBar(dom.barUnsafe, dom.confUnsafe, scores.UNSAFE);
}

function updateBar(barEl, textEl, score) {
  const pct = (score * 100).toFixed(0);
  barEl.style.width = pct + "%";
  textEl.textContent = pct + "%";
}

function showInfo(msg) {
  dom.infoToast.textContent = msg;
  dom.infoToast.classList.add("info-toast--visible");
  setTimeout(() => dom.infoToast.classList.remove("info-toast--visible"), 3000);
}

function showError(msg) {
  dom.errorToast.textContent = msg;
  dom.errorToast.classList.add("error-toast--visible");
  setTimeout(() => dom.errorToast.classList.remove("error-toast--visible"), 4000);
}

function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

// ═══════════════════════════════════════════════════════════
// Initialization
// ═══════════════════════════════════════════════════════════
window.addEventListener("DOMContentLoaded", () => {
  Camera.init();
  UIManager.init();

  dom.scanBtn.addEventListener("click", () => {
    if (!dom.scanBtn.disabled) runScan();
  });
});
