from pydantic import BaseModel
from datetime import datetime

class OrderOut(BaseModel):
    id: int
    user_id: int
    total: float
    created_at: datetime

    class Config:
        orm_mode = True
