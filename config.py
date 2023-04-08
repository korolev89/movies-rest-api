class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///C:\\Anton\\Projects\\education\\movies-rest-api\\movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'bestSecret'
    PWD_HASH_SALT = b'helloWorld'
    PWD_HASH_ITERATIONS = 100_000
    ALGORITHM = 'HS256'
