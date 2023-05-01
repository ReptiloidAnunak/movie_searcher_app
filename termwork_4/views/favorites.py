import jwt
from dao.models.user import User
from flask import request
from flask_restx import Resource, Namespace
from implemented import movie_service, user_service, f_movie_service
from config import Config
from utils import auth_required



favorites_ns = Namespace('favorites')

@favorites_ns.route('/movies/<int:id>')
class FavoritesView(Resource):
    @auth_required
    def post(self, id):
        movie = movie_service.get_one(id)
        f_movie_id = movie.id

        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]

        decoded_data = jwt.decode(token, Config.JWT_SECRET, algorithms=[Config.JWT_ALGO])
        print(decoded_data)
        user_email = decoded_data.get("email", None)
        user = User.query.filter_by(email=user_email).first()
        user_id = user.id
        f_movie_service.add_movie_to_favorites(user_id, f_movie_id)

        return f"Фильм {movie.title} добавлен в Избранное", 201

    @auth_required
    def delete(self, id):
        movie = movie_service.get_one(id)
        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]

        decoded_data = jwt.decode(token, Config.JWT_SECRET, algorithms=[Config.JWT_ALGO])
        print("Decoded_data_from_view_del:", decoded_data)
        user_email = decoded_data.get("email")
        user = User.query.filter_by(email=user_email).first()
        user_id = user.id
        print(user_id)
        f_movie_service.dlt_movie_from_favorites(user_id, id)
        return "", 204



