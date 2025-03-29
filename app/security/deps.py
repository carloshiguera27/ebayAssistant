from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from app.core.config import settings

oauth2Scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str= Depends(oauth2Scheme)):
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        return payload["sub"]
    except JWTError:
        raise HTTPException(status_code=401, detail="Token invalido")