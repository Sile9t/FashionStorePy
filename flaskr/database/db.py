from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from flask import current_app, g

Base = declarative_base()

engine = create_engine('sqlite:///instance/fashionStore.db')

db_session = scoped_session(sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine
))

Base.query = db_session.query_property()

def init_db():
    from .. import models
    Base.metadata.create_all(engine)