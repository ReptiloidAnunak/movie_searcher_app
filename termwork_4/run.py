from flask import Flask
from flask_restx import Api

from setup_db import db

from config import Config
from views.genres import genre_ns
from views.directors import director_ns
from views.movies import movie_ns
from views.users import user_ns
from views.auth import auth_ns


def create_app(config: Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    app.app_context().push()
    register_extention(app)
    return app

def register_extention(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)

app = create_app(Config())
app.debug = True


if __name__ == "__main__":
    app.run(host="localhost", port=10001, debug=True)
