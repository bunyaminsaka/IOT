# 📡 Task 2: MQTT Broker Infrastructure

Eclipse Mosquitto MQTT broker configuration for IoT device communication.

## Files

| File | Description |
|------|-------------|
| `mosquitto.conf` | MQTT broker configuration |
| `docker-compose.yml` | Standalone MQTT deployment |

## Ports

| Port | Protocol | Purpose |
|------|----------|---------|
| 1883 | TCP | MQTT clients (IoT devices) |
| 9001 | WebSocket | Browser clients |

## Deploy Standalone

```bash
docker-compose up -d
```

## Test Connection

```bash
# Subscribe
mosquitto_sub -h localhost -t "smarthome/#" -v

# Publish
mosquitto_pub -h localhost -t "smarthome/test" -m "Hello"
```

## Topics Used

| Topic | Description |
|-------|-------------|
| `smarthome/lights/<room>` | Light control commands |
| `smarthome/heating` | Heating control |
| `smarthome/sensors/temperature` | Temperature readings |
| `smarthome/sensors/motion/<room>` | Motion detection |

