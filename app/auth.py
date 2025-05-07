import jwt
import uuid
from datetime import datetime, timedelta

SECRET_KEY = "clave-super-secreta"

def create_jwt():
    payload = {
        "sub": str(uuid.uuid4()),
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + timedelta(seconds=60)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

