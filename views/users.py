from flask import request
from flask_restx import Resource, Namespace
from container import user_service
from dao.model.users import UsersSchema

users_ns = Namespace('users')


@users_ns.route("/")
class GenresView(Resource):
    def post(self):
        data = request.get_json()
        user_service.create_user(data)

        return "", 204

