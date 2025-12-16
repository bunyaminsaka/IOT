"""
SmartHomeHubDoeb - Motion Sensor Simulator
Simulates a PIR motion sensor

Requirements: pip install paho-mqtt
"""

import paho.mqtt.client as mqtt
import json
import time
import random
from datetime import datetime

MQTT_BROKER = "40.66.52.113"
MQTT_PORT = 1883
DEVICE_ID = "motion-sensor-01"
ROOM = "living_room"

def main():
    print(f"🚶 Motion Sensor - {ROOM}")
    
    client = mqtt.Client(client_id=DEVICE_ID)
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()
    
    try:
        while True:
            # Random motion detection (20% chance every 3 seconds)
            if random.random() > 0.8:
                payload = {
                    "device_id": DEVICE_ID,
                    "room": ROOM,
                    "motion_detected": True,
                    "timestamp": datetime.now().isoformat()
                }
                
                client.publish(f"smarthome/sensors/motion/{ROOM}", json.dumps(payload))
                print(f"📤 Motion detected in {ROOM}!")
            
            time.sleep(3)
            
    except KeyboardInterrupt:
        print("Stopped")
        client.disconnect()

if __name__ == "__main__":
    main()

