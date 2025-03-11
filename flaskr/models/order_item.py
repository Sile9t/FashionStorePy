from sqlalchemy import Column, Integer, Float, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from base import Base

class OrderItem(Base):
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), index=True)
    clothing_id = Column(Integer, ForeignKey('clothings.id'), index=True)
    size_id = Column(Integer, ForeignKey('sizes.id'), index=True)
    quantity = Column(Integer, CheckConstraint('quanity >= 0'), nullable=False)
    price = Column(Float, CheckConstraint('price >= 0'), nullable=False)

    order = relationship('Order', back_populates='items', lazy='joined')
    clothing = relationship('Clothing', back_populates='order_items', lazy='joined')
    size = relationship('Size', back_populates='order_items', lazy='joined')