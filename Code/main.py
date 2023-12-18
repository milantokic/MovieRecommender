from src.Movies import Movie
from src.User import User


try:
    mov1 = Movie(title = 'titlee', genres=['horror'], year=1994, runtime=99)
except ValueError as e:
    print(f"Error: {e}")
else:
    print(mov1)

us1 = User(username='mttoka')
us2 = User(username='test')
print(us1)
us2.watch_movie(mov1)
us2.watch_movie(mov1)
us2.watch_movie(mov1)
