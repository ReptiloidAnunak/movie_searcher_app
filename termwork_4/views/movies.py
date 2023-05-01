import json

from flask import request
from flask_restx import Resource, Namespace

from dao.models.movie import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')

@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        movies = movie_service.get_all()
        res = MovieSchema(many=True).dump(movies)
        return res, 200

    def post(self):
        req_json = json.loads(request.data)
        new_movie = movie_service.create(req_json)
        return "", 201, {"location": f"/movies/{new_movie.id}"}


@movie_ns.route('/page=<int:p>')
class MoviesView(Resource):
    def get(self, p):
        movies = movie_service.get_all_paginated(p)
        res = MovieSchema(many=True).dump(movies)
        return res, 200

@movie_ns.route('/status=new&page=<int:p>')
class MoviesView(Resource):
    def get(self, p):
        movies = movie_service.get_new_paginated(p)
        res = MovieSchema(many=True).dump(movies)
        return res, 200


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        res = MovieSchema().dump(movie)
        return res, 200

    def put(self, mid):
        req = json.loads(request.data)
        if "id" not in req:
            req["id"] == mid
        movie_service.update(req)
        return "", 204

    def delete(self, mid):
        movie_service.delete(mid)
        return "", 204


