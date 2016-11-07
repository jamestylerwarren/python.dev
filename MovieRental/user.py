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

    def save_to_file(self):
        with open("{}.txt".format(self.name), 'w') as f:
            f.write(self.name + "\n")
            for movie in self.movies:
                f.write("{},{},{}\n".format(movie.name, movie.genre, str(movie.watched)))

    @classmethod
    def load_from_file(cls, filename): #cls runs on class itself, not the object
        with open(filename, "r") as f:
            content = f.readlines()
            username = content[0]
            movies = []
            for line in content[1:]: #starts iterating on element 1 (not 0, which is username) and finishes at the end
                movie_data = line.split(",") #['name', 'genre', 'watched']
                movies.append(Movie(movie_data[0], movie_data[1], movie_data[2] == "True"))
            user = cls(username) #change User to cls
            user.movies = movies
            return user