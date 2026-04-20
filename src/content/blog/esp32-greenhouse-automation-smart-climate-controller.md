---
pubDatetime: 2026-03-21T21:30:00Z
title: "ESP32 Greenhouse Automation: Build a Smart Climate Controller"
postSlug: "esp32-greenhouse-automation-smart-climate-controller"
description: "ESP32 Greenhouse Automation: Build a Smart Climate Controller"
tags:
  - esp32
  - climate-control
  - automation
  - iot
  - diy
  - greenhouse
  - arduino
---

# ESP32 Greenhouse Automation: Build a Smart Climate Controller

*Turn a 2ft square greenhouse into a precision growing environment with £50 of electronics*

A 2ft (60cm) square greenhouse is the perfect size for ESP32 automation. Small enough to heat and cool efficiently, big enough to grow valuable crops like chillies, herbs, or early tomatoes. This guide shows you how to build a complete climate control system using ESP32 devices.

---

## 🎯 What You Can Actually Control

| Function | Hardware Needed | ESP32 Role |
|----------|-----------------|------------|
| **Temperature (heat)** | Tube heater + relay | Switch on when temp drops below threshold |
| **Temperature (cool)** | Extractor fan + relay | Switch on when temp exceeds threshold |
| **Humidity** | Extractor fan / misting | Reduce or increase humidity |
| **Ventilation** | Automatic vent opener / servo | Open/close based on conditions |
| **Lighting** | LED grow lights | Extend day length, boost growth |
| **Watering** | Solenoid valve + pump | Soil moisture-based irrigation |
| **Monitoring** | Various sensors | Log data, send alerts |

---

## 🛒 Shopping List: Complete System

### Core Components

| Item | Quantity | Cost | Notes |
|------|----------|------|-------|
| **ESP32 Dev Board** | 1-2 | £8-15 | Wemos D1 Mini or NodeMCU |
| **DHT22 Sensor** | 1 | £4 | Temperature + humidity |
| **DS18B20 Sensor** | 1-2 | £3 each | Waterproof temperature probes |
| **Soil Moisture Sensor** | 1-2 | £3 each | Capacitive type (resistive corrode) |
| **4-Channel Relay Module** | 1 | £5 | 5V logic, opto-isolated |
| **5V Power Supply** | 1 | £5 | 2A+ for ESP32 + peripherals |
| **Jumper Wires** | Pack | £3 | Male-female and male-male |
| **Small Project Box** | 1 | £3 | IP65 rated for greenhouse |
| **Cable Glands** | 4-6 | £3 | Waterproof cable entry |

**Total Core Cost: ~£35-45**

### Actuators (Choose What You Need)

| Item | Cost | Power | Application |
|------|------|-------|-------------|
| **Tube Heater (60W)** | £15-25 | 60W | Frost protection |
| **12V PC Fan** | £5-10 | 5-10W | Air circulation |
| **Extractor Fan (12V)** | £10-15 | 15-25W | Hot air removal |
| **Solenoid Valve (12V)** | £8-12 | 5W | Automated watering |
| **Submersible Pump (12V)** | £8-12 | 10-15W | Water delivery |
| **LED Grow Light (12V)** | £15-30 | 10-20W | Day length extension |
| **Servo (MG996R)** | £6 | 5W | Vent control |
| **12V Power Supply** | £10-15 | 5A | For all 12V devices |

**Total Actuator Cost (full system): ~£80-120**

---

## 🔌 Wiring Diagrams

### Basic Temperature Control

```
┌─────────────────────────────────────────────────────────────┐
│                        ESP32                                 │
│                                                              │
│  3.3V ─────┬───────────────────────────────────── DHT22 VCC │
│            │                                                  │
│  GND  ─────┼───────────────────────────────────── DHT22 GND │
│            │                                                  │
│  GPIO 4 ───┴───────────────────────────────────── DHT22 DATA │
│                                                              │
│  GPIO 25 ────────────────────────────── Relay IN1            │
│            (to heater)                                        │
│  GPIO 26 ────────────────────────────── Relay IN2            │
│            (to fan)                                           │
│                                                              │
│  5V   ──────────────────────────────── Relay VCC             │
│  GND  ──────────────────────────────── Relay GND             │
│                                                              │
│  COM1  ──────── Mains Live IN (heater circuit)               │
│  NO1   ──────── Mains Live OUT (to heater)                   │
│  COM2  ──────── 12V + IN (fan circuit)                       │
│  NO2   ──────── 12V + OUT (to fan +)                         │
└─────────────────────────────────────────────────────────────┘
```

