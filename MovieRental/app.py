#from movie.py and user.py import the classes
from movie import Movie
from user import User
import json

user = User('Tyler')

user.add_movie("The Matrix", "Sci-Fi")
user.add_movie("The Interview", "Comedy")

print(user.json())

with open('my_file.txt', 'w') as f:
    json.dump(user.json(), f)
