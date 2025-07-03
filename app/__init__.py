from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

# instantiate extensions

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    """Application factory"""
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # init extensions
    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)

    # register blueprints
    from .controllers.home_controller import home_bp
    app.register_blueprint(home_bp)

    return app
