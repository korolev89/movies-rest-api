from flask import Flask
from flask_restx import Api
from config import Config
from setup_db import db
from views.movies import movies_ns
from views.directors import directors_ns
from views.genres import genres_ns
from views.auth import auth_ns
from views.users import users_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.app.config["RESTX_JSON"] = {"ensure_ascii": False, 'indent': 4}
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(users_ns)


if __name__ == "__main__":
    app_config = Config()
    app = create_app(app_config)
    app.run()
