class Movie:
    # constructor funtion:
    def  __init__(self, name, genre):
        self.name = name
        self.genre = genre

    def __repr__(self):
        return "<Movie: {}, Genre: {}>".format(self.name, self.genre)
