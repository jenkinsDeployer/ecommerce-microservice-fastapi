from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from app.database.session import SessionLocal
from app.schemas.userSechma import UserCreate, UserLogin, Token
from app.services.auth import register_user, login_user, refresh_access_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=dict)
def register(user: UserCreate, db: Session = Depends(get_db)):
    register_user(user, db)
    return {"message": "User registered successfully"}

@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    return login_user(user.email, user.password, db)


@router.post("/refresh", response_model=Token)
def refresh(refresh_token: str = Body(...)):
    return refresh_access_token(refresh_token)
