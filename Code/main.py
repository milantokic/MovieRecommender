from src.Movies import Movie
from src.User import User
from src.Rating import Rating


mov1 = Movie(title='title', genres=['Horror'], year=1994, runtime=99)
mov2 = Movie(title='titlee2', genres=['Horror'], year=1994, runtime=99)

us1 = User(username='mttoka')
#us1.watch_movie(mov1)
us2 = User(username='testusr')
us1.watch_movie(mov2)

rev1 = Rating(user=us1, movie=mov1, score=3.5, review='Not bad movie')
rev2 = Rating(user=us1, movie=mov2, score=3.5, review='bad movie')
Rating(us1, mov1, 2.0, 'Okay movie.')
print(us1.reviewed_movies)
