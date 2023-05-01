from dao.models.favorite_movies import FavoritMovies, FavoriteMoviesSchema
from dao.models.user import User
from setup_db import db



class FavoriteMoviesDAO:
    def __init__(self, session):
        self.session = session

    def add_movie_to_favorites(self, user_id, movie_id):
        data = {"user_id": user_id, "movie_id": movie_id}
        new_movie = FavoritMovies(**data)
        db.session.add(new_movie)
        db.session.commit()

    def delete_movie_from_favorites(self, uid, movie_id):
        favor_id_lst = FavoritMovies.query.filter(FavoritMovies.movie_id == movie_id).all()
        print(favor_id_lst)
        print(type(favor_id_lst))
        for obj in favor_id_lst:
            if obj.user_id == uid:
                db.session.delete(obj)
                db.session.commit()
