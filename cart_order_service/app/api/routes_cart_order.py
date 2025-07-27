from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import SessionLocal
from app.services import cart_order
from app.schemas import cartSchema as cart_schema, orderSchema as order_schema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

USER_ID = 1  # static for now

@router.post("/cart", response_model=cart_schema.CartItemOut)
def add_to_cart(data: cart_schema.CartAdd, db: Session = Depends(get_db)):
    return cart_order.add_to_cart(USER_ID, data.product_id, data.quantity, db)

@router.get("/cart", response_model=list[cart_schema.CartItemOut])
def view_cart(db: Session = Depends(get_db)):
    return cart_order.get_cart(USER_ID, db)

@router.patch("/cart/{item_id}", response_model=cart_schema.CartItemOut)
def update_cart(item_id: int, data: cart_schema.CartUpdate, db: Session = Depends(get_db)):
    return cart_order.update_cart_item(item_id, data.quantity, db)

@router.delete("/cart/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    success = cart_order.delete_cart_item(item_id, db)
    if not success:
        raise HTTPException(status_code=404, detail="Cart item not found")
    return {"message": "Deleted"}

@router.post("/order", response_model=order_schema.OrderOut)
def place_order(db: Session = Depends(get_db)):
    return cart_order.place_order(USER_ID, db)
