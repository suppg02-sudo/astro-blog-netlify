---
pubDatetime: 2026-03-08T14:02:00Z
title: "ESP32 Voice Recorder: No Buttons, No Touch"
postSlug: "youtube-esp32-voice-recorder"
description: "Build a gesture-controlled voice recorder using ESP32-S3 with shake-to-record functionality"
tags:
  - gesture-control
  - i2s
  - esp32
  - arduino
  - voice-recorder
  - diy-electronics
---

This video demonstrates building a gesture-controlled voice recorder using the ESP32-S3 microcontroller with no physical buttons or touch interface. The project uses the Megapes Touch ESP32-S3 development kit with a built-in digital I2S microphone (INMP441) and QMI8658 motion sensor. A simple shake gesture starts and stops recording, with audio saved as standard WAV files to an SD card.

## Hardware Platform

The Megapes Touch ESP32-S3 Development Kit provides an all-in-one solution with:
- **ESP32-S3** powerful microcontroller
- **INMP441 Digital I2S Microphone** - eliminates analog noise
- **QMI8658 Motion Sensor** - 6-axis IMU for gesture detection
- **3.16" TFT Display** - visual feedback
- **SD Card Slot** - audio storage
- **Battery Support** - built-in charging for portability

## How It Works

The system uses a simple shake gesture to control recording:
1. Power on → 2-second calibration (keep still)
2. Standby mode → wait for shake gesture
3. Shake detected → Start recording (red REC indicator)
4. Audio captured → Written to SD card in real-time
5. Shake detected again → Stop recording (green SAVED indicator)

## Audio Specifications

- **Sample Rate**: 22.05 kHz
- **Bit Depth**: 16-bit
- **Quality**: AM radio level (clear for speech)
- **Format**: Standard WAV files

## Key Insights

**Why Digital I2S Microphone?**
Digital audio transmission bypasses the ESP32's ADC, eliminating noise and instability.

**Why Gesture Control?**
Motion-based control is more intuitive than physical buttons - no wiring, debouncing, or mechanical wear.

**Why WAV Format?**
Universal compatibility - plays on any device without conversion.

## Future Development

Version 2 will add DSP processing, digital gain control, limiters, and noise handling for studio-quality voiceover recording.

---

[Watch the original video](https://www.youtube.com/watch?v=x4bm2PTf27w)