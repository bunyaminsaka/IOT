# 🏗️ Task 8: Infrastructure as Code (Bicep)

Azure Bicep templates for deploying SmartHomeHubDoeb infrastructure.

## Files

| File | Description |
|------|-------------|
| `main.bicep` | Main infrastructure template |
| `deploy.ps1` | PowerShell deployment script |

## Resources Deployed

- Virtual Machine (Ubuntu 24.04, Standard_B1s)
- Virtual Network + Subnet
- Network Security Group (SSH, HTTP, MQTT)
- Public IP Address

## Deploy

```powershell
# Login to Azure
az login

# Deploy
./deploy.ps1 -ResourceGroup "IOTProject" -Location "francecentral"
```

## Manual Deploy

```bash
az group create --name IOTProject --location francecentral

az deployment group create \
  --resource-group IOTProject \
  --template-file main.bicep \
  --parameters adminPassword='YourPassword123!'
```

