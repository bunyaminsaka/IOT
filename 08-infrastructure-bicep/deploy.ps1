# =============================================================================
# SmartHomeHubDoeb - Bicep Deployment Script
# =============================================================================

param(
    [string]$ResourceGroup = "IOTProject",
    [string]$Location = "francecentral",
    [string]$AdminPassword = ""
)

if (-not $AdminPassword) {
    $AdminPassword = Read-Host -Prompt "Enter VM admin password" -AsSecureString | ConvertFrom-SecureString -AsPlainText
}

Write-Host "Creating resource group..." -ForegroundColor Yellow
az group create --name $ResourceGroup --location $Location

Write-Host "Deploying infrastructure..." -ForegroundColor Yellow
az deployment group create `
    --resource-group $ResourceGroup `
    --template-file main.bicep `
    --parameters adminPassword=$AdminPassword

Write-Host "Deployment complete!" -ForegroundColor Green

