#from movie.py and user.py import the classes
from movie import Movie
from user import User

user = User.load_from_file('Tyler.txt')

print(user.name)

print(user.movies)