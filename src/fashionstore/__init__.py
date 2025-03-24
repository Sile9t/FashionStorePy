import os
from flask import Flask, render_template
from config import settings
from loguru import logger
from .dao.database import async_session_maker
from .containers import Container

def create_app(test_config=None):
    container = Container()
    
    db = container.db()
    db.create_database()
    
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=settings.get_db_url()
    # )
    app.config = settings
    app.container = container

    
    if test_config in None:
        app.config.from_file('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    
    log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "log.txt")
    logger.add(log_file_path, format=settings.FORMAT_LOG, level="INFO", rotation=settings.LOG_ROTATION)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        # return "Hello! This is index page."
        return render_template('index.html')
    
    from .controllers import auth, brand
    app.register_blueprint(auth.bp)
    app.register_blueprint(brand.bp)

    return app