### With Soil Moisture and Watering

```
┌─────────────────────────────────────────────────────────────┐
│                        ESP32                                 │
│                                                              │
│  GPIO 34 (ADC) ───────────────────── Capacitive Soil Sensor │
│  GPIO 27 ───────────────────────────── Relay IN3 (pump)     │
│                                                              │
│  3.3V ───────────────────────────────── Soil Sensor VCC     │
│  GND  ───────────────────────────────── Soil Sensor GND     │
└─────────────────────────────────────────────────────────────┘
```

### Power Distribution

```
Mains (230V) ──┬── 5V Power Supply ───── ESP32 + Relays
               │
               └── 12V Power Supply ───── Fans + Pump + Lights

For heater: Use mains via relay (ensure proper safety)
For fans/pump/lights: Use 12V via relay (safer, easier)
```

---

## 💻 Code: Basic Climate Controller

### Arduino IDE Sketch

```cpp
#include <WiFi.h>
#include <DHT.h>
#include <WebServer.h>

// Pin Definitions
#define DHT_PIN 4
#define HEATER_RELAY 25
#define FAN_RELAY 26
#define PUMP_RELAY 27
#define SOIL_SENSOR 34

// Sensor
#define DHT_TYPE DHT22
DHT dht(DHT_PIN, DHT_TYPE);

// WiFi Credentials
const char* ssid = "YOUR_WIFI_SSID";
const char* password = "YOUR_WIFI_PASSWORD";

// Web Server
WebServer server(80);

// Thresholds
float TEMP_LOW = 10.0;      // Turn heater ON below this
float TEMP_HIGH = 28.0;     // Turn fan ON above this
int SOIL_DRY = 3000;         // Water when soil reading above this
int SOIL_WET = 1500;         // Stop watering below this

// Timing
unsigned long lastReading = 0;
const long READING_INTERVAL = 60000; // Read every minute

// Current values
float temperature = 0;
float humidity = 0;
int soilMoisture = 0;

void setup() {
  Serial.begin(115200);
  
  // Initialize pins
  pinMode(HEATER_RELAY, OUTPUT);
  pinMode(FAN_RELAY, OUTPUT);
  pinMode(PUMP_RELAY, OUTPUT);
  
  // Relays are active LOW (common)
  digitalWrite(HEATER_RELAY, HIGH);
  digitalWrite(FAN_RELAY, HIGH);
  digitalWrite(PUMP_RELAY, HIGH);
  
  // Initialize DHT
  dht.begin();
  
  // Connect WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected: ");
  Serial.println(WiFi.localIP());
  
  // Web server endpoints
  server.on("/", handleRoot);
  server.on("/status", handleStatus);
  server.on("/config", handleConfig);
  server.begin();
}

void loop() {
  server.handleClient();
  
  unsigned long currentMillis = millis();
  if (currentMillis - lastReading >= READING_INTERVAL) {
    lastReading = currentMillis;
    readSensors();
    controlClimate();
  }
}

void readSensors() {
  temperature = dht.readTemperature();
  humidity = dht.readHumidity();
  soilMoisture = analogRead(SOIL_SENSOR);
  
  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("DHT read error");
    return;
  }
  
  Serial.print("Temp: ");
  Serial.print(temperature);
  Serial.print("°C  Humidity: ");
  Serial.print(humidity);
  Serial.print("%  Soil: ");
  Serial.println(soilMoisture);
}

void controlClimate() {
  // Temperature control
  if (temperature < TEMP_LOW) {
    digitalWrite(HEATER_RELAY, LOW);  // ON
    Serial.println("Heater ON");
  } else if (temperature > TEMP_LOW + 2) {
    digitalWrite(HEATER_RELAY, HIGH); // OFF
    Serial.println("Heater OFF");
  }
  
  if (temperature > TEMP_HIGH) {
    digitalWrite(FAN_RELAY, LOW);     // ON
    Serial.println("Fan ON");
  } else if (temperature < TEMP_HIGH - 2) {
    digitalWrite(FAN_RELAY, HIGH);    // OFF
    Serial.println("Fan OFF");
  }
  
  // Soil moisture control (water for 5 seconds when dry)
  static unsigned long pumpStart = 0;
  static bool pumpRunning = false;
  
  if (soilMoisture > SOIL_DRY && !pumpRunning) {
    digitalWrite(PUMP_RELAY, LOW);    // ON
    pumpStart = millis();
    pumpRunning = true;
    Serial.println("Pump ON");
  }
  
  if (pumpRunning && (millis() - pumpStart > 5000 || soilMoisture < SOIL_WET)) {
    digitalWrite(PUMP_RELAY, HIGH);   // OFF
    pumpRunning = false;
    Serial.println("Pump OFF");
  }
}

void handleRoot() {
  String html = "<!DOCTYPE html><html><head>";
  html += "<meta name='viewport' content='width=device-width,initial-scale=1'>";
  html += "<meta http-equiv='refresh' content='30'>";
  html += "<title>Greenhouse Monitor</title>";
  html += "<style>body{font-family:Arial,sans-serif;margin:20px;}";
  html += ".card{background:#f4f4f4;padding:15px;margin:10px 0;border-radius:8px;}";
  html += ".value{font-size:2em;font-weight:bold;color:#2e7d32;}";
  html += "</style></head><body>";
  html += "<h1>🌱 Greenhouse Monitor</h1>";
  html += "<div class='card'><strong>Temperature:</strong> ";
  html += "<span class='value'>" + String(temperature, 1) + "°C</span></div>";
  html += "<div class='card'><strong>Humidity:</strong> ";
  html += "<span class='value'>" + String(humidity, 0) + "%</span></div>";
  html += "<div class='card'><strong>Soil Moisture:</strong> ";
  html += "<span class='value'>" + String(soilMoisture) + "</span>";
  html += (soilMoisture > SOIL_DRY ? " (Dry)" : " (Wet)") + "</div>";
  html += "<p><a href='/config'>⚙️ Configuration</a></p>";
  html += "<p><small>Last updated: " + String(millis()/1000) + "s ago</small></p>";
  html += "</body></html>";
  server.send(200, "text/html", html);
}

void handleStatus() {
  String json = "{";
  json += "\"temperature\":" + String(temperature) + ",";
  json += "\"humidity\":" + String(humidity) + ",";
  json += "\"soilMoisture\":" + String(soilMoisture) + ",";
  json += "\"heaterOn\":" + String(!digitalRead(HEATER_RELAY)) + ",";
  json += "\"fanOn\":" + String(!digitalRead(FAN_RELAY)) + ",";
  json += "\"pumpOn\":" + String(!digitalRead(PUMP_RELAY));
  json += "}";
  server.send(200, "application/json", json);
}

void handleConfig() {
  if (server.hasArg("tempLow")) {
    TEMP_LOW = server.arg("tempLow").toFloat();
  }
  if (server.hasArg("tempHigh")) {
    TEMP_HIGH = server.arg("tempHigh").toFloat();
  }
  if (server.hasArg("soilDry")) {
    SOIL_DRY = server.arg("soilDry").toInt();
  }
  
  String html = "<!DOCTYPE html><html><head>";
  html += "<title>Greenhouse Config</title>";
  html += "<style>body{font-family:Arial;margin:20px;}";
  html += "input[type='number']{width:100px;padding:5px;}";
  html += "</style></head><body>";
  html += "<h1>⚙️ Configuration</h1>";
  html += "<form method='GET'>";
  html += "<p>Heater ON below: <input type='number' step='0.5' name='tempLow' value='" + String(TEMP_LOW) + "'> °C</p>";
  html += "<p>Fan ON above: <input type='number' step='0.5' name='tempHigh' value='" + String(TEMP_HIGH) + "'> °C</p>";
  html += "<p>Water when soil >: <input type='number' name='soilDry' value='" + String(SOIL_DRY) + "'></p>";
  html += "<p><input type='submit' value='Save'></p>";
  html += "</form>";
  html += "<p><a href='/'>← Back to Monitor</a></p>";
  html += "</body></html>";
  server.send(200, "text/html", html);
}
```

