class User:
    def __init__(self, name):
        self.name = name
        self.movies = []


    # definies a string that gets printed when object is instantiated
    def __repr__(self):
        return "<User {}>".format(self.name)


    # get list of movies that have been watched
    def watched_movies(self):
        return list(filter(lambda movie: movie.watched, self.movies))

        #lambda function take place of code below:
        #watched_movies = []
        #for movie in self.movies:
           # if movie.watched:
               # watched_movies.append(movie)
