from dao.model.directors import Directors


class DirectorsDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        directors = Directors.query.all()
        return directors

    def get_one(self, did):
        directors = Directors.query.get(did)
        return directors
