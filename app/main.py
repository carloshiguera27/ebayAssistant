from fastapi import FastAPI, Depends
from app.core.config import settings
from app.routes import user
from app.security.deps import get_current_user

app = FastAPI(title=settings.app_name)
app.include_router(user.router)

@app.get("/me")
def read_current_user(user= Depends(get_current_user)):
    return {"email": user}

@app.get("/status")
def status():
    return {
        "status": "ok", 
        "user": "not_logged_in"
    }