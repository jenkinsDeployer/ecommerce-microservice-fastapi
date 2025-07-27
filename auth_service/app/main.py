from fastapi import FastAPI
from app.api.routes_auth import router as auth_router
from app.database.base import Base
from app.database.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Auth Service")

app.include_router(auth_router, prefix="/api/auth")