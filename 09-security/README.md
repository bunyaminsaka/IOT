# 🔐 Task 9: Security (TLS/JWT)

Security configurations for SmartHomeHubDoeb.

## Files

| File | Description |
|------|-------------|
| `jwt_auth.py` | JWT authentication module |
| `tls_config.md` | TLS setup guide |

## Current Status

**Demo Mode:** Anonymous access enabled for demonstration.

## Production Recommendations

1. **Enable JWT Authentication**
   - Add `@token_required` decorator to API routes
   - Generate tokens on user login

2. **Enable TLS/HTTPS**
   - Use Let's Encrypt for free SSL
   - Configure Nginx reverse proxy

3. **MQTT Security**
   - Enable username/password authentication
   - Configure TLS on port 8883

4. **Secrets Management**
   - Use Azure Key Vault
   - Never commit secrets to Git

## Quick Enable JWT

```python
from jwt_auth import token_required

@app.route('/api/state')
@token_required
def get_state():
    return jsonify(state)
```

