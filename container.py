from dao.genres import GenresDAO
from dao.directors import DirectorsDAO
from dao.movies import MoviesDAO
from dao.users import UsersDAO
from service.auth import AuthService
from service.genres import GenresService
from service.directors import DirectorsService
from service.movies import MoviesService
from service.users import UsersService
from setup_db import db

movies_dao = MoviesDAO(db.session)
directors_dao = DirectorsDAO(db.session)
genres_dao = GenresDAO(db.session)
user_dao = UsersDAO(db.session)

movies_service = MoviesService(movies_dao=movies_dao)
directors_service = DirectorsService(directors_dao=directors_dao)
genres_service = GenresService(genres_dao=genres_dao)
user_service = UsersService(user_dao=user_dao)
auth_service = AuthService(user_service=user_service)