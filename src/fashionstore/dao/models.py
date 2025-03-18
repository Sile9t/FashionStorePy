from typing import Annotated, List
from sqlalchemy import TIMESTAMP, Table, Integer, Float, String, Text, DateTime, ForeignKey, CheckConstraint, func
from sqlalchemy.orm import declared_attr, Mapped, relationship, DeclarativeBase, mapped_column
# from sqlalchemy.ext.asyncio import AsyncAttrs
from src.fashionstore.dao.database import Base
# from datetime import datetime

uniq_str_an = Annotated[str, mapped_column(unique=True)]
uniq_index_str_an = Annotated[str, mapped_column(unique=True, index=True)]

# class Base(AsyncAttrs, DeclarativeBase):
#     __abstract__ = True

#     @classmethod
#     @property
#     @declared_attr.directive
#     def __tablename__(cls) -> str:
#         return cls.__name__.lower() + 's'

class User(Base):
    # id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[uniq_index_str_an]
    email: Mapped[uniq_index_str_an]
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    first_name: Mapped[str | None] = mapped_column(String(50))
    last_name: Mapped[str | None] = mapped_column(String(50))
    phone: Mapped[str] = mapped_column(String(20), CheckConstraint("LENGTH(phone) >= 10"))
    address: Mapped[str]
    # created_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())

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
    # id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[uniq_index_str_an] = mapped_column(String(100))

    clothings: Mapped[List["Clothing"] | None] = relationship(
        "Clothing",
        back_populates="type",
        cascade="all, delete-orphan")

    def __init__(self, name):
        self.name = name

class Clothing(Base):
    # id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    description: Mapped[str | None]
    brand_id: Mapped[int] = mapped_column( ForeignKey("brands.id"), index=True)
    type_id: Mapped[int] = mapped_column( ForeignKey("clothingtypes.id"), index=True)
    price: Mapped[float] = mapped_column(Float, CheckConstraint("price >= 0"), nullable=False)
    # created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=func.now())

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