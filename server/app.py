from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from server import db
from server.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)
    JWTManager(app)

    return app


app = create_app()
