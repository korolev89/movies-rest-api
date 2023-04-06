from dao.model.movies import Movies


class MoviesDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        movies = Movies.query.all()
        return movies

    def get_by_year(self, year):
        movies = Movies.query.filter(Movies.year == year).all()
        return movies

    def get_by_director(self, director_id):
        movies = Movies.query.filter(Movies.director_id == director_id)
        return movies

    def get_by_genre(self, genre_id):
        movies = Movies.query.filter(Movies.genre_id == genre_id)
        return movies

    def get_one(self, mid):
        movie = Movies.query.get(mid)
        return movie

    def create(self, data):
        movie = Movies(**data)
        self.session.add(movie)
        self.session.commit()
        self.session.close()

    def update(self, data):
        self.session.add(data)
        self.session.commit()
        self.session.close()

    def delete(self, movie):
        self.session.delete(movie)
        self.session.commit()
        self.session.close()
