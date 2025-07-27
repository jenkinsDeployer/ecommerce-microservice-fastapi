from sqlalchemy.orm import Session
from app.models.cartModel import CartItem
from app.models.orderModel import Order
from app.core.config import settings
import requests

def add_to_cart(user_id: int, product_id: int, quantity: int, db: Session):
    product = requests.get(f"{settings.PRODUCT_SERVICE_URL}/{product_id}").json()
    price = product["price"]
    item = CartItem(user_id=user_id, product_id=product_id, quantity=quantity, price=price)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def get_cart(user_id: int, db: Session):
    return db.query(CartItem).filter(CartItem.user_id == user_id).all()

def update_cart_item(item_id: int, quantity: int, db: Session):
    item = db.query(CartItem).filter(CartItem.id == item_id).first()
    if item:
        item.quantity = quantity
        db.commit()
        db.refresh(item)
    return item

def delete_cart_item(item_id: int, db: Session):
    item = db.query(CartItem).filter(CartItem.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
        return True
    return False

def place_order(user_id: int, db: Session):
    cart = get_cart(user_id, db)
    total = sum([item.price * item.quantity for item in cart])

    order = Order(user_id=user_id, total=total)
    db.add(order)
    db.commit()
    db.refresh(order)

    for item in cart:
        requests.patch(f"{settings.PRODUCT_SERVICE_URL}/{item.product_id}", json={"inventory": item.quantity * -1})
        db.delete(item)

    db.commit()
    return order
