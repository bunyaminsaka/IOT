"""
SmartHomeHubDoeb - JWT Authentication Module
Token-based authentication for API security

Note: Current demo uses anonymous access. 
Enable JWT auth for production deployment.
"""

import jwt
import datetime
from functools import wraps
from flask import request, jsonify

# =============================================================================
# CONFIGURATION
# =============================================================================
SECRET_KEY = "your-secret-key-change-in-production"
ALGORITHM = "HS256"
TOKEN_EXPIRY_HOURS = 24

# =============================================================================
# TOKEN FUNCTIONS
# =============================================================================
def generate_token(user_id: str, role: str = "user") -> str:
    """Generate JWT token for user"""
    payload = {
        "user_id": user_id,
        "role": role,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=TOKEN_EXPIRY_HOURS),
        "iat": datetime.datetime.utcnow()
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(token: str) -> dict:
    """Verify and decode JWT token"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {"valid": True, "payload": payload}
    except jwt.ExpiredSignatureError:
        return {"valid": False, "error": "Token expired"}
    except jwt.InvalidTokenError:
        return {"valid": False, "error": "Invalid token"}


def token_required(f):
    """Decorator to protect routes with JWT"""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        
        if not token:
            return jsonify({"error": "Token missing"}), 401
        
        # Remove "Bearer " prefix
        if token.startswith("Bearer "):
            token = token[7:]
        
        result = verify_token(token)
        if not result["valid"]:
            return jsonify({"error": result["error"]}), 401
        
        return f(*args, **kwargs)
    return decorated


# =============================================================================
# EXAMPLE USAGE
# =============================================================================
if __name__ == "__main__":
    # Generate token
    token = generate_token("user123", "admin")
    print(f"Token: {token}")
    
    # Verify token
    result = verify_token(token)
    print(f"Valid: {result['valid']}")
    print(f"Payload: {result.get('payload')}")

