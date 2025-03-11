from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base, clothing_sizes

class Size(Base):
    __tablename__ = 'sizes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(10), nullable=False, index=True)

    clothing = relationship('Clothing', secondary=clothing_sizes, back_populates='sizes', lazy='joined')
    storage = relationship('Storage', back_populates='size', lazy='joined')
    cart_items = relationship('Cart', back_populates='size', lazy='joined')
    order_items = relationship('OrderItem', back_populates='size', lazy='joined')