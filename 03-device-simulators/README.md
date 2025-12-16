# 🔌 Task 3: Device Simulators

Python scripts to simulate IoT devices connecting to the MQTT broker.

## Files

| File | Description |
|------|-------------|
| `device_simulator.py` | Multi-sensor simulator |
| `temperature_sensor.py` | Temperature/humidity sensor |
| `motion_sensor.py` | PIR motion sensor |
| `requirements.txt` | Python dependencies |

## Setup

```bash
pip install -r requirements.txt
```

## Usage

1. Update `MQTT_BROKER` in the script with your VM IP
2. Run:

```bash
python device_simulator.py
```

## MQTT Topics Published

| Topic | Data |
|-------|------|
| `smarthome/sensors/temperature` | `{temperature, humidity, timestamp}` |
| `smarthome/sensors/motion/<room>` | `{room, detected, timestamp}` |

