import json

import jwt
from flask import request, abort
from flask_restx import Resource, Namespace
from implemented import user_service
from config import Config

from utils import generate_tokens

from dao.models.user import User, UserSchema

auth_ns = Namespace('auth')

@auth_ns.route('/register')
class AuthRegView(Resource):
    def post(self):
        new_user_data = json.loads(request.data)
        new_user = user_service.create(new_user_data)
        return "", 201, {"location": f"/users/{new_user.id}"}

@auth_ns.route('/logging')
class AuthLogView(Resource):
    def post(self):
        user_data = json.loads(request.data)
        user_email = user_data.get('email', None)
        user_pwd = user_data.get('password', None)

        if None in [user_email, user_pwd]:
            return "Нет логина или пароля", 400

        user = User.query.filter(User.email == user_email).first()

        if user is None:
            raise abort(404)

        if user.compare_password(user_pwd) == False:
            return "Пароль неверный"

        data = {"email": user.email,
                "password": str(user.password)}

        return generate_tokens(data), 200

    def put(self):
        try:
            data = json.loads(request.data)
            refresh_token = data.get("refresh_token")
            decoded_data = jwt.decode(jwt=refresh_token, key=Config.JWT_SECRET, algorithms=Config.JWT_ALGO)
        except Exception as e:
            print('JWT decode exception', e)
            return 'Token is not valid:', 404

        user_email = decoded_data.get("email", None)
        data = {"email": user_email, "password": None}
        return generate_tokens(data, is_refresh=True), 200
