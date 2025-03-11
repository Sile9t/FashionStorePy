from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from base import Base

class Storage(Base):
    __tablename__ = 'storage'
    id = Column(Integer, primary_key=True, autoincrement=True)
    clothing_id = Column(Integer, ForeignKey('clothings.id'), index=True)
    size_id = Column(Integer, ForeignKey('sizes.id'), index=True)
    quantity = Column(Integer, CheckConstraint('quanity >= 0'), nullable=False)
    last_updated = Column(DateTime, default=datetime.utcnow)

    clothing = relationship('Clothing', back_populates='storage', lazy='joined')
    size = relationship('Size', back_populates='storage', lazy='joined')