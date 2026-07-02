---
pubDatetime: 2026-07-02T13:00:00Z
title: "Building an ESP32 Battery Monitor for the WINDTURER 3D-Printed Wind Turbine"
postSlug: "esp32-windturer-battery-monitor"
description: "A complete guide to building a standalone ESP32 + INA219 monitoring system for the WINDTURER 3D-printed portable wind turbine — real-time charge tracking, battery state of charge, and a web dashboard that runs from your phone with zero infrastructure."
tags:
  - ESP32
  - DIY
  - renewable energy
  - IoT
  - INA219
  - wind turbine
  - 3D printing
  - embedded
---

> **TL;DR**: An ESP32 DevKit, an INA219 current sensor, two resistors, and ~150 lines of C++ give you a real-time web dashboard showing turbine output voltage, charge current, power, and battery state of charge — all served from a WiFi hotspot with no internet required.

---

## The Problem: You Built a Turbine, Now What?

The [WINDTURER](https://hackaday.io/project/185070-3d-printed-portable-wind-turbine) is a brilliant open-source 3D-printed portable wind turbine. You print the blades, wire up a small BLDC motor as a generator, rectify the output to DC, and charge a battery. It's a complete renewable energy system you can carry in a backpack.

But once it's spinning, you're flying blind. How much power is it actually generating? Is the battery charging or just trickling? When do you need to stop and let it recover? Without instrumentation, you're guessing.

This project solves that with a ~$20 monitoring board that clips onto the turbine's existing wiring and serves a live dashboard to your phone.

---

## System Architecture

```
Wind → Blades → BLDC Generator → 3-Phase Rectifier
                                      ↓
                                 INA219 (0x40)  ← measures charge V/I/P
                                      ↓
                                 BMS Board
                                      ↓
                                NP-F Battery (2S 7.4V)
                                      ↓
                              Voltage Divider → ESP32 GPIO34
                                    ESP32
                                      ↓
                                 WiFi AP (192.168.4.1)
                                      ↓
                              Phone Dashboard (5s refresh)
```

The ESP32 reads the INA219 over I2C every 3 seconds, calculates battery state of charge from the ADC voltage divider, and serves both a JSON API (`/api/status`) and a web dashboard (`/`) over a self-hosted WiFi access point.

---

## Bill of Materials

| Component | Purpose | Cost |
|-----------|---------|------|
| ESP32 DevKit V1 | MCU + WiFi AP | $8-15 |
| INA219 breakout (Adafruit 904) | Charge current/voltage sensor | $4-10 |
| 100kΩ resistor (1/4W) | Voltage divider R1 | $0.10 |
| 47kΩ resistor (1/4W) | Voltage divider R2 | $0.10 |
| 3-phase rectifier (6A min) | AC→DC conversion | $3-5 |
| BMS 2S 8.4V 4A | Battery protection | $2-4 |
| NP-F battery (or 2x 18650) | Energy storage | $8-20 |
| Jumper wires, perfboard | Assembly | $3 |

**Total monitor cost: ~$20-35** beyond the WINDTURER turbine itself.

---

## Wiring

### ESP32 Connections

| ESP32 Pin | Connected To |
|-----------|-------------|
| GPIO21 (SDA) | INA219 SDA |
| GPIO22 (SCL) | INA219 SCL |
| 3.3V | INA219 VCC |
| GND | Common ground + divider GND |
| GPIO34 (ADC) | Voltage divider midpoint |

### INA219 Placement

The INA219 sits **between the rectifier output and the BMS input**. This means it measures current flowing *into* the battery — exactly what you want to know.

- **VIN+** → Rectifier positive output
- **VIN-** → BMS positive input (to battery +)
- **Address**: 0x40 (default, ADDR pin to GND)

### Voltage Divider

For a 2S Li-ion pack (7.4V nominal, 8.4V max), a 100kΩ/47kΩ divider maps the battery voltage down to a safe ADC range:

```
Battery+ ──┬─ 100kΩ ──┬── 47kΩ ── GND
           │          │
         BMS+     GPIO34 (ADC)
```

At 8.4V battery, the ADC pin sees 2.68V — comfortably within the ESP32's 3.3V limit.

---

## The Firmware

The firmware is written in Arduino C++ and built with PlatformIO. It does four things:

### 1. Sensor Reading

```cpp
void readSensors() {
  // INA219: turbine charge metrics
  float busV    = inaCharge.getBusVoltage_V();
  float current = abs(inaCharge.getCurrent_mA());
  float power   = abs(inaCharge.getPower_mW());

  // ADC: battery voltage via divider
  int adc = analogRead(VBAT_PIN);
  float vPin = (adc / 4095.0) * 3.3;
  float batV = vPin * ((R1 + R2) / R2);

  // State of charge: linear map 6.0V→0%, 8.4V→100%
  float batPct = constrain((batV - 6.0) / (8.4 - 6.0) * 100.0, 0.0, 100.0);
}
```

The INA219 gives us bus voltage, current, and power directly. Battery voltage comes from the ADC with the divider ratio applied. State of charge is a simple linear interpolation between the 2S Li-ion empty (6.0V) and full (8.4V) thresholds.

### 2. WiFi Access Point

The ESP32 creates its own WiFi network (`WINDTURER` / password: `windpower`). No existing network, no router, no internet — just connect your phone directly.

### 3. JSON API

```json
// GET /api/status
{
  "charge_v": 7.42,
  "charge_A": 0.183,
  "charge_W": 1.36,
  "battery_V": 7.81,
  "battery_pct": 76
}
```

### 4. Web Dashboard

The dashboard is a single HTML file served from SPIFFS (the ESP32's flash filesystem). It features:

- Real-time gauges for turbine voltage, current, and power
- Battery voltage and state of charge with progress bar
- Status badge: CHARGING / IDLE / DISCHARGING
- Dark theme optimised for outdoor visibility
- Auto-refresh every 5 seconds

---

## Dashboard Preview

The web UI is designed to be readable on a phone in bright sunlight:

- **Green cards** = turbine output (voltage, current, power)
- **Blue cards** = battery status (voltage, state of charge)
- **Status badge** = instantly see if you're generating, idle, or draining
- **Progress bar** = visual SoC at a glance

No app install required. Connect to the WiFi AP, open a browser, go to `192.168.4.1`.

---

## Optional: Cloud Dashboard via MQTT

The firmware includes optional MQTT support for [Adafruit IO](https://io.adafruit.com/). Fill in your credentials and the ESP32 will publish metrics to the cloud, letting you monitor the turbine from anywhere:

```cpp
const char* MQTT_SERVER = "io.adafruit.com";
const char* AIO_USERNAME = "your_username";
const char* AIO_KEY      = "your_key";
```

This is disabled by default — the standalone AP mode is the primary design. Cloud monitoring is a bonus for permanent installations.

---

## Calibration

Before field deployment, calibrate the voltage divider:

1. **Measure actual resistor values** with a multimeter (tolerances matter — a 5% 100kΩ could be 95kΩ or 105kΩ)
2. **Update `R1` and `R2`** constants in `main.cpp`
3. **Verify battery voltage** against a multimeter reading at the battery terminals
4. **Adjust SoC thresholds** if using a different battery chemistry (LiFePO4, for example, uses 6.0V→10.0V for 2S)

The formula: `Vbat = ADC_voltage * (R1 + R2) / R2`

---

## Deployment Checklist

- [ ] Print and assemble the WINDTURER turbine
- [ ] Wire the ESP32 + INA219 + voltage divider per the schematic
- [ ] Flash firmware via PlatformIO (`pio run --target upload`)
- [ ] Upload the web dashboard to SPIFFS (`pio run --target uploadfs`)
- [ ] Calibrate resistor values with a multimeter
- [ ] Connect phone to `WINDTURER` WiFi and verify dashboard loads
- [ ] Spin the turbine and watch the numbers move

---

## What This Enables

This monitor transforms the WINDTURER from a novelty into a **usable power tool**:

- **Know when to stop**: Watch the charge rate drop as the battery fills — stop before you overcharge
- **Optimise positioning**: Real-time power output tells you instantly if repositioning the turbine helped
- **Monitor health**: If power output drops over time, you know something needs attention (blades, bearings, connections)
- **Log sessions**: With MQTT enabled, build a historical record of generation across days and weather conditions
- **Plan capacity**: Know exactly how much energy you're harvesting to size your loads accordingly

---

## Technical Notes

- **INA219 calibration**: The firmware uses the `16V_400mA` range, which matches the WINDTURER's expected output. For higher-power turbines, switch to `32V_2A`
- **ADC accuracy**: The ESP32 ADC is notoriously non-linear at the extremes. For precision work, consider an ADS1115 external ADC instead of the built-in GPIO34
- **Power consumption**: The ESP32 draws ~50mA in AP mode. For long deployments, consider deep sleep with periodic wake, or power the ESP32 from the turbine's own output (via the 5V Vin pin with a regulator)
- **Second INA219**: The firmware supports a second INA219 at address 0x41 for monitoring battery *load* (what you're drawing), not just charge

---

## Source Code

The complete project — firmware, web dashboard, wiring guide, and PlatformIO config — is at `/root/windturer-monitor` and can be built with:

```bash
# Install dependencies
pio lib install

# Upload filesystem (web dashboard)
pio run --target uploadfs

# Upload firmware
pio run --target upload

# Monitor serial output
pio device monitor -b 115200
```

---

## Conclusion

For about $20 in parts and an afternoon's work, you can turn a 3D-printed wind turbine into an instrumented renewable energy system. The ESP32 + INA219 combination is one of the best value-to-capability ratios in DIY electronics — you get professional-grade monitoring with a phone-friendly dashboard and zero infrastructure requirements.

The WINDTURER is already a remarkable piece of open-source engineering. Adding real-time telemetry makes it genuinely useful for off-grid charging, camping, emergency preparedness, or just understanding how wind energy actually works in practice.

Spin it up, connect your phone, and watch the watts roll in.

---

*References: [WINDTURER Hackaday Project](https://hackaday.io/project/185070-3d-printed-portable-wind-turbine), [Adafruit INA219](https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout), [ESP32 Arduino Core](https://github.com/espressif/arduino-esp32), [PlatformIO](https://platformio.org/)*
