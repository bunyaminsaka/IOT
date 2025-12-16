# 📊 Task 1: C4 Architecture Diagrams

C4 model architecture diagrams for SmartHomeHubDoeb.

## Files

| File | Level | Description |
|------|-------|-------------|
| `c4-system-context.puml` | 1 | System and external actors |
| `c4-container.puml` | 2 | Containers (Dashboard, API, MQTT) |
| `c4-component.puml` | 3 | Flask API internal components |
| `c4-deployment.puml` | - | Azure deployment architecture |

## Generate PNG Images

1. Go to https://www.plantuml.com/plantuml/uml/
2. Paste `.puml` file content
3. Download PNG

## Architecture Overview

```
[Home Owner] → [Browser] → [Dashboard :80]
                              ↓
                         [Flask API :7071]
                              ↓
                         [MQTT Broker :1883]
                              ↓
                         [IoT Devices]
```

