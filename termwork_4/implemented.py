from dao.movies import MovieDAO
from service.movies import MovieService
from dao.genres import GenreDAO
from service.genres import GenreService
from dao.directors import DirectorDAO
from service.directors import DitrectorService
from dao.users import UserDAO
from service.users import UserService
from service.favorite_movies import FavoriteMovieService
from dao.favorite_movies import FavoriteMoviesDAO

from setup_db import db

movie_dao = MovieDAO(session=db.session)
movie_service = MovieService(dao=movie_dao)

genre_dao = GenreDAO(session=db.session)
genre_service = GenreService(dao=genre_dao)

director_dao = DirectorDAO(session=db.session)
director_service = DitrectorService(dao=director_dao)

user_dao = UserDAO(session=db.session)
user_service = UserService(dao=user_dao)

f_movie_dao = FavoriteMoviesDAO(session=db.session)
f_movie_service = FavoriteMovieService(dao=f_movie_dao)