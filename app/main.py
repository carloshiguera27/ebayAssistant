from fastapi import FastAPI
from core.config import settings

app = FastAPI(title=settings.app_name)

@app.get("/status")
def status():
    return {"status": "ok", "user": "not_logged_in"}

