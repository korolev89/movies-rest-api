class MoviesService:
    def __init__(self, movies_dao):
        self.movies_dao = movies_dao

    def get_all(self):
        return self.movies_dao.get_all()

    def get_by_year(self, year):
        return self.movies_dao.get_by_year(year)

    def get_by_director(self, director_id):
        return self.movies_dao.get_by_director(director_id)

    def get_by_genre(self, genre_id):
        return self.movies_dao.get_by_genre(genre_id)

    def get_one(self, mid):
        return self.movies_dao.get_one(mid)

    def create(self, data):
        return self.movies_dao.create(data)

    def update(self, data, mid):
        movie = self.movies_dao.get_one(mid)

        movie.title = data["title"]
        movie.description = data["description"]
        movie.trailer = data["trailer"]
        movie.year = data["year"]
        movie.rating = data["rating"]

        self.movies_dao.update(movie)

    def update_partially(self, data, mid):
        movie = self.movies_dao.get_one(mid)

        if "title" in data:
            movie.title = data["title"]
        if "description" in data:
            movie.description = data["description"]
        if "trailer" in data:
            movie.trailer = data["trailer"]
        if "year" in data:
            movie.year = data["year"]
        if "rating" in data:
            movie.rating = data["rating"]

        self.movies_dao.update(movie)

    def delete(self, mid):
        movie = self.movies_dao.get_one(mid)
        return self.movies_dao.delete(movie)