import base64
import hashlib
import hmac
from config import Config

class UsersService:
    def __init__(self, user_dao):
        self.user_dao = user_dao

    def get_user_by_username(self, username):
        return self.user_dao.get_user_by_username(username)

    def create_user(self, user):
        user["password"] = self.get_hash(user["password"])
        return self.user_dao.create_user(user)

    def get_hash(self, password):
        return base64.b64encode(hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            Config().PWD_HASH_SALT,
            Config().PWD_HASH_ITERATIONS
        ))

    def compare_passwords(self, password_hash, password):
        return hmac.compare_digest(
            base64.b64decode(password_hash),
            hashlib.pbkdf2_hmac(
                "sha256",
                password.encode(),
                Config().PWD_HASH_SALT,
                Config().PWD_HASH_ITERATIONS
            )
        )
