"""
SmartHomeHubDoeb - Temperature Sensor Simulator
Simulates a temperature/humidity sensor

Requirements: pip install paho-mqtt
"""

import paho.mqtt.client as mqtt
import json
import time
import random
from datetime import datetime

MQTT_BROKER = "40.66.52.113"
MQTT_PORT = 1883
DEVICE_ID = "temp-sensor-01"
ROOM = "living_room"

def main():
    print(f"🌡️ Temperature Sensor - {ROOM}")
    
    client = mqtt.Client(client_id=DEVICE_ID)
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()
    
    base_temp = 20.0
    
    try:
        while True:
            # Simulate realistic temperature fluctuation
            temp = base_temp + random.uniform(-2, 2)
            humidity = 50 + random.uniform(-10, 10)
            
            payload = {
                "device_id": DEVICE_ID,
                "room": ROOM,
                "temperature": round(temp, 1),
                "humidity": round(humidity, 1),
                "unit": "celsius",
                "timestamp": datetime.now().isoformat()
            }
            
            client.publish(f"smarthome/sensors/temperature/{ROOM}", json.dumps(payload))
            print(f"📤 Temp: {payload['temperature']}°C | Humidity: {payload['humidity']}%")
            
            time.sleep(10)
            
    except KeyboardInterrupt:
        print("Stopped")
        client.disconnect()

if __name__ == "__main__":
    main()

