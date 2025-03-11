from sqlalchemy import Table, Column, Integer, Float, String, Text, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship, DeclarativeBase
from datetime import datetime
from .database.db import Base

clothing_materials = Table(
    'clothing_materials', Base.metadata,
    Column('clothing_id', Integer, ForeignKey('clothing.id'), primary_key=True, index=True),
    Column('material_id', Integer, ForeignKey('materials.id'), primary_key=True, index=True)
)

clothing_colors = Table(
    'clothing_colors', Base.metadata,
    Column('clothing_id', Integer, ForeignKey('clothing.id'), primary_key=True, index=True),
    Column('color_id', Integer, ForeignKey('colors.id'), primary_key=True, index=True)
)

clothing_sizes = Table(
    'clothing_sizes', Base.metadata,
    Column('clothing_id', Integer, ForeignKey('clothing.id'), primary_key=True, index=True),
    Column('size_id', Integer, ForeignKey('sizes.id'), primary_key=True, index=True)
)

clothing_seasons = Table(
    'clothing_seasons', Base.metadata,
    Column('clothing_id', Integer, ForeignKey('clothing.id'), primary_key=True, index=True),
    Column('season_id', Integer, ForeignKey('seasons.id'), primary_key=True, index=True)
)

clothing_styles = Table(
    'clothing_styles', Base.metadata,
    Column('clothing_id', Integer, ForeignKey('clothing.id'), primary_key=True, index=True),
    Column('style_id', Integer, ForeignKey('styles.id'), primary_key=True, index=True)
)

clothing_categories = Table(
    'clothing_categories', Base.metadata,
    Column('clothing_id', Integer, ForeignKey('clothing.id'), primary_key=True, index=True),
    Column('category_id', Integer, ForeignKey('categories.id'), primary_key=True, index=True)
)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True, index=True)
    email = Column(String(100), nullable=False, unique=True, index=True)
    password_hash = Column(String(255), nullable=False)
    first_name = Column(String(50))
    last_name = Column(String(50))
    phone = Column(String(20), CheckConstraint('LENGTH(phone) >= 10'))
    address = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    cart_items = relationship('Cart', back_populates='user', cascade="all, delete-orphan", lazy="joined")
    favourites = relationship('Favourite', back_populates='user', cascade="all, delete-orphan", lazy="joined")
    orders = relationship('Order', back_populates='user', cascade="all, delete-orphan", lazy="joined")
    reviews = relationship('Review', back_populates='user', cascade="all, delete-orphan", lazy="joined")

    def __init__(self, username, email, password_hash):
        self.username = username
        self.email = email
        self.password_hash = password_hash

class Brand(Base):
    __tablename__ = 'brands'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, index=True)
    country = Column(String(50))
    website = Column(String(255))

    clothing = relationship('Clothing', back_populates='brand', lazy="joined")

    def __init__(self, name, country=None):
        self.name = name
        self.country = country

class ClothingType(Base):
    __tablename__ = 'clothing_types'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, index=True)

    clothing = relationship('Clothing', back_populates='type', lazy="joined")

    def __init__(self, name):
        self.name = name

class Clothing(Base):
    __tablename__ = 'clothing'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, index=True)
    description = Column(Text)
    brand_id = Column(Integer, ForeignKey('brands.id'), index=True)
    type_id = Column(Integer, ForeignKey('clothing_types.id'), index=True)
    price = Column(Float, CheckConstraint('price >= 0'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    brand = relationship('Brand', back_populates='clothing', lazy="joined")
    type = relationship('ClothingType', back_populates='clothing', lazy="joined")
    materials = relationship('Material', secondary=clothing_materials, back_populates='clothing', lazy="joined")
    colors = relationship('Color', secondary=clothing_colors, back_populates='clothing', lazy="joined")
    sizes = relationship('Size', secondary=clothing_sizes, back_populates='clothing', lazy="joined")
    seasons = relationship('Season', secondary=clothing_seasons, back_populates='clothing', lazy="joined")
    styles = relationship('Style', secondary=clothing_styles, back_populates='clothing', lazy="joined")
    categories = relationship('Category', secondary=clothing_categories, back_populates='clothing', lazy="joined")
    storage = relationship('Storage', back_populates='clothing', lazy="joined")
    cart_items = relationship('Cart', back_populates='clothing', lazy="joined")
    favourites = relationship('Favourite', back_populates='clothing', lazy="joined")
    order_items = relationship('OrderItem', back_populates='clothing', lazy="joined")
    reviews = relationship('Review', back_populates='clothing', lazy="joined")

    def __init__(self, name, brand_id, type_id):
        self.name = name
        self.brand_id = brand_id
        self.type_id = type_id

class Material(Base):
    __tablename__ = 'materials'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, index=True)

    clothing = relationship('Clothing', secondary=clothing_materials, back_populates='materials', lazy="joined")

    def __init__(self, name):
        self.name = name

class Color(Base):
    __tablename__ = 'colors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, index=True)

    clothing = relationship('Clothing', secondary=clothing_colors, back_populates='colors', lazy="joined")

    def __init__(self, name):
        self.name = name

class Size(Base):
    __tablename__ = 'sizes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(10), nullable=False, index=True)

    clothing = relationship('Clothing', secondary=clothing_sizes, back_populates='sizes', lazy="joined")
    storage = relationship('Storage', back_populates='size', lazy="joined")
    cart_items = relationship('Cart', back_populates='size', lazy="joined")
    order_items = relationship('OrderItem', back_populates='size', lazy="joined")

    def __init__(self, name):
        self.name = name

class Season(Base):
    __tablename__ = 'seasons'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, index=True)

    clothing = relationship('Clothing', secondary=clothing_seasons, back_populates='seasons', lazy="joined")

    def __init__(self, name):
        self.name = name

