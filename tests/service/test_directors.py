from unittest.mock import MagicMock

import pytest

from dao.directors import DirectorsDAO
from service.directors import DirectorsService


@pytest.fixture()
def directors_dao():
    directors_dao = DirectorsDAO(None)

    directors_dao.get_one = MagicMock()
    directors_dao.get_all = MagicMock()

    return directors_dao


class TestDirectorsService:
    @pytest.fixture(autouse=True)
    def directors_service(self, directors_dao):
        self.directors_service = DirectorsService(directors_dao=directors_dao)

    parameters = ((1, {'id': 1, 'name': 'John Smith'}), (2, {'id': 2, 'name': 'Alice Black'}),)

    @pytest.mark.parametrize('did, director', parameters)
    def test_get_one(self, did, director):
        self.directors_service.directors_dao.get_one.return_value = director
        assert self.directors_service.get_one(did) == director

    parameters = ([{'id': 1, 'name': 'John Smith'}, {'id': 2, 'name': 'Alice Black'}])

    @pytest.mark.parametrize('directors', parameters)
    def test_get_all(self, directors):
        self.directors_service.directors_dao.get_all.return_value = directors
        assert self.directors_service.get_all() == directors
