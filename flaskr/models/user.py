from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, CheckConstraint
from sqlalchemy.orm import DeclarativeBase, relationship
from base import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True, index=True)
    email = Column(String(100), nullable=False, unique=True, index=True)
    password_hash = Column(String(255), nullable=False)
    first_name = Column(String(50))
    last_name = Column(String(50))
    phone = Column(String(20), CheckConstraint("LENGTH(phone) >= 10"))
    address = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    cart_items = relationship('Cart', back_populates='user', lazy='joined')
    favourites = relationship('Favourite', back_populates='user', lazy='joined')
    orders = relationship('Order', back_populates='user', lazy='joined')
    reviews = relationship('Review', back_populates='user', lazy='joined')
