from pydantic import BaseModel

class CartAdd(BaseModel):
    product_id: int
    quantity: int

class CartUpdate(BaseModel):
    quantity: int

class CartItemOut(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int
    price: float

    class Config:
        orm_mode = True
