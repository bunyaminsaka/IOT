"""
SmartHomeHubDoeb - Device Simulator
Simulates IoT devices sending data to MQTT broker

Requirements: pip install paho-mqtt
Usage: python device_simulator.py
"""

import paho.mqtt.client as mqtt
import json
import time
import random
from datetime import datetime

# =============================================================================
# CONFIGURATION - UPDATE WITH YOUR VM IP
# =============================================================================
MQTT_BROKER = "40.66.52.113"  # Your VM's public IP
MQTT_PORT = 1883
DEVICE_ID = "smarthome-sensor-01"

# =============================================================================
# MQTT CALLBACKS
# =============================================================================
def on_connect(client, userdata, flags, rc):
    codes = {0: "Connected", 1: "Bad protocol", 2: "Bad ID", 3: "Unavailable", 4: "Bad auth", 5: "Not authorized"}
    print(f"✅ {codes.get(rc, f'Code: {rc}')}")
    if rc == 0:
        client.subscribe("smarthome/#")
        print("📡 Subscribed to smarthome/#")

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        print(f"📨 {msg.topic}: {json.dumps(payload)}")
    except:
        print(f"📨 {msg.topic}: {msg.payload.decode()}")

# =============================================================================
# MAIN
# =============================================================================
def main():
    print("=" * 50)
    print("🏠 SmartHomeHubDoeb - Device Simulator")
    print("=" * 50)
    print(f"📍 Broker: {MQTT_BROKER}:{MQTT_PORT}")
    
    client = mqtt.Client(client_id=DEVICE_ID)
    client.on_connect = on_connect
    client.on_message = on_message
    
    try:
        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        client.loop_start()
        
        print("\n🎮 Running - Press Ctrl+C to stop\n")
        
        while True:
            # Temperature sensor
            temp = round(random.uniform(17, 25), 1)
            humidity = round(random.uniform(40, 70), 1)
            
            client.publish("smarthome/sensors/temperature", json.dumps({
                "device_id": DEVICE_ID,
                "temperature": temp,
                "humidity": humidity,
                "timestamp": datetime.now().isoformat()
            }))
            print(f"🌡️  Temp: {temp}°C | Humidity: {humidity}%")
            
            # Motion sensor (30% chance)
            if random.random() > 0.7:
                room = random.choice(["living_room", "bedroom", "kitchen"])
                client.publish(f"smarthome/sensors/motion/{room}", json.dumps({
                    "room": room,
                    "detected": True,
                    "timestamp": datetime.now().isoformat()
                }))
                print(f"🚶 Motion: {room}")
            
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\n👋 Stopped")
        client.disconnect()
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()

