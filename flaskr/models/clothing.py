from datetime import datetime
from sqlalchemy import Column, Integer, Float,String, Text, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from base import Base, clothing_materials, clothing_colors, clothing_sizes, clothing_seasons, clothing_styles, clothing_categories

class Clothing(Base):
    __tablename__ = 'clothings'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, index=True)
    description = Column(Text)
    brand_id = Column(Integer, ForeignKey('brands.id'), index=True)
    type_id = Column(Integer, ForeignKey('clothing_types.id'), index=True)
    price = Column(Float, CheckConstraint('price >= 0'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    brand = relationship('Brand', back_populates='clothing', lazy='joined')
    type = relationship('ClothingType', back_populates='clothing', lazy='joined')
    materials = relationship('Material', secondary=clothing_materials, back_populates='clothing', lazy='joined')
    colors = relationship('Color', secondary=clothing_colors, back_populates='clothing', lazy='joined')
    sizes = relationship('Size', secondary=clothing_sizes, back_populates='clothing', lazy='joined')
    seasons = relationship('Season', secondary=clothing_seasons, back_populates='clothing', lazy='joined')
    styles = relationship('Style', secondary=clothing_styles, back_populates='clothing', lazy='joined')
    categories = relationship('Category', secondary=clothing_categories, back_populates='clothing', lazy='joined')
    storage = relationship('Storage', back_populates='clothing', lazy='joined')
    cart_items = relationship('Cart', back_populates='clothing', lazy='joined')
    favourites = relationship('Favourite', back_populates='clothing', lazy='joined')
    order_items = relationship('OrderItem', back_populates='clothing', lazy='joined')
    reviews = relationship('Review', back_populates='clothing', lazy='joined')