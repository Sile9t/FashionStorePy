from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class Favourite(Base):
    __tablename__ = 'favourites'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    clothing_id = Column(Integer, ForeignKey('clothings.id'), index=True)
    added_at = Column(DateTime, default=datetime.utcnow)

    user = relationship('User', back_populates='favourites', lazy='joined')
    clothing = relationship('Clothing', back_populates='favourites', lazy='joined')