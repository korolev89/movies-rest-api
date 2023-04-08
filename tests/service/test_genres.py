from unittest.mock import MagicMock

import pytest

from dao.genres import GenresDAO
from service.genres import GenresService


@pytest.fixture()
def genres_dao():
    genres_dao = GenresDAO(None)

    genres_dao.get_one = MagicMock()
    genres_dao.get_all = MagicMock()

    return genres_dao


class TestGenresService:
    @pytest.fixture(autouse=True)
    def genres_service(self, genres_dao):
        self.genres_service = GenresService(genres_dao=genres_dao)

    parameters = ((1, {'id': 1, 'name': 'Drama'}), (2, {'id': 2, 'name': 'Fantasy'}),)

    @pytest.mark.parametrize('gid, genre', parameters)
    def test_get_one(self, gid, genre):
        self.genres_service.genres_dao.get_one.return_value = genre
        assert self.genres_service.get_one(gid) == genre

    parameters = ([{'id': 1, 'name': 'Drama'}, {'id': 2, 'name': 'Fantasy'}])

    @pytest.mark.parametrize('genres', parameters)
    def test_get_all(self, genres):
        self.genres_service.genres_dao.get_all.return_value = genres
        assert self.genres_service.get_all() == genres
