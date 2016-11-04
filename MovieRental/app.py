#from movie.py and user.py import the classes
from movie import Movie
from user import User

#creating a new user
user = User("Tyler")

user.add_movie("The Matrix", "Sci-Fi")
user.add_movie("The Interview", "Comedy")

user.save_to_file()