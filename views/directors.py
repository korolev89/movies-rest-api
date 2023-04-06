from flask_restx import Resource, Namespace
from container import directors_service
from dao.model.directors import DirectorsSchema

directors_ns = Namespace('directors')


@directors_ns.route("/")
class DirectorsView(Resource):
    def get(self):
        directors = directors_service.get_all()
        result = DirectorsSchema(many=True).dump(directors)

        return result, 200


@directors_ns.route("/<int:did>")
class DirectorsView(Resource):
    def get(self, did):
        director = directors_service.get_one(did)
        result = DirectorsSchema().dump(director)

        return result, 200
