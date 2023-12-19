from src.Movies import Movie
from src.User import User
from src.Rating import Rating


mov1 = Movie(title='title', genres=['Horror'], year=1994, runtime=99)
mov2 = Movie(title='titlee2', genres=['Horror'], year=1994, runtime=99)

us1 = User(username='mttoka')
#us1.watch_movie(mov1)
us2 = User(username='testusr')
us1.watch_movie(mov2)
rate = Rating(user=us1, movie=mov2, score=2.5, review='Not bad')
print(mov1)

