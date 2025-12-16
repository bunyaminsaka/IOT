"""
SmartHomeHubDoeb - CosmosDB Storage Operations
CRUD operations for device telemetry and state storage
"""

from azure.cosmos import CosmosClient, PartitionKey
from datetime import datetime
import os

class SmartHomeStorage:
    """Azure Cosmos DB storage for SmartHomeHubDoeb"""
    
    def __init__(self):
        self.client = CosmosClient(
            os.getenv("COSMOS_ENDPOINT"),
            os.getenv("COSMOS_KEY")
        )
        self.database = self.client.get_database_client("SmartHomeDB")
        self.telemetry_container = self.database.get_container_client("DeviceTelemetry")
        self.costs_container = self.database.get_container_client("EnergyCosts")
    
    def save_telemetry(self, device_id: str, data: dict):
        """Save device telemetry data"""
        document = {
            "id": f"{device_id}_{datetime.utcnow().isoformat()}",
            "deviceId": device_id,
            "timestamp": datetime.utcnow().isoformat(),
            "data": data
        }
        return self.telemetry_container.create_item(document)
    
    def get_telemetry(self, device_id: str, limit: int = 100):
        """Get recent telemetry for a device"""
        query = f"SELECT * FROM c WHERE c.deviceId = '{device_id}' ORDER BY c.timestamp DESC"
        return list(self.telemetry_container.query_items(query, max_item_count=limit))
    
    def save_cost_record(self, date: str, electricity: float, gas: float):
        """Save daily cost record"""
        document = {
            "id": f"cost_{date}",
            "date": date,
            "electricity_pln": electricity,
            "gas_pln": gas,
            "total_pln": electricity + gas,
            "timestamp": datetime.utcnow().isoformat()
        }
        return self.costs_container.upsert_item(document)
    
    def get_cost_history(self, days: int = 30):
        """Get cost history for last N days"""
        query = "SELECT * FROM c ORDER BY c.date DESC"
        return list(self.costs_container.query_items(query, max_item_count=days))


# Example usage
if __name__ == "__main__":
    storage = SmartHomeStorage()
    
    # Save telemetry
    storage.save_telemetry("temp-sensor-01", {
        "temperature": 22.5,
        "humidity": 45.0
    })
    
    # Save cost record
    storage.save_cost_record("2025-12-12", 150.0, 75.0)

