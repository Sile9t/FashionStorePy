from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, relationship

class Base(DeclarativeBase):
    pass

class ClothingType(Base):
    __tablename__ = 'clothing_types'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, index=True)

    clothing = relationship('Clothing', back_populates='type', lazy='joined')