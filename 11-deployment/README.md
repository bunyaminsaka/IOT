# 🚀 Task 11: Deployment

Complete deployment package for SmartHomeHubDoeb.

## Files

| File | Description |
|------|-------------|
| `docker-compose.yml` | Full stack container orchestration |
| `setup.sh` | VM setup script |

## Quick Deploy

### 1. Create Azure VM
- Ubuntu 24.04 LTS
- Standard_B1s
- Region: France Central
- Open ports: 22, 80, 1883

### 2. SSH into VM
```bash
ssh IOTPRUSER@YOUR_VM_IP
```

### 3. Run Setup
```bash
git clone https://github.com/YOUR_USERNAME/SmartHomeHubDoeb-GHub.git
cd SmartHomeHubDoeb-GHub/11-deployment
chmod +x setup.sh
./setup.sh
```

### 4. Deploy Stack
```bash
cd ~/smarthome
sudo docker-compose up -d --build
```

### 5. Access Dashboard
http://YOUR_VM_IP

## Management Commands

```bash
# Start
sudo docker-compose up -d

# Stop
sudo docker-compose down

# Logs
sudo docker-compose logs -f

# Rebuild
sudo docker-compose up -d --build
```

