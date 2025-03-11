import enum
from datetime import datetime
from sqlalchemy import Column, Integer, Text, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class ShipmentStatus(enum.Enum):
    pending = "pending"
    in_transit = "in_transit"
    delivered = "delivered"
    returned = "returned"
    
class Shipment(Base):
    __tablename__ = 'shipments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), index=True)
    address = Column(Text, nullable=False)
    tracking_number = Column(String(100))
    status = Column(ShipmentStatus, default=ShipmentStatus.pending, nullable=False)
    shipped_at = Column(DateTime, default=datetime.utcnow)

    order = relationship('Order', back_populates='shipments', lazy='joined')