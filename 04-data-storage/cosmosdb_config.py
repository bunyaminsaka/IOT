"""
SmartHomeHubDoeb - CosmosDB Configuration
Azure Cosmos DB connection settings for telemetry storage
"""

import os

# =============================================================================
# COSMOS DB CONFIGURATION
# =============================================================================

COSMOS_CONFIG = {
    "endpoint": os.getenv("COSMOS_ENDPOINT", "https://smarthomehubdoeb.documents.azure.com:443/"),
    "key": os.getenv("COSMOS_KEY", "your-cosmos-key-here"),
    "database": "SmartHomeDB",
    "containers": {
        "telemetry": "DeviceTelemetry",
        "devices": "Devices",
        "alerts": "Alerts",
        "costs": "EnergyCosts"
    }
}

# Container partition keys
PARTITION_KEYS = {
    "telemetry": "/deviceId",
    "devices": "/deviceId",
    "alerts": "/deviceId",
    "costs": "/date"
}

