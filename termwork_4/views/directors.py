import json

from flask import request
from flask_restx import Resource, Namespace

from dao.models.director import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')

@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = director_service.get_all()
        res = DirectorSchema(many=True).dump(directors)
        return res, 200

    def post(self):
        req_json = request.json()
        new_director = director_service.create(req_json)
        return "", 201, {"location": f"/directors/{new_director.id}"}

@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        director = director_service.get_one(did)
        res = DirectorSchema().dump(director)
        return res, 200

    def put(self, did):
        req = json.loads(request.data)
        if "id" not in req:
            req["id"] == did
        director_service.update(req)
        return "", 204

    def delete(self, did):
        director_service.delete(did)
        return "", 204