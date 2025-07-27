from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database.session import SessionLocal
from app.schemas.productSchemas import *
from app.services import productService as product_service

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ProductOut)
def create(product: ProductCreate, db: Session = Depends(get_db)):
    return product_service.create_product(product, db)

# ✅ New: Bulk product creation
@router.post("/bulk", response_model=List[ProductOut])
def create_products_bulk(products: List[ProductCreate], db: Session = Depends(get_db)):
    return product_service.create_products_bulk(products, db)

@router.get("/", response_model=list[ProductOut])
def list_products(skip: int = 0, limit: int = 10, category: str | None = None, db: Session = Depends(get_db)):
    return product_service.get_all_products(db, skip, limit, category)

@router.get("/{product_id}", response_model=ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = product_service.get_product_by_id(product_id, db)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.patch("/{product_id}", response_model=ProductOut)
def update(product_id: int, update_data: ProductUpdate, db: Session = Depends(get_db)):
    updated = product_service.update_product(product_id, update_data, db)
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated

@router.delete("/{product_id}")
def delete(product_id: int, db: Session = Depends(get_db)):
    success = product_service.delete_product(product_id, db)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted"}
