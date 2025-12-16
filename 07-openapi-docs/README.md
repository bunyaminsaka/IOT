# 📄 Task 7: OpenAPI Documentation

Swagger/OpenAPI specification for SmartHomeHubDoeb REST API.

## Files

| File | Description |
|------|-------------|
| `openapi.yaml` | OpenAPI 3.0 specification |

## View Documentation

1. Go to https://editor.swagger.io/
2. Paste `openapi.yaml` content
3. Interactive API documentation

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/state` | Get all device states |
| POST | `/api/lights/{room}` | Control light |
| POST | `/api/heating` | Control heating |
| POST | `/api/costs/reset` | Reset costs |

## Example Requests

### Turn on light
```bash
curl -X POST http://40.66.52.113/api/lights/living_room \
  -H "Content-Type: application/json" \
  -d '{"on": true}'
```

### Enable heating
```bash
curl -X POST http://40.66.52.113/api/heating \
  -H "Content-Type: application/json" \
  -d '{"enabled": true, "target_temp": 24}'
```

