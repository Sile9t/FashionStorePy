from models import Brand
from sqlalchemy import Table
from database.db import Base, engine

brands = Table('brands', Base.metadata, autoload=True)
conn = engine.connect()

def addBrand():
    newBrand = Brand(name='Gucci', country='Italy')
    conn.execute(brands.insert(newBrand))