---

## 📡 Advanced: MQTT + Home Assistant Integration

For remote monitoring and integration with smart home systems:

### MQTT Publishing

Add to the code above:

```cpp
#include <PubSubClient.h>

WiFiClient espClient;
PubSubClient mqtt(espClient);

const char* mqtt_server = "YOUR_MQTT_BROKER_IP";
const char* mqtt_user = "YOUR_MQTT_USER";
const char* mqtt_pass = "YOUR_MQTT_PASSWORD";

void setupMQTT() {
  mqtt.setServer(mqtt_server, 1883);
  mqtt.setCallback(mqttCallback);
}

void reconnectMQTT() {
  while (!mqtt.connected()) {
    if (mqtt.connect("Greenhouse", mqtt_user, mqtt_pass)) {
      mqtt.subscribe("greenhouse/heater/set");
      mqtt.subscribe("greenhouse/fan/set");
      mqtt.subscribe("greenhouse/thresholds/set");
    } else {
      delay(5000);
    }
  }
}

void publishStatus() {
  StaticJsonDocument<256> doc;
  doc["temperature"] = temperature;
  doc["humidity"] = humidity;
  doc["soil_moisture"] = soilMoisture;
  doc["heater"] = !digitalRead(HEATER_RELAY);
  doc["fan"] = !digitalRead(FAN_RELAY);
  
  char buffer[256];
  serializeJson(doc, buffer);
  mqtt.publish("greenhouse/status", buffer);
}

void mqttCallback(char* topic, byte* payload, unsigned int length) {
  String message;
  for (int i = 0; i < length; i++) {
    message += (char)payload[i];
  }
  
  if (String(topic) == "greenhouse/heater/set") {
    if (message == "ON") digitalWrite(HEATER_RELAY, LOW);
    else digitalWrite(HEATER_RELAY, HIGH);
  }
  // Handle other commands...
}
```

