from sqlalchemy.orm import Session
from typing import List

from app.models.productModel import Product
from app.schemas.productSchemas import ProductCreate, ProductUpdate

def create_product(product: ProductCreate, db: Session):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def create_products_bulk(products: List[ProductCreate], db: Session):
    db_products = []
    for product in products:
        db_product = Product(**product.dict())
        db.add(db_product)
        db.flush()  # flush ensures the ID is generated before commit
        db.refresh(db_product)
        db_products.append(db_product)
    
    db.commit()
    return db_products


def get_all_products(db: Session, skip=0, limit=10, category: str | None = None):
    query = db.query(Product)
    if category:
        query = query.filter(Product.category == category)
    return query.offset(skip).limit(limit).all()

def get_product_by_id(product_id: int, db: Session):
    return db.query(Product).filter(Product.id == product_id).first()

def update_product(product_id: int, update_data: ProductUpdate, db: Session):
    product = get_product_by_id(product_id, db)
    if not product:
        return None
    for field, value in update_data.dict(exclude_unset=True).items():
        setattr(product, field, value)
    db.commit()
    db.refresh(product)
    return product

def delete_product(product_id: int, db: Session):
    product = get_product_by_id(product_id, db)
    if not product:
        return False
    db.delete(product)
    db.commit()
    return True
