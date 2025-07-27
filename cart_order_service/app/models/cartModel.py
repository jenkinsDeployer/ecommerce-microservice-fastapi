from sqlalchemy import Column, Integer, Float
from app.database.base import Base

class CartItem(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    product_id = Column(Integer)
    quantity = Column(Integer)
    price = Column(Float)  # capture at time of add
