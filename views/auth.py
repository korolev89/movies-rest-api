from flask import request, jsonify
from flask_restx import Resource, Namespace

from container import auth_service

auth_ns = Namespace('auth')


@auth_ns.route("/")
class AuthView(Resource):
    def post(self):
        try:
            req_json = request.get_json()
            username = req_json.get("username", None)
            password = req_json.get("password", None)

            if None in [username, password]:
                return "", 400

            tokens = auth_service.generate_tokens(username, password)

            return tokens, 200

        except Exception as e:
            return str(e), 400

    def put(self):
        try:
            req_json = request.get_json()
            refresh_token = req_json["refresh_token"]
            tokens = auth_service.refresh_tokens(refresh_token)
            return tokens, 200
        except Exception as e:
            return str(e), 400