class Style(Base):
    __tablename__ = 'styles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, index=True)

    clothing = relationship('Clothing', secondary=clothing_styles, back_populates='styles', lazy="joined")

    def __init__(self, name):
        self.name = name

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, index=True)

    clothing = relationship('Clothing', secondary=clothing_categories, back_populates='categories', lazy="joined")

    def __init__(self, name):
        self.name = name

class Storage(Base):
    __tablename__ = 'storage'
    id = Column(Integer, primary_key=True, autoincrement=True)
    clothing_id = Column(Integer, ForeignKey('clothing.id'), index=True)
    size_id = Column(Integer, ForeignKey('sizes.id'), index=True)
    quantity = Column(Integer, CheckConstraint('quantity >= 0'), nullable=False)
    last_updated = Column(DateTime, default=datetime.utcnow)

    clothing = relationship('Clothing', back_populates='storage', lazy="joined")
    size = relationship('Size', back_populates='storage', lazy="joined")

    def __init__(self, clothing_id, size_id, quanity):
        self.clothing_id = clothing_id
        self.size_id = size_id
        self.quantity = quanity

class Cart(Base):
    __tablename__ = 'cart'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    clothing_id = Column(Integer, ForeignKey('clothing.id'), index=True)
    size_id = Column(Integer, ForeignKey('sizes.id'), index=True)
    quantity = Column(Integer, CheckConstraint('quantity >= 0'), nullable=False)
    added_at = Column(DateTime, default=datetime.utcnow)

    user = relationship('User', back_populates='cart_items', lazy="joined")
    clothing = relationship('Clothing', back_populates='cart_items', lazy="joined")
    size = relationship('Size', back_populates='cart_items', lazy="joined")

    def __init__(self, user_id, clothing_id, size_id, quanity):
        self.user_id = user_id
        self.clothing_id = clothing_id
        self.size_id = size_id
        self.quantity = quanity

class Favourite(Base):
    __tablename__ = 'favourites'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    clothing_id = Column(Integer, ForeignKey('clothing.id'), index=True)
    added_at = Column(DateTime, default=datetime.utcnow)

    user = relationship('User', back_populates='favourites', lazy="joined")
    clothing = relationship('Clothing', back_populates='favourites', lazy="joined")

    def __init__(self, user_id, clothing_id):
        self.user_id = user_id
        self.clothing_id = clothing_id

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    total_amount = Column(Float, CheckConstraint('total_amount >= 0'), nullable=False)
    status = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship('User', back_populates='orders', lazy="joined")
    items = relationship('OrderItem', back_populates='order', lazy="joined")

    def __init__(self, user_id):
        self.user_id = user_id

class OrderItem(Base):
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), index=True)
    clothing_id = Column(Integer, ForeignKey('clothing.id'), index=True)
    size_id = Column(Integer, ForeignKey('sizes.id'), index=True)
    quantity = Column(Integer, CheckConstraint('quantity >= 0'), nullable=False)
    price = Column(Float, CheckConstraint('price >= 0'), nullable=False)

    order = relationship('Order', back_populates='items', lazy="joined")
    clothing = relationship('Clothing', back_populates='order_items', lazy="joined")
    size = relationship('Size', back_populates='order_items', lazy="joined")

    def __init__(self, order_id, clothing_id, size_id, quanity):
        self.order_id = order_id
        self.clothing_id = clothing_id
        self.size_id = size_id 
        self.quantity = quanity

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    clothing_id = Column(Integer, ForeignKey('clothing.id'), index=True)
    rating = Column(Integer, CheckConstraint('rating >= 1 AND rating <= 5'), nullable=False)
    comment = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship('User', back_populates='reviews', lazy="joined")
    clothing = relationship('Clothing', back_populates='reviews', lazy="joined")

    def __init__(self, user_id, clothing_id, rating):
        self.user_id = user_id
        self.clothing_id = clothing_id
        self.rating = rating

class Discount(Base):
    __tablename__ = 'discounts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    clothing_id = Column(Integer, ForeignKey('clothing.id'), index=True)
    discount_percent = Column(Float, CheckConstraint('discount_percent >= 0 AND discount_percent <= 100'), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)

    clothing = relationship('Clothing', back_populates='discounts', lazy="joined")

    def __init__(self, clothing_id, discount_percent):
        self.clothing_id = clothing_id
        self.discount_percent = discount_percent

class Payment(Base):
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), index=True)
    amount = Column(Float, CheckConstraint('amount >= 0'), nullable=False)
    payment_method = Column(String(50), nullable=False)
    status = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    order = relationship('Order', back_populates='payments', lazy="joined")

    def __init__(self, order_id, amount, paymant_method):
        self.order_id = order_id
        self.amount = amount
        self.payment_method = paymant_method

class Shipment(Base):
    __tablename__ = 'shipments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), index=True)
    address = Column(Text, nullable=False)
    tracking_number = Column(String(100))
    status = Column(String(50), nullable=False)
    shipped_at = Column(DateTime, default=datetime.utcnow)

    order = relationship('Order', back_populates='shipments', lazy="joined")

    def __init__(self, order_id, address, tracking_number):
        self.order_id = order_id
        self.address = address
        self.tracking_number = tracking_number