from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import timedelta

from jose import jwt, JWTError
from app.core.config import settings

from app.models.userModel import User
from app.schemas.userSechma import UserCreate
from app.core.security import hash_password, verify_password, create_access_token, create_refresh_token

def register_user(user: UserCreate, db: Session):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(email=user.email, password=hash_password(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# def login_user(email: str, password: str, db: Session):
#     db_user = db.query(User).filter(User.email == email).first()
#     if not db_user or not verify_password(password, db_user.password):
#         raise HTTPException(status_code=401, detail="Invalid credentials")

#     token = create_access_token({"sub": db_user.email})
#     return {"access_token": token}


def login_user(email: str, password: str, db: Session):
    db_user = db.query(User).filter(User.email == email).first()
    if not db_user or not verify_password(password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        {"sub": db_user.email}, expires_delta=access_token_expires
    )

    refresh_token = create_refresh_token({"sub": db_user.email})

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "expires_in": 1800  # 30 minutes in seconds
    }




def refresh_access_token(refresh_token: str):
    try:
        payload = jwt.decode(refresh_token,settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email = payload.get("sub")
        if not email:
            raise HTTPException(status_code=401, detail="Invalid token")

        access_token = create_access_token({"sub": email})
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
            "expires_in": 1800
        }
    except JWTError:
        raise HTTPException(status_code=401, detail="Token expired or invalid")
