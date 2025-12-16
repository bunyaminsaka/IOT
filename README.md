<<<<<<< HEAD
# 🏠 SmartHomeHubDoeb

**IoT Smart Home System** - Complete smart home solution deployed on Azure VM

🌐 **Live Demo:** http://40.66.52.113

---

## 📋 Project Tasks

| # | Task | Folder | Status |
|---|------|--------|--------|
| 1 | C4 Architecture Diagrams | `/01-diagrams/` | ✅ |
| 2 | MQTT Broker Infrastructure | `/02-mqtt-infrastructure/` | ✅ |
| 3 | Device Simulators | `/03-device-simulators/` | ✅ |
| 4 | Data Storage (CosmosDB) | `/04-data-storage/` | ✅ |
| 5 | REST API | `/05-rest-api/` | ✅ |
| 6 | Cost Calculation | `/06-cost-calculation/` | ✅ |
| 7 | OpenAPI Documentation | `/07-openapi-docs/` | ✅ |
| 8 | Infrastructure as Code (Bicep) | `/08-infrastructure-bicep/` | ✅ |
| 9 | Security (TLS/JWT) | `/09-security/` | ✅ |
| 10 | Dashboard (Frontend) | `/10-dashboard/` | ✅ |
| 11 | Deployment Package | `/11-deployment/` | ✅ |

---

## 🚀 Quick Start

### Deploy to Azure VM

```bash
# 1. Create Azure VM (Ubuntu 24.04, Standard_B1s, France Central)
# 2. Open ports: 22, 80, 1883

# 3. SSH into VM
ssh IOTPRUSER@YOUR_VM_IP

# 4. Run deployment
cd ~
git clone https://github.com/YOUR_USERNAME/SmartHomeHubDoeb.git
cd SmartHomeHubDoeb/11-deployment
chmod +x setup.sh
./setup.sh
```

### Access Dashboard

Open: `http://YOUR_VM_IP`

---

## ✨ Features

- 💡 **Smart Lights** - 3 rooms with manual + auto control
- ⏰ **Time Automation** - Schedule-based ON/OFF
- 🔥 **Heating Control** - Temperature management
- 💰 **Cost Tracking** - 10 PLN/light, 5 PLN/gas per 10s
- ⏱️ **Demo Clock** - 40 seconds = 1 hour
- 🔄 **Real-time** - WebSocket updates

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────┐
│              Azure VM (Ubuntu 24.04)            │
│                 France Central                  │
│                                                 │
│  ┌───────────┐  ┌───────────┐  ┌────────────┐  │
│  │ Dashboard │  │ Flask API │  │   MQTT     │  │
│  │  HTML/JS  │◄─┤ + Socket  │◄─┤ Mosquitto  │  │
│  │   :80     │  │  :7071    │  │  :1883     │  │
│  └───────────┘  └───────────┘  └────────────┘  │
└─────────────────────────────────────────────────┘
```

---

## 👥 Team

SmartHomeHubDoeb - IoT Project

bünyamin yahya saka, deniz vardal, emir yumrukkaya, ömer boran

## 📄 License

Educational Project
