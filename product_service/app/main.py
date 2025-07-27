from fastapi import FastAPI
from app.api.routes_product import router as product_router
from app.database.base import Base
from app.database.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Product Service")

app.include_router(product_router, prefix="/api/products", tags=["Products"])
