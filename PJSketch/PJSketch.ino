/*
 * SensoPack — Arduino Sensor Hub (PJSketch)
 * 
 * Reads sensor values ON DEMAND and sends them over Serial at 9600 baud
 * as a JSON line: {"temp": 25.0, "humidity": 60.0, "ammonia_ppm": 4.8}\n
 * 
 * Protocol:
 *   The web app sends 'R\n' when it needs a reading.
 *   Arduino reads sensors and replies with one CSV line.
 * 
 * Hardware wiring:
 *   - MQ-135 ammonia sensor  → Analog pin A0  (AOUT)
 *   - AHT20 temp/humidity    → I2C (SDA, SCL pins)
 *   - AHT20 VCC → 3.3V or 5V, GND → GND
 *   - MQ-135 VCC → 5V, GND → GND
 * 
 * Required libraries:
 *   Install "Adafruit AHTX0" by Adafruit from the Library Manager
 *   (Sketch → Include Library → Manage Libraries → search "Adafruit AHTX0")
 * 
 * Upload this sketch, then connect the web app via the
 * "Connect Arduino" button in the SensoPack dashboard.
 */

#include <Wire.h>
#include <Adafruit_AHTX0.h>

// ─── Pin Configuration ───
#define MQ135_PIN    A0     // MQ-135 analog output connected to A0
// Note: AHT20 uses hardware I2C pins (SDA, SCL). On Uno, these are A4(SDA) and A5(SCL)

// ─── Sensor Configuration ───
#define USE_AHT20    true   // Set to true if AHT20 is connected, false to use defaults

// ─── MQ-135 Calibration ───
// R0 is the sensor resistance in clean air divided by 3.6
// CALIBRATE R0 for your specific sensor (see instructions at bottom)
#define MQ135_RL         10.0    // Load resistor on the module (kΩ), typically 10kΩ
#define MQ135_R0         30.0    // Calculated R0 (kΩ) — CALIBRATE THIS
// Datasheet curve for NH3: log10(ppm) = slope * log10(Rs/R0) + intercept
#define MQ135_SLOPE      -3.32
#define MQ135_INTERCEPT  1.0

// ─── Timing ───
#define WARMUP_TIME_MS   30000   // 30 second warmup before first reading

Adafruit_AHTX0 aht;

bool warmedUp = false;
bool ahtConnected = false;

void setup() {
  Serial.begin(9600);
  
  if (USE_AHT20) {
    if (aht.begin()) {
      ahtConnected = true;
    } else {
      Serial.println("# ERROR: Could not find AHT20. Check wiring!");
    }
  }
  
  Serial.println("# SensoPack Arduino Sensor Hub starting...");
  Serial.println("# Warming up MQ-135 sensor on pin A0 (30 seconds)...");
  Serial.println("# Format: {\"temp\":..,\"humidity\":..,\"ammonia_ppm\":..}");
}

void loop() {
  unsigned long now = millis();
  
  // Wait for MQ-135 warmup period
  if (!warmedUp) {
    if (now > WARMUP_TIME_MS) {
      warmedUp = true;
      Serial.println("# Warmup complete. Waiting for scan command...");
    }
    return;
  }
  
  // Only send readings when requested by the web app
  // Web app sends 'R\n' when user clicks "Scan Package"
  if (Serial.available() > 0) {
    char cmd = Serial.read();
    if (cmd == 'R') {
      sendReadings();
    }
  }
}

void sendReadings() {
  // ── Read MQ-135 and convert to calibrated ammonia ppm ──
  // (previously this sent the raw uncalibrated analog average under a
  // "mq_raw" field, which silently bypassed this exact conversion curve
  // despite it being fully implemented below -- the ML model was retrained
  // against that arbitrary 0-1023 raw scale instead of real ppm, which is
  // why thresholds stopped lining up with the literature-grounded bounds.)
  float ammonia_ppm = readAmmoniaPpm();

  // ── Read AHT20 temperature and humidity ──
  float temperature = 4.0;   // Default safe chilling temp
  float humidity    = 85.0;  // Default humidity

  if (USE_AHT20 && ahtConnected) {
    sensors_event_t humidity_event, temp_event;
    aht.getEvent(&humidity_event, &temp_event);

    temperature = temp_event.temperature;
    humidity    = humidity_event.relative_humidity;
  } else if (USE_AHT20 && !ahtConnected) {
    // Serial.println("# ERROR: AHT20 not connected, using defaults");
  }

  // Clamp values to valid ranges expected by the ML model
  temperature = constrain(temperature, -20.0, 50.0);
  humidity    = constrain(humidity, 0.0, 100.0);

  // ── Send JSON line ──
  // Format: {"temp": 25.0, "humidity": 60.0, "ammonia_ppm": 4.8}
  Serial.print("{\"temp\": ");
  Serial.print(temperature, 1);
  Serial.print(", \"humidity\": ");
  Serial.print(humidity, 1);
  Serial.print(", \"ammonia_ppm\": ");
  Serial.print(ammonia_ppm, 2);
  Serial.println("}");
}

/*
 * Read the MQ-135 analog value and convert to ammonia ppm.
 *
 * The MQ-135 outputs a variable resistance based on gas concentration.
 * We convert the analog reading to a resistance ratio (Rs/R0),
 * then use the datasheet's log-log curve to estimate ppm.
 */
float readAmmoniaPpm() {
  // Average 10 readings for stability
  int rawTotal = 0;
  for (int i = 0; i < 10; i++) {
    rawTotal += analogRead(MQ135_PIN);
    delay(5);
  }
  float rawAvg = rawTotal / 10.0;

  // Prevent division by zero
  if (rawAvg < 1) rawAvg = 1;

  // Convert analog reading to sensor resistance (Rs)
  // Voltage divider: Vout = VCC * RL / (Rs + RL)
  // Rs = RL * (1023 - rawAvg) / rawAvg
  float rs = MQ135_RL * (1023.0 - rawAvg) / rawAvg;

  // Ratio of sensor resistance to clean-air resistance
  float ratio = rs / MQ135_R0;

  // Convert ratio to ppm using log-log relationship from datasheet
  // log10(ppm) = slope * log10(ratio) + intercept
  float logPpm = MQ135_SLOPE * log10(ratio) + MQ135_INTERCEPT;
  float ppm = pow(10.0, logPpm);

  return ppm;
}

/*
 * ═══════════════════════════════════════════════════════════
 * MQ-135 CALIBRATION INSTRUCTIONS
 * ═══════════════════════════════════════════════════════════
 * 
 * The MQ-135 needs calibration to give accurate ppm readings.
 * 
 * Step 1: PREHEAT
 *   Power the sensor continuously for 24-48 hours before
 *   calibrating. The heater needs this time to stabilize.
 * 
 * Step 2: FIND R0 (clean air resistance)
 *   - Place the sensor in clean outdoor air (no chemicals)
 *   - Run this code and note the analog reading
 *   - Calculate R0:
 *       Rs_clean = RL * (1023 - analogReading) / analogReading
 *       R0 = Rs_clean / 3.6
 *     (3.6 is the Rs/R0 ratio in clean air from the datasheet)
 *   - Update MQ135_R0 with your calculated value
 * 
 * Step 3: VERIFY
 *   - Compare readings against a known ammonia source
 *   - Adjust MQ135_SLOPE and MQ135_INTERCEPT if needed
 * 
 * The default values above are reasonable starting points
 * for demonstration purposes.
 * ═══════════════════════════════════════════════════════════
 */
