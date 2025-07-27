from sqlalchemy import Column, Integer, Float, DateTime, String
from app.database.base import Base
from datetime import datetime

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    total = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
