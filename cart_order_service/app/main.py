from fastapi import FastAPI
from app.api.routes_cart_order import router as cart_router
from app.database.base import Base
from app.database.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cart & Order Service")
app.include_router(cart_router, prefix="/api", tags=["Cart & Order"])
