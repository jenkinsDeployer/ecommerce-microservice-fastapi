from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    description: str | None = None
    price: float
    category: str | None = None
    inventory: int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    category: str | None = None
    inventory: int | None = None

class ProductOut(ProductBase):
    id: int

    class Config:
        orm_mode = True
