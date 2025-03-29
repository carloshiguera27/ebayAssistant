from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user import User
from app.schemas.user import UserCreate, UserOut
from app.security.hash import hash_password, verify_password
from app.security.jwt import create_access_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=UserOut)
def register(user:UserCreate, db: Session =Depends(get_db)):
    existing = db.query(User).filter(User.email == user.email).first()

    if existing:
        raise HTTPException(status_code=400, detail="Email ya registrado")
    
    dbUser = User(
        username=user.username,
        email=user.email,
        hashed_pasword=hash_password(user.password),
        role="user"
    )
    db.add(dbUser)
    db.commit()
    db.refresh(dbUser)
    return dbUser

@router.post("/login")
def login(form_data: UserCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.email).first()

    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Usuario no encontrado, o credenciales invalidas")
    
    accessToken = create_access_token(data={'sub': user.email})
    return {"access_token": accessToken, 
            "token_type": "bearer"}

