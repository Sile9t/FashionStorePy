from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base, clothing_styles

class Style(Base):
    __tablename__ = 'styles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

    clothing = relationship('Clothing', secondary=clothing_styles, back_populates='style')