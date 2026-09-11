from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from server import db
from server.config import Config

from server.routes.auth import auth_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)
    JWTManager(app)

    app.register_blueprint(auth_bp)

    return app


app = create_app()
