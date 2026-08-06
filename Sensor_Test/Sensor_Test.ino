/*
 * SensoPack — Hardware Test Sketch
 * 
 * Use this sketch to test if your MQ-137 and AHT20 sensors
 * are wired correctly and reading valid data.
 * 
 * Unlike the main sketch, this one DOES NOT wait for the web app.
 * It simply prints the readings to the Serial Monitor every 2 seconds
 * so you can read them with your own eyes.
 * 
 * 1. Upload this sketch to your Arduino.
 * 2. Open the "Serial Monitor" in the Arduino IDE (magnifying glass icon top right).
 * 3. Set the baud rate in the bottom right corner of the Serial Monitor to 9600.
 */

#include <Wire.h>
#include <Adafruit_AHTX0.h>

#define MQ137_PIN A0

Adafruit_AHTX0 aht;
bool ahtConnected = false;

void setup() {
  Serial.begin(9600);
  while (!Serial) delay(10); // Wait for serial monitor to open

  Serial.println("=========================================");
  Serial.println("   SensoPack Hardware Diagnostic Test    ");
  Serial.println("=========================================");

  // Initialize AHT20
  Serial.print("Checking AHT20 (Temp/Humidity) sensor... ");
  if (aht.begin()) {
    Serial.println("FOUND!");
    ahtConnected = true;
  } else {
    Serial.println("FAILED!");
    Serial.println(" -> Check SDA (A4) and SCL (A5) wiring.");
  }

  // Check MQ-137
  Serial.print("Checking MQ-137 (Ammonia) sensor... ");
  int rawGas = analogRead(MQ137_PIN);
  if (rawGas > 0 && rawGas < 1023) {
    Serial.println("FOUND (Analog reading OK)!");
  } else {
    Serial.println("WARNING: Raw reading is 0 or 1023. Check A0 wiring.");
  }

  Serial.println("\nStarting continuous readings in 3 seconds...");
  delay(3000);
  Serial.println("TIME\t\tTEMP (°C)\tHUMIDITY (%)\tAMMONIA (Raw Analog)");
  Serial.println("------------------------------------------------------------------");
}

void loop() {
  unsigned long timeSec = millis() / 1000;
  Serial.print(timeSec);
  Serial.print("s\t\t");

  // Read AHT20
  if (ahtConnected) {
    sensors_event_t humidity_event, temp_event;
    aht.getEvent(&humidity_event, &temp_event);
    
    Serial.print(temp_event.temperature, 1);
    Serial.print("\t\t");
    Serial.print(humidity_event.relative_humidity, 1);
    Serial.print("\t\t");
  } else {
    Serial.print("ERROR\t\tERROR\t\t");
  }

  // Read MQ-137 (Raw value instead of PPM so it's easier to debug hardware)
  int rawGas = analogRead(MQ137_PIN);
  Serial.print(rawGas);
  
  if (rawGas < 100) {
    Serial.print(" (Very low - might be disconnected)");
  }

  Serial.println();
  
  delay(2000); // Wait 2 seconds before next reading
}
