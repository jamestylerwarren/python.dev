class User:
    def __init__(self, name):
        self.name = name
        self.movies = []


    # definies a string that gets printed when object is instantiated
    def __repr__(self):
        return "<User {}>".format(self.name)