### Home Assistant Configuration

Add to `configuration.yaml`:

```yaml
mqtt:
  sensor:
    - name: "Greenhouse Temperature"
      state_topic: "greenhouse/status"
      unit_of_measurement: "°C"
      value_template: "{{ value_json.temperature }}"
      
    - name: "Greenhouse Humidity"
      state_topic: "greenhouse/status"
      unit_of_measurement: "%"
      value_template: "{{ value_json.humidity }}"
      
    - name: "Greenhouse Soil Moisture"
      state_topic: "greenhouse/status"
      value_template: "{{ value_json.soil_moisture }}"
      
  switch:
    - name: "Greenhouse Heater"
      command_topic: "greenhouse/heater/set"
      state_topic: "greenhouse/status"
      value_template: "{{ value_json.heater }}"
      payload_on: "ON"
      payload_off: "OFF"
      
    - name: "Greenhouse Fan"
      command_topic: "greenhouse/fan/set"
      state_topic: "greenhouse/status"
      value_template: "{{ value_json.fan }}"
      payload_on: "ON"
      payload_off: "OFF"

  automation:
    - alias: "Greenhouse Frost Protection"
      trigger:
        - platform: numeric_state
          entity_id: sensor.greenhouse_temperature
          below: 5
      action:
        - service: switch.turn_on
          target:
            entity_id: switch.greenhouse_heater
            
    - alias: "Greenhouse Overheat Protection"
      trigger:
        - platform: numeric_state
          entity_id: sensor.greenhouse_temperature
          above: 35
      action:
        - service: switch.turn_on
          target:
            entity_id: switch.greenhouse_fan
            
    - alias: "Greenhouse Alert - High Temp"
      trigger:
        - platform: numeric_state
          entity_id: sensor.greenhouse_temperature
          above: 30
      action:
        - service: notify.mobile_app
          data:
            message: "⚠️ Greenhouse temperature is {{ states('sensor.greenhouse_temperature') }}°C"
```

---

## 🌡️ Smart Automation Logic

### Temperature Management Strategy

| Time | Target Temp | Heater | Fan | Notes |
|------|-------------|--------|-----|-------|
| **Night (10pm-6am)** | 12-15°C | Active | Off | Frost protection |
| **Morning (6am-10am)** | 18-20°C | Active | Off | Warm up for day |
| **Midday (10am-4pm)** | 22-28°C | Off | Active if >28°C | Allow natural warmth |
| **Evening (4pm-10pm)** | 18-20°C | Off then active | Off | Retain heat |

### Code: Time-Based Thresholds

```cpp
void adjustThresholds() {
  int hour = (timeClient.getHours() + timezoneOffset) % 24;
  
  if (hour >= 22 || hour < 6) {
    // Night mode
    TEMP_LOW = 10.0;
    TEMP_HIGH = 35.0; // Fan unlikely needed
  } else if (hour >= 6 && hour < 10) {
    // Morning warm-up
    TEMP_LOW = 15.0;
    TEMP_HIGH = 32.0;
  } else if (hour >= 10 && hour < 16) {
    // Midday
    TEMP_LOW = 8.0;  // Heater unlikely needed
    TEMP_HIGH = 28.0;
  } else {
    // Evening
    TEMP_LOW = 12.0;
    TEMP_HIGH = 30.0;
  }
}
```

### Humidity Control

