import json

from flask import request
from flask_restx import Resource, Namespace

from dao.models.user import UserSchema
from implemented import user_service
from utils import auth_required

user_ns = Namespace('user')

@user_ns.route('/<int:uid>')
class UserView(Resource):
    @auth_required
    def get(self, uid):
        user = user_service.get_one(uid)
        res = UserSchema().dump(user)
        del res["password"]
        return res, 200

    @auth_required
    def patch(self, uid):
        req = json.loads(request.data)
        if "uid" not in req:
            req["id"] = uid
        user_service.update(req)
        return "", 204

    @auth_required
    def delete(self, uid):
        user_service.delete(uid)
        return "", 201

@user_ns.route('/<int:uid>/password')
class UserPwdView(Resource):
    @auth_required
    def put(self, uid):
        req = json.loads(request.data)
        if "uid" not in req:
            req["id"] = uid

        if "password_1" not in req or "password_2" not in req:
            return "Введите старый и новый пароли"

        user_service.update_password(req)

        if not user_service.update_password(req) == False:
            return "Неверный пароль", 401

        return "", 204



