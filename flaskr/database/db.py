from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import click
from models.base import Base
from models.brand import Brand
from models.cart import Cart
from models.category import Category
from models.clothing import Clothing
from models.clothing_type import ClothingType
from models.color import Color
from models.discount import Discount
from models.favourite import Favourite
from models.material import Material
from models.order import Order, OrderStatus
from models.order_item import OrderItem
from models.payment import Payment, PaymentStatus
from models.review import Review
from models.season import Season
from models.shipment import Shipment, ShipmentStatus
from models.size import Size
from models.storage import Storage
from models.style import Style
from models.user import User
from flask import current_app, g

engine = create_engine('sqlite:///tmp/fashionStore.db')

Session = sessionmaker(
    autocommit = False,
    autoflusj = False,
    ding = engine
)

session = Session()

def init_db():
    Base.metadata.create_all(engine)
    g.db = session    

def close_db():
    db = g.get('db', None)

    if db is not None:
        db.close()
        
@click.command('init-db')
def init_db_command():
    init_db()
    click.echo('Initialized the database.')

def init_app(app):    
    app.teardown_appcontext()
    app.cli.add_command(init_db_command)