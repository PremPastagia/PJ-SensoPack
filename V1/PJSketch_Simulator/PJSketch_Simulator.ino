/*
 * SensoPack — Arduino SIMULATOR (No Sensors Needed)
 * 
 * Use this sketch to test the web app without real sensors.
 * It sends realistic simulated sensor data over Serial
 * in the exact same CSV format the web app expects.
 * 
 * Protocol: Same as PJSketch.ino — waits for 'R' command,
 * then replies with one CSV line of fake data.
 * 
 * Upload to any Arduino Uno and connect via the web app.
 * 
 * No wiring required — just USB cable.
 */

int cycle = 0;

void setup() {
  Serial.begin(9600);
  randomSeed(analogRead(A5));  // Seed from floating pin
  Serial.println("# SensoPack Simulator - Sending fake sensor data");
  Serial.println("# Format: ammonia_ppm,temperature_c,humidity_pct");
  Serial.println("# Waiting for scan command...");
}

void loop() {
  // Only send readings when requested by the web app (matching sensor hub protocol)
  if (Serial.available() > 0) {
    char cmd = Serial.read();
    if (cmd == 'R') {
      cycle++;
      sendSimulatedReadings();
    }
  }
}

void sendSimulatedReadings() {
  float ammonia, temperature, humidity;
  
  // Cycle through 3 scenarios every 15 scans
  int scenario = (cycle / 15) % 3;
  
  switch (scenario) {
    case 0:  // FRESH shrimp
      ammonia     = 1.5  + randomFloat(-0.5, 0.8);
      temperature = 2.0  + randomFloat(-0.5, 1.0);
      humidity    = 83.0 + randomFloat(-3.0, 3.0);
      break;
      
    case 1:  // BOUNDARY / Caution
      ammonia     = 9.0  + randomFloat(-1.5, 2.0);
      temperature = 8.0  + randomFloat(-1.0, 2.0);
      humidity    = 88.0 + randomFloat(-3.0, 3.0);
      break;
      
    case 2:  // SPOILED
      ammonia     = 26.0 + randomFloat(-3.0, 4.0);
      temperature = 20.0 + randomFloat(-2.0, 5.0);
      humidity    = 78.0 + randomFloat(-4.0, 4.0);
      break;
  }
  
  // Clamp to valid ranges
  ammonia     = constrain(ammonia, 0.1, 200.0);
  temperature = constrain(temperature, -20.0, 50.0);
  humidity    = constrain(humidity, 0.0, 100.0);
  
  // Send CSV: ammonia_ppm,temperature_c,humidity_pct
  Serial.print(ammonia, 1);
  Serial.print(",");
  Serial.print(temperature, 1);
  Serial.print(",");
  Serial.println(humidity, 0);
}

float randomFloat(float minVal, float maxVal) {
  return minVal + (maxVal - minVal) * (random(1000) / 1000.0);
}
