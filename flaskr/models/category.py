from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base, clothing_categories

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, index=True)

    clothing = relationship('Clothing', secondary=clothing_categories, back_populates='categories', lazy='joined')