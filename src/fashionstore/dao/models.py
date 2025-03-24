from typing import Annotated, List
from sqlalchemy import TIMESTAMP, Table, Integer, Float, String, Text, DateTime, ForeignKey, CheckConstraint, func
from sqlalchemy.orm import declared_attr, Mapped, relationship, DeclarativeBase, mapped_column
# from sqlalchemy.ext.asyncio import AsyncAttrs
from src.fashionstore.dao.database import Base
# from datetime import datetime

uniq_str_an = Annotated[str, mapped_column(unique=True)]
uniq_index_str_an = Annotated[str, mapped_column(unique=True, index=True)]

#TODO: add user birth_date and age fields
class User(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[uniq_index_str_an]
    email: Mapped[uniq_index_str_an]
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    first_name: Mapped[str | None] = mapped_column(String(50))
    last_name: Mapped[str | None] = mapped_column(String(50))
    phone: Mapped[str] = mapped_column(String(20), CheckConstraint("LENGTH(phone) >= 10"))
    address: Mapped[str]
    
    # cart_items = relationship("Cart", back_populates="user", cascade="all, delete-orphan")
    # favourites = relationship("Favourite", back_populates="user", cascade="all, delete-orphan")
    # orders = relationship("Order", back_populates="user", cascade="all, delete-orphan")
    # reviews = relationship("Review", back_populates="user", cascade="all, delete-orphan")

    def __init__(self, username, email, password_hash, first_name=None, last_name=None, phone=None,
                  address=None, cart_items=None, favourites=None, orders=None, reviews=None):
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.address = address
        # self.cart_items = cart_items
        # self.favourites = favourites
        # self.orders = orders
        # self.reviews = reviews

class Brand(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[uniq_index_str_an]
    country: Mapped[str] = mapped_column(String(50))
    website: Mapped[str | None] = mapped_column(String(255))

    clothings: Mapped[List["Clothing"] | None] = relationship(
        "Clothing",
        back_populates=("clothing.brand"),
        cascade="all, delete-orphan")

    def __init__(self, name, country=None, website=None):
        self.name = name
        self.country = country
        self.website = website

    def __repr__(self):
        return f"<Brand (name={self.name}, country={self.country}, website={self.website})>"
    
class ClothingType(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[uniq_index_str_an] = mapped_column(String(100))

    clothings: Mapped[List["Clothing"] | None] = relationship(
        "Clothing",
        back_populates="type",
        cascade="all, delete-orphan")

    def __init__(self, name):
        self.name = name

class Clothing(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    description: Mapped[str | None]
    brand_id: Mapped[int] = mapped_column( ForeignKey("brands.id"), index=True)
    type_id: Mapped[int] = mapped_column( ForeignKey("clothingtypes.id"), index=True)
    price: Mapped[float] = mapped_column(Float, CheckConstraint("price >= 0"), nullable=False)
    
    brand: Mapped["Brand"] = relationship("Brand", back_populates="clothings")
    type: Mapped["ClothingType"] = relationship("ClothingType", back_populates="clothings")
    # materials = relationship("Material", secondary=clothing_materials, back_populates="clothing")
    # colors = relationship("Color", secondary=clothing_colors, back_populates="clothing")
    # sizes = relationship("Size", secondary=clothing_sizes, back_populates="clothing")
    # seasons = relationship("Season", secondary=clothing_seasons, back_populates="clothing")
    # styles = relationship("Style", secondary=clothing_styles, back_populates="clothing")
    # categories = relationship("Category", secondary=clothing_categories, back_populates="clothing")
    # storage = relationship("Storage", back_populates="clothing")
    # cart_items = relationship("Cart", back_populates="clothing")
    # favourites = relationship("Favourite", back_populates="clothing")
    # order_items = relationship("OrderItem", back_populates="clothing")
    # reviews = relationship("Review", back_populates="clothing")
    # discounts = relationship("Discount", back_populates="clothing", lazy="joined")

    def __init__(self, name, description=None, brand_id=0, type_id=0, price=0):
        self.name = name
        self.description = description
        self.brand_id = brand_id
        self.type_id = type_id
        self.price = price

# class Material(Base):
#     __tablename__ = 'materials'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(100), nullable=False, index=True)

#     clothing = relationship('Clothing', secondary=clothing_materials, back_populates='materials')

#     def __init__(self, name):
#         self.name = name

# class Color(Base):
#     __tablename__ = 'colors'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(50), nullable=False, index=True)

#     clothing = relationship('Clothing', secondary=clothing_colors, back_populates='colors')

#     def __init__(self, name):
#         self.name = name

# class Size(Base):
#     __tablename__ = 'sizes'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(10), nullable=False, index=True)

#     clothing = relationship('Clothing', secondary=clothing_sizes, back_populates='sizes')
#     storage = relationship('Storage', back_populates='size')
#     cart_items = relationship('Cart', back_populates='size')
#     order_items = relationship('OrderItem', back_populates='size')

#     def __init__(self, name):
#         self.name = name

# class Season(Base):
#     __tablename__ = 'seasons'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(50), nullable=False, index=True)

#     clothing = relationship('Clothing', secondary=clothing_seasons, back_populates='seasons')

#     def __init__(self, name):
#         self.name = name

# class Style(Base):
#     __tablename__ = 'styles'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(100), nullable=False, index=True)

#     clothing = relationship('Clothing', secondary=clothing_styles, back_populates='styles')

#     def __init__(self, name):
#         self.name = name

# class Category(Base):
#     __tablename__ = 'categories'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(100), nullable=False, index=True)

#     clothing = relationship('Clothing', secondary=clothing_categories, back_populates='categories')

#     def __init__(self, name):
#         self.name = name

# class Storage(Base):
#     __tablename__ = 'storage'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     clothing_id = Column(Integer, ForeignKey('clothing.id'), index=True)
#     size_id = Column(Integer, ForeignKey('sizes.id'), index=True)
#     quantity = Column(Integer, CheckConstraint('quantity >= 0'), nullable=False)
#     last_updated = Column(DateTime, default=datetime.utcnow)

#     clothing = relationship('Clothing', back_populates='storage')
#     size = relationship('Size', back_populates='storage')

#     def __init__(self, clothing_id, size_id, quanity):
#         self.clothing_id = clothing_id
#         self.size_id = size_id
#         self.quantity = quanity

# class Cart(Base):
#     __tablename__ = 'cart'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(Integer, ForeignKey('users.id'), index=True)
#     clothing_id = Column(Integer, ForeignKey('clothing.id'), index=True)
#     size_id = Column(Integer, ForeignKey('sizes.id'), index=True)
#     quantity = Column(Integer, CheckConstraint('quantity >= 0'), nullable=False)
#     added_at = Column(DateTime, default=datetime.utcnow)

#     user = relationship('User', back_populates='cart_items')
#     clothing = relationship('Clothing', back_populates='cart_items')
#     size = relationship('Size', back_populates='cart_items')

#     def __init__(self, user_id, clothing_id, size_id, quanity):
#         self.user_id = user_id
#         self.clothing_id = clothing_id
#         self.size_id = size_id
#         self.quantity = quanity

# class Favourite(Base):
#     __tablename__ = 'favourites'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(Integer, ForeignKey('users.id'), index=True)
#     clothing_id = Column(Integer, ForeignKey('clothing.id'), index=True)
#     added_at = Column(DateTime, default=datetime.utcnow)

#     user = relationship('User', back_populates='favourites')
#     clothing = relationship('Clothing', back_populates='favourites')

#     def __init__(self, user_id, clothing_id):
#         self.user_id = user_id
#         self.clothing_id = clothing_id

# class Order(Base):
#     __tablename__ = 'orders'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(Integer, ForeignKey('users.id'), index=True)
#     total_amount = Column(Float, CheckConstraint('total_amount >= 0'), nullable=False)
#     status = Column(String(50), nullable=False)
#     created_at = Column(DateTime, default=datetime.utcnow)
#     updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

#     user = relationship('User', back_populates='orders')
#     items = relationship('OrderItem', back_populates='order')
#     payments = relationship('Payment', back_populates='order', lazy='joined')
#     shipments = relationship('Shipment', back_populates='order', lazy='joined')

#     def __init__(self, user_id):
#         self.user_id = user_id

# class OrderItem(Base):
#     __tablename__ = 'order_items'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     order_id = Column(Integer, ForeignKey('orders.id'), index=True)
#     clothing_id = Column(Integer, ForeignKey('clothing.id'), index=True)
#     size_id = Column(Integer, ForeignKey('sizes.id'), index=True)
#     quantity = Column(Integer, CheckConstraint('quantity >= 0'), nullable=False)
#     price = Column(Float, CheckConstraint('price >= 0'), nullable=False)

#     order = relationship('Order', back_populates='items')
#     clothing = relationship('Clothing', back_populates='order_items')
#     size = relationship('Size', back_populates='order_items')

#     def __init__(self, order_id, clothing_id, size_id, quanity):
#         self.order_id = order_id
#         self.clothing_id = clothing_id
#         self.size_id = size_id 
#         self.quantity = quanity

# class Review(Base):
#     __tablename__ = 'reviews'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(Integer, ForeignKey('users.id'), index=True)
#     clothing_id = Column(Integer, ForeignKey('clothing.id'), index=True)
#     rating = Column(Integer, CheckConstraint('rating >= 1 AND rating <= 5'), nullable=False)
#     comment = Column(Text)
#     created_at = Column(DateTime, default=datetime.utcnow)

#     user = relationship('User', back_populates='reviews')
#     clothing = relationship('Clothing', back_populates='reviews')

#     def __init__(self, user_id, clothing_id, rating):
#         self.user_id = user_id
#         self.clothing_id = clothing_id
#         self.rating = rating

# class Discount(Base):
#     __tablename__ = 'discounts'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     clothing_id = Column(Integer, ForeignKey('clothing.id'), index=True)
#     discount_percent = Column(Float, CheckConstraint('discount_percent >= 0 AND discount_percent <= 100'), nullable=False)
#     start_date = Column(DateTime, nullable=False)
#     end_date = Column(DateTime, nullable=False)

#     clothing = relationship('Clothing', back_populates='discounts')

#     def __init__(self, clothing_id, discount_percent):
#         self.clothing_id = clothing_id
#         self.discount_percent = discount_percent

# class Payment(Base):
#     __tablename__ = 'payments'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     order_id = Column(Integer, ForeignKey('orders.id'), index=True)
#     amount = Column(Float, CheckConstraint('amount >= 0'), nullable=False)
#     payment_method = Column(String(50), nullable=False)
#     status = Column(String(50), nullable=False)
#     created_at = Column(DateTime, default=datetime.utcnow)

#     order = relationship('Order', back_populates='payments')

#     def __init__(self, order_id, amount, payment_method):
#         self.order_id = order_id
#         self.amount = amount
#         self.payment_method = payment_method

# class Shipment(Base):
#     __tablename__ = 'shipments'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     order_id = Column(Integer, ForeignKey('orders.id'), index=True)
#     address = Column(Text, nullable=False)
#     tracking_number = Column(String(100))
#     status = Column(String(50), nullable=False)
#     shipped_at = Column(DateTime, default=datetime.utcnow)

#     order = relationship('Order', back_populates='shipments')

#     def __init__(self, order_id, address, tracking_number):
#         self.order_id = order_id
#         self.address = address
#         self.tracking_number = tracking_number