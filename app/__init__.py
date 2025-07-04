from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flasgger import Swagger

# instantiate extensions

db = SQLAlchemy()
migrate = Migrate()
swagger = Swagger()
swagger_template = {
    "components": {
        "schemas": {
            "Product": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"},
                    "price": {"type": "number"},
                },
            }
        }
    }
}


def create_app():
    """Application factory"""
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # init extensions
    CORS(app)
    db.init_app(app)
    app.config["SWAGGER"] = {
        "title": "Flask REST API",
        "uiversion": 3,
        "openapi": "3.0.2",
    }
    swagger.init_app(app, template=swagger_template)

    # Import models so they are registered with SQLAlchemy before migrations
    from . import models  # noqa: F401

    migrate.init_app(app, db)

    # register blueprints
    from .controllers.home_controller import home_bp
    from .controllers.product_controller import product_bp
    app.register_blueprint(home_bp)
    app.register_blueprint(product_bp)

    return app
