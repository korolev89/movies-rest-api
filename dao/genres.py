from dao.model.genres import Genres


class GenresDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        genres = Genres.query.all()
        return genres

    def get_one(self, gid):
        genres = Genres.query.get(gid)
        return genres