```cpp
#define HUMIDITY_HIGH 85  // Turn on fan if humidity exceeds this
#define HUMIDITY_LOW 60   // Target humidity

void controlHumidity() {
  if (humidity > HUMIDITY_HIGH) {
    digitalWrite(FAN_RELAY, LOW);  // Fan ON
  } else if (humidity < HUMIDITY_LOW) {
    digitalWrite(FAN_RELAY, HIGH); // Fan OFF
  }
}
```

### Smart Watering

```cpp
void smartWatering() {
  static bool morningWatered = false;
  static bool eveningWatered = false;
  
  int hour = getCurrentHour();
  
  // Water in morning (6-8am) if dry
  if (hour >= 6 && hour < 8 && !morningWatered) {
    if (soilMoisture > SOIL_DRY) {
      waterFor(5000); // 5 seconds
    }
    morningWatered = true;
  }
  
  // Reset flags
  if (hour >= 8) morningWatered = false;
  if (hour >= 20) eveningWatered = false;
  
  // Emergency watering (always check)
  if (soilMoisture > SOIL_DRY + 500) {
    waterFor(3000);
  }
}

void waterFor(int ms) {
  digitalWrite(PUMP_RELAY, LOW);
  delay(ms);
  digitalWrite(PUMP_RELAY, HIGH);
  Serial.printf("Watered for %d ms\n", ms);
}
```

---

## 🔋 Power Considerations for 2ft Greenhouse

### Power Budget

| Device | Power (W) | Daily Runtime | Daily Wh |
|--------|-----------|---------------|----------|
| **ESP32 + Sensors** | 2 | 24h | 48 |
| **Tube Heater (60W)** | 60 | 8h (cold nights) | 480 |
| **Extractor Fan** | 15 | 4h (hot days) | 60 |
| **Circulation Fan** | 5 | 12h | 60 |
| **Water Pump** | 10 | 5 min | 1 |
| **LED Grow Light** | 15 | 6h (spring) | 90 |

**Peak demand:** ~100W (heater + fans running together)
**Typical daily use:** 300-700Wh depending on weather

### Power Options

**Mains Powered (Recommended):**
- Run extension to greenhouse
- Use outdoor-rated cable and RCD protection
- Most reliable for heating

**Solar Powered (Advanced):**
- 50W solar panel + 20Ah 12V battery
- Sufficient for fans, pump, ESP32
- **Not sufficient for heater** (need mains for heating)

---

## 📱 Remote Monitoring Options

### Option 1: Web Interface (Built-in)

Access `http://[ESP32_IP]` from any device on your network. Simple, no additional infrastructure.

### Option 2: Blynk App

```cpp
#include <BlynkSimpleEsp32.h>

#define BLYNK_TEMPLATE_ID "YOUR_TEMPLATE"
#define BLYNK_DEVICE_NAME "Greenhouse"
#define BLYNK_AUTH_TOKEN "YOUR_TOKEN"

BlynkTimer timer;

void sendSensor() {
  Blynk.virtualWrite(V0, temperature);
  Blynk.virtualWrite(V1, humidity);
  Blynk.virtualWrite(V2, soilMoisture);
}

void setup() {
  Blynk.begin(BLYNK_AUTH_TOKEN, ssid, password);
  timer.setInterval(60000L, sendSensor);
}

void loop() {
  Blynk.run();
  timer.run();
}
```

### Option 3: Telegram Alerts

```cpp
#include <UniversalTelegramBot.h>

const char* botToken = "YOUR_BOT_TOKEN";
const char* chatId = "YOUR_CHAT_ID";

void sendAlert(String message) {
  bot.sendMessage(chatId, message, "");
}

// In control code:
if (temperature < 5.0) {
  sendAlert("⚠️ Frost warning! Greenhouse at " + String(temperature) + "°C");
}
```

---

## 🛠️ Physical Build

### Enclosure

```
┌────────────────────────────────────────┐
│ IP65 Project Box                        │
│                                         │
│  ┌─────────┐                           │
│  │  ESP32  │                           │
│  │         │    ┌──────────────┐       │
│  │         │    │ 4-Channel    │       │
│  └─────────┘    │ Relay Module │       │
│                 └──────────────┘       │
│                                         │
│  [DHT22]  [Soil]  [Temp Probe]         │
│    │        │         │                │
└────┼────────┼─────────┼────────────────┘
     │        │         │
   Cable glands for waterproof entry
```

### Sensor Placement

