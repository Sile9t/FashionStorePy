from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base, clothing_colors

class Color(Base):
    __tablename__ = 'colors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, index=True)

    clothing = relationship('Clothing', secondary=clothing_colors, back_populates='colors', lazy='joined')