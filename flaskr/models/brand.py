from typing import Optional
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, relationship
from base import Base

class Brand(Base):
    __tablename__ = 'brands'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, index=True)
    country = Column(String(50))
    website = Column(String(255))

    # Связи
    clothing = relationship('Clothing', back_populates='brand', lazy='joined')