| Sensor | Position | Why |
|--------|----------|-----|
| **DHT22** | Mid-height, shaded | Accurate air temp/humidity |
| **DS18B20** | Near plants | Soil/leaf temperature |
| **Soil Moisture** | Root zone | Actual growing conditions |

**Tip**: Put DHT22 in a small ventilated enclosure to protect from direct sun and water.

### Heater Placement

For a 2ft square greenhouse:
- **Tube heater**: Low down on one side
- **Warm air rises** naturally
- **Circulation fan**: Opposite corner, blowing across

---

## 📊 Data Logging

### SD Card Logging

```cpp
#include <SD.h>
#include <SPI.h>

#define SD_CS 5

void logToSD() {
  File file = SD.open("/greenhouse.csv", FILE_APPEND);
  if (file) {
    file.printf("%s,%.1f,%.0f,%d,%d,%d\n",
      timeClient.getFormattedTime().c_str(),
      temperature,
      humidity,
      soilMoisture,
      !digitalRead(HEATER_RELAY),
      !digitalRead(FAN_RELAY)
    );
    file.close();
  }
}
```

### CSV Format

```csv
timestamp,temperature,humidity,soil_moisture,heater_on,fan_on
2026-03-21T08:00:00,12.5,78,2100,1,0
2026-03-21T08:01:00,12.3,79,2095,1,0
```

---

## 🎯 Project Phases

### Phase 1: Basic Monitoring (Weekend Project)
- [ ] Flash ESP32 with basic code
- [ ] Connect DHT22 sensor
- [ ] Test web interface
- [ ] Verify readings are accurate

### Phase 2: Temperature Control (1 Day)
- [ ] Add relay module
- [ ] Connect tube heater (via electrician if not confident)
- [ ] Connect extractor fan
- [ ] Test heating and cooling logic
- [ ] Adjust thresholds

### Phase 3: Irrigation (1 Day)
- [ ] Add soil moisture sensor
- [ ] Connect solenoid valve or pump
- [ ] Test watering logic
- [ ] Calibrate soil moisture readings

### Phase 4: Advanced Features (Ongoing)
- [ ] Add MQTT integration
- [ ] Connect to Home Assistant
- [ ] Set up Telegram alerts
- [ ] Add data logging
- [ ] Fine-tune automation rules

---

## 💡 Practical Tips

### Calibration

**Soil Moisture Sensor:**
1. Insert into dry soil → note reading (e.g., 3500)
2. Water thoroughly → note reading (e.g., 1200)
3. Set SOIL_DRY = dry_reading - 500
4. Set SOIL_WET = wet_reading + 200

**Temperature:**
1. Compare with accurate thermometer
2. Add offset in code if needed:
   ```cpp
   temperature = dht.readTemperature() + TEMP_OFFSET;
   ```

### Safety

- **Mains voltage**: Use proper enclosures, RCD protection
- **Water + electricity**: Keep 12V and mains separate
- **Fire risk**: Use tube heaters (designed for greenhouses), not fan heaters
- **Backup**: Manual override switch for heating

### Reliability

- **Watchdog timer**: Reset ESP32 if it hangs
  ```cpp
  #include <esp_task_wdt.h>
  void setup() {
    esp_task_wdt_init(30, true);
  }
  ```
- **WiFi reconnect**: Handle disconnections gracefully
- **Sensor validation**: Check for NaN/impossible values

---

## 📈 Expected Results

### Without Automation
- Temperature range: 5°C to 40°C+
- Daily fluctuations: 20-30°C
- Frost damage: Likely in cold snaps
- Overheating: Probable on sunny days

### With ESP32 Automation
- Temperature range: 12°C to 28°C (adjustable)
- Daily fluctuations: 8-12°C
- Frost damage: Prevented
- Overheating: Managed automatically
- Watering: Optimized to need

---

## 🔧 Troubleshooting

| Problem | Likely Cause | Solution |
|---------|--------------|----------|
| **ESP32 keeps resetting** | Power supply too weak | Use 2A+ supply |
| **Temperature readings wrong** | Sensor in direct sun | Move to shade |
| **WiFi keeps dropping** | Weak signal | Add WiFi extender |
| **Relays not switching** | Logic inverted | Check active HIGH/LOW |
| **Soil sensor corroded** | Resistive type | Use capacitive sensor |
| **Heater not warming enough** | Undersized | Check wattage vs space |

---

*A 2ft greenhouse with ESP32 control is a perfect testbed for automation concepts that scale to larger setups. Start simple, add features gradually, and learn what your plants actually need.*