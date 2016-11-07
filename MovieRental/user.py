from movie import Movie

class User:
    def __init__(self, name):
        self.name = name
        self.movies = []


    # definies a string that gets printed when object is instantiated
    def __repr__(self):
        return "<User {}>".format(self.name)

    def add_movie(self, name, genre): #my_user_object.add_movie(name, genre)
        movie = Movie(name, genre, False)
        self.movies.append(movie)

    def delete_movie(self, name):
        #re-defining self.movies with movies that != to movie.name
        self.movies = list(filter(lambda movie: movie.name != name, self.movies))


    # get list of movies that have been watched
    def watched_movies(self):
        return list(filter(lambda movie: movie.watched, self.movies))
        #lambda function take place of code below:
        #watched_movies = []
        #for movie in self.movies:
           # if movie.watched:
               # watched_movies.append(movie)

    def json(self):
        return {
            'name': self.name,
            'movies': [
                movie.json() for movie in self.movies
            ]

        }


