from datetime import datetime
from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from base import Base

class Discount(Base):
    __tablename__ = 'discounts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    clothing_id = Column(Integer, ForeignKey('clothing.id'), index=True)
    discount_percent = Column(Float, CheckConstraint('discount_percent >= 0 AND discount_percent <= 100'), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)

    clothing = relationship('Clothing', back_populates='discounts', lazy='joined')