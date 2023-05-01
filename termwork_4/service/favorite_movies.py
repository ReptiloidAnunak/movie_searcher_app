from dao.favorite_movies import FavoriteMoviesDAO

class FavoriteMovieService:
    def __init__(self, dao: FavoriteMoviesDAO):
        self.dao = dao

    def add_movie_to_favorites(self, user_id, movie_id):
        self.dao.add_movie_to_favorites(user_id, movie_id)

    def dlt_movie_from_favorites(self, user_id, movie_id):
        self.dao.delete_movie_from_favorites(user_id, movie_id)