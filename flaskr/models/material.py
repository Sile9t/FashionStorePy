from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, relationship
from base import Base, clothing_materials

class Material(Base):
    __tablename__ = 'materials'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, index=True)

    # Связи
    clothing = relationship('Clothing', secondary=clothing_materials, back_populates='materials', lazy='joined')