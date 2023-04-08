from flask import request
from flask_restx import Resource, Namespace
from container import movies_service
from dao.model.movies import MoviesSchema
from helpers import auth_required, admin_required

movies_ns = Namespace('movies')


@movies_ns.route("/")
class MoviesView(Resource):
    @auth_required
    def get(self):
        year = request.args.get("year")
        director_id = request.args.get("director_id")
        genre_id = request.args.get("genre_id")

        if year:
            movies = movies_service.get_by_year(year)
        elif director_id:
            movies = movies_service.get_by_director(director_id)
        elif genre_id:
            movies = movies_service.get_by_genre(genre_id)
        else:
            movies = movies_service.get_all()

        result = MoviesSchema(many=True).dump(movies)

        return result, 200

    @admin_required
    def post(self):
        data = request.get_json()
        movie = movies_service.create(data)
        result = MoviesSchema().dump(movie)

        return result, 201


@movies_ns.route("/<int:mid>")
class MoviesView(Resource):
    @auth_required
    def get(self, mid):
        movie = movies_service.get_one(mid)
        result = MoviesSchema().dump(movie)
        return result, 200

    @admin_required
    def put(self, mid):
        data = request.get_json()
        movies_service.update(data, mid)
        return "", 204

    @admin_required
    def patch(self, mid):
        data = request.get_json()
        movies_service.update_partially(data, mid)
        return "", 204

    @admin_required
    def delete(self, mid):
        movies_service.delete(mid)
        return "", 204
