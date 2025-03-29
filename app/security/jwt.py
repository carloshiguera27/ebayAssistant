from datetime import datetime, timedelta
from jose import jwt
from app.core.config import settings

def create_access_token(data: dict, expiresMinutes: int = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expiresMinutes or settings.access_token_expire_minutes)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)