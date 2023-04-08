import calendar
import datetime

import jwt
from config import Config


class AuthService:
    def __init__(self, user_service):
        self.user_service = user_service

    def generate_tokens(self, username, password, is_refresh = False):
        user = self.user_service.get_user_by_username(username)

        if not user:
            raise Exception("Incorrect username or password")

        if not is_refresh:
            if not self.user_service.compare_passwords(user.password, password):
                raise Exception("Incorrect username or password")

        data = {
            'username': user.username,
            'role': user.role
        }

        days30 = datetime.datetime.utcnow() + datetime.timedelta(days=30)
        data["exp"] = calendar.timegm(days30.timetuple())
        access_token = jwt.encode(data, Config().SECRET_KEY, algorithm=Config().ALGORITHM)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, Config().SECRET_KEY, algorithm=Config().ALGORITHM)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }

    def refresh_tokens(self, refresh_token):
        try:
            user = jwt.decode(refresh_token, Config().SECRET_KEY, algorithms=Config().ALGORITHM)
            username = user['username']

            user = self.user_service.get_user_by_username(username)

            if not user:
                raise Exception()

            return self.generate_tokens(username, user.password, is_refresh=True)
        except Exception as e:
            raise e
