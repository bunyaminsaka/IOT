# 💾 Task 4: Data Storage (CosmosDB)

Azure Cosmos DB configuration for storing device telemetry and cost data.

## Files

| File | Description |
|------|-------------|
| `cosmosdb_config.py` | Configuration settings |
| `cosmosdb_storage.py` | CRUD operations |
| `requirements.txt` | Dependencies |

## Database Structure

```
SmartHomeDB/
├── DeviceTelemetry    (partition: /deviceId)
├── Devices            (partition: /deviceId)
├── Alerts             (partition: /deviceId)
└── EnergyCosts        (partition: /date)
```

## Setup

1. Create Azure Cosmos DB account
2. Set environment variables:

```bash
export COSMOS_ENDPOINT="https://your-account.documents.azure.com:443/"
export COSMOS_KEY="your-key-here"
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Note

Current implementation uses in-memory state for demo. CosmosDB integration is optional for production use.

