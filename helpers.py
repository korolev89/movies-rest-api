import jwt
from flask import request, abort

from config import Config


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]

        try:
            jwt.decode(token, Config().SECRET_KEY, algorithms=Config().ALGORITHM)
        except Exception:
            abort(401)

        return func(*args, **kwargs)

    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]

        try:
            user = jwt.decode(token, Config().SECRET_KEY, algorithms=Config().ALGORITHM)
            role = user.get("role")
            if role != "admin":
                abort(400)
        except Exception:
            abort(401)

        return func(*args, **kwargs)

    return wrapper
