class Movie:
    # constructor funtion:
    def  __init__(self, name, genre, watched):
        self.name = name
        self.genre = genre
        self.watched = watched

    def __repr__(self):
        return "<Movie: {}, Genre: {}>".format(self.name, self.genre)

    def json(self):
        return {
            'name': self.name,
            'genre': self.genre,
            'watched': self.watched
        }