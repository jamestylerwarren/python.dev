#from movie.py and user.py import the classes
from movie import Movie
from user import User
import json



with open('my_file.txt', 'r') as f:
    json_data = json.load(f)
    user = User.from_json(json_data)
    print(user.json())