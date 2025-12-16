# 🔒 TLS Configuration Guide

## MQTT TLS Setup

### 1. Generate Certificates

```bash
# Create CA
openssl genrsa -out ca.key 2048
openssl req -new -x509 -days 365 -key ca.key -out ca.crt

# Create Server Certificate
openssl genrsa -out server.key 2048
openssl req -new -key server.key -out server.csr
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 365
```

### 2. Mosquitto TLS Config

```conf
listener 8883
cafile /mosquitto/certs/ca.crt
certfile /mosquitto/certs/server.crt
keyfile /mosquitto/certs/server.key
require_certificate false
```

## HTTPS Setup (Nginx)

```nginx
server {
    listen 443 ssl;
    ssl_certificate /etc/ssl/certs/server.crt;
    ssl_certificate_key /etc/ssl/private/server.key;
    
    location / {
        proxy_pass http://localhost:7071;
    }
}
```

## Let's Encrypt (Production)

```bash
sudo apt install certbot
sudo certbot certonly --standalone -d yourdomain.com
```

