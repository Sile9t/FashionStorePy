from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base, clothing_seasons

class Season(Base):
    __tablename__ = 'seasons'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, index=True)

    clothing = relationship('Clothing', secondary=clothing_seasons, back_populates='seasons', lazy='joined')