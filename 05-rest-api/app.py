"""
SmartHomeHubDoeb - REST API
Flask + Socket.IO backend for smart home control

Features:
- Light control (manual + time-based automation)
- Heating system control
- Cost tracking (10 PLN/10s electricity, 5 PLN/10s gas)
- Simulated 24h clock (40 seconds = 1 hour)
- Real-time WebSocket updates
"""

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import json, threading, time
from datetime import datetime

app = Flask(__name__, static_folder='../10-dashboard', static_url_path='')
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

# =============================================================================
# SIMULATED TIME SYSTEM (40 seconds = 1 hour)
# =============================================================================
SIM_SPEED = 40
sim_start_real = time.time()
sim_start_hour = 6

def get_sim_time():
    elapsed = time.time() - sim_start_real
    sim_hours = (elapsed / SIM_SPEED) + sim_start_hour
    h = int(sim_hours) % 24
    m = int((sim_hours % 1) * 60)
    return f"{h:02d}:{m:02d}"

# =============================================================================
# DEVICE STATE
# =============================================================================
state = {
    "lights": {
        "living_room": {"on": False, "auto_mode": False, "on_time": "18:00", "off_time": "23:00"},
        "bedroom": {"on": False, "auto_mode": False, "on_time": "20:00", "off_time": "07:00"},
        "kitchen": {"on": False, "auto_mode": False, "on_time": "06:00", "off_time": "09:00"}
    },
    "heating": {"enabled": False, "target_temp": 22, "current_temp": 18},
    "costs": {"electricity_rate": 10, "gas_rate": 5, "electricity_total": 0, "gas_total": 0},
    "sim_time": "06:00"
}

# =============================================================================
# BACKGROUND THREADS
# =============================================================================
def cost_calculator():
    while True:
        time.sleep(10)
        active = sum(1 for r, l in state["lights"].items() if l["on"])
        if active > 0:
            state["costs"]["electricity_total"] += state["costs"]["electricity_rate"] * active
        if state["heating"]["enabled"]:
            state["costs"]["gas_total"] += state["costs"]["gas_rate"]
        socketio.emit('cost_update', state["costs"])

def time_controller():
    while True:
        state["sim_time"] = get_sim_time()
        now = state["sim_time"]
        for room, light in state["lights"].items():
            if light["auto_mode"]:
                on_t, off_t = light["on_time"], light["off_time"]
                should_on = (on_t <= now < off_t) if on_t <= off_t else (now >= on_t or now < off_t)
                if should_on != light["on"]:
                    light["on"] = should_on
                    socketio.emit('state_update', state)
        socketio.emit('time_update', {"sim_time": now})
        time.sleep(0.667)

# =============================================================================
# API ROUTES
# =============================================================================
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/state')
def get_state():
    state["sim_time"] = get_sim_time()
    return jsonify(state)

@app.route('/api/lights/<room>', methods=['POST'])
def control_light(room):
    if room in state["lights"]:
        state["lights"][room].update(request.json)
        socketio.emit('state_update', state)
        return jsonify({"success": True, "room": room})
    return jsonify({"error": "Not found"}), 404

@app.route('/api/heating', methods=['POST'])
def control_heating():
    state["heating"].update(request.json)
    socketio.emit('state_update', state)
    return jsonify({"success": True})

@app.route('/api/costs/reset', methods=['POST'])
def reset_costs():
    state["costs"]["electricity_total"] = 0
    state["costs"]["gas_total"] = 0
    socketio.emit('cost_update', state["costs"])
    return jsonify({"success": True})

# =============================================================================
# WEBSOCKET
# =============================================================================
@socketio.on('connect')
def handle_connect():
    state["sim_time"] = get_sim_time()
    emit('state_update', state)
    emit('cost_update', state["costs"])
    emit('time_update', {"sim_time": state["sim_time"]})

# =============================================================================
# MAIN
# =============================================================================
if __name__ == '__main__':
    threading.Thread(target=cost_calculator, daemon=True).start()
    threading.Thread(target=time_controller, daemon=True).start()
    socketio.run(app, host='0.0.0.0', port=7071)

