import json

from flask import request
from flask_restx import Resource, Namespace

from dao.models.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')

@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genre_service.get_all()
        res = GenreSchema(many=True).dump(genres)
        return res, 200

    def post(self):
        req_json = json.loads(request.data)
        new_genre = genre_service.create(req_json)
        return "", 201, {"location": f"/genres/{new_genre.id}"}


@genre_ns.route('/page=<int:p>')
class GenrePageView(Resource):
    def get(self, p):
        genres = genre_service.get_all_paginated(p)
        res = GenreSchema(many=True).dump(genres)
        return res, 200

@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        genre = genre_service.get_one(gid)
        res = GenreSchema().dump(genre)
        return res, 200

    def put(self, gid):
        req = json.loads(request.data)
        if "id" not in req:
            req["id"] == gid
        genre_service.update(req)
        return "", 204

    def delete(self, gid):
        genre_service.delete(gid)
        return "", 204