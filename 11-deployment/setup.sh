#!/bin/bash
# =============================================================================
# SmartHomeHubDoeb - VM Setup Script
# Run this inside your Azure VM
# =============================================================================

set -e

echo "============================================"
echo "🏠 SmartHomeHubDoeb - Setup"
echo "============================================"

# Install Docker
echo "📦 Installing Docker..."
sudo apt update
sudo apt install -y docker.io docker-compose
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER

# Create directories
echo "📁 Creating project structure..."
mkdir -p ~/smarthome/mosquitto/config ~/smarthome/mosquitto/data ~/smarthome/mosquitto/log
mkdir -p ~/smarthome/api
mkdir -p ~/smarthome/dashboard

echo "📋 Copy files from the repository:"
echo "   - 05-rest-api/* -> ~/smarthome/api/"
echo "   - 10-dashboard/* -> ~/smarthome/dashboard/"
echo "   - 02-mqtt-infrastructure/mosquitto.conf -> ~/smarthome/mosquitto/config/"
echo "   - 11-deployment/docker-compose.yml -> ~/smarthome/"
echo ""
echo "Then run: cd ~/smarthome && sudo docker-compose up -d --build"

