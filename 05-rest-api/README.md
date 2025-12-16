# 🌐 Task 5: REST API

Flask REST API with WebSocket support for real-time updates.

## Files

| File | Description |
|------|-------------|
| `app.py` | Main API application |
| `requirements.txt` | Python dependencies |
| `Dockerfile` | Container configuration |

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Dashboard |
| GET | `/api/state` | Get all device states |
| POST | `/api/lights/<room>` | Control light |
| POST | `/api/heating` | Control heating |
| POST | `/api/costs/reset` | Reset costs |

## WebSocket Events

| Event | Direction | Data |
|-------|-----------|------|
| `state_update` | Server→Client | Full state object |
| `cost_update` | Server→Client | Cost totals |
| `time_update` | Server→Client | Simulated time |

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

## Docker

```bash
docker build -t smarthome-api .
docker run -p 7071:7071 smarthome-api
```

