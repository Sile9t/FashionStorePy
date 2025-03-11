import enum
from datetime import datetime
from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from base import Base

class PaymentStatus(enum.Enum):
    pending = "pending"
    completed = "completed"
    failed = "failed"

class Payment(Base):
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), index=True)
    amount = Column(Float, CheckConstraint('amount >= 0'), nullable=False)
    payment_method = Column(String(50), nullable=False)
    status = Column(PaymentStatus, default=PaymentStatus.pending, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    order = relationship('Order', back_populates='payments', lazy='joined')