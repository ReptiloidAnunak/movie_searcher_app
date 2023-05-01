from marshmallow import Schema, fields

from setup_db import db

class FavoritMovies(db.Model):
    __tablename__ = "favorite_movies"
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    user = db.relationship("User")
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"), primary_key=True)
    movie = db.relationship("Movie")

class FavoriteMoviesSchema(Schema):
    user_id = fields.Integer()
    movie_id = fields.Integer()

