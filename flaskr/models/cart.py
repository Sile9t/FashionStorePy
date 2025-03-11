from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from base import Base

class Cart(Base):
    __tablename__ = 'cart'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    clothing_id = Column(Integer, ForeignKey('clothings.id'), index=True)
    size_id = Column(Integer, ForeignKey('sizes.id'), index=True)
    quantity = Column(Integer, CheckConstraint('quanity >= 0'), nullable=False)
    added_at = Column(DateTime, default=datetime.utcnow)

    user = relationship('User', back_populates='cart_items', lazy='joined')
    clothing = relationship('Clothing', back_populates='cart_items', lazy='joined')
    size = relationship('Size', back_populates='cart_items', lazy='joined')