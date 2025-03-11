from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

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