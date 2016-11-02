#from movie.py and user.py import the classes
from movie import Movie
from user import User

#creating a new user
user = User("Tyler")

#declare a new Movie and pass needed parameters
my_movie = Movie("The Matrix", "Sci-Fi")

#add my_movie defined above to a user we defined above
user.movies.append(my_movie)

print(user)
print(user.movies)