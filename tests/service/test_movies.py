from unittest.mock import MagicMock

import pytest

from dao.movies import MoviesDAO
from service.movies import MoviesService


@pytest.fixture()
def movies_dao():
    movies_dao = MoviesDAO(None)

    movies_dao.get_one = MagicMock()
    movies_dao.get_all = MagicMock()
    movies_dao.create = MagicMock()
    movies_dao.update = MagicMock()
    movies_dao.delete = MagicMock()

    return movies_dao


class TestMoviesService:
    @pytest.fixture(autouse=True)
    def movies_service(self, movies_dao):
        self.movies_service = MoviesService(movies_dao=movies_dao)

    parameters = ((1, {'id': 1, 'title': 'Movie1'}), (2, {'id': 2, 'title': ''}),)

    @pytest.mark.parametrize('mid, movie', parameters)
    def test_get_one(self, mid, movie):
        self.movies_service.movies_dao.get_one.return_value = movie

        assert self.movies_service.get_one(mid) == movie

    parameters = ([({'id': 1, 'title': 'Movie1'}), ({'id': 2, 'title': ''})])

    @pytest.mark.parametrize('movies', parameters)
    def test_get_all(self, movies):
        self.movies_service.movies_dao.get_all.return_value = movies

        assert len(self.movies_service.get_all()) == 2
        assert self.movies_service.get_all() == movies

    parameters = (
        (
            {
                "title": "Movie_1",
                "description": "Movie_1 description",
                "trailer": "",
                "year": 2023,
                "rating": 8.0,
                "genre_id": 1,
                "director_id": 1
             }
        ),
        (
            {
            "title": ""
            }
        ),
    )

    @pytest.mark.parametrize('movie', parameters)
    def test_create(self, movie):
        self.movies_service.movies_dao.create.return_value = movie

        assert self.movies_service.create(movie) == movie

    parameters = (({'id': 1, 'title': 'Movie1'}, {'id': 1, 'title': 'Movie123'}),)

    @pytest.mark.parametrize('movie_orig, movie_new', parameters)
    def test_update(self, movie_orig, movie_new):
        self.movies_service.movies_dao.update.return_value = movie_new

        assert self.movies_service.update_partially(movie_new, 1) == movie_new

    def test_delete(self):
        self.movies_service.delete(1)
        self.movies_service.movies_dao.delete.assert_called_once_with(1)
