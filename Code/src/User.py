from src.Movies import Movie
class User:
    user_counter = 0

    def __repr__(self):
        return repr(f"{self.user_ID}  Username: {self.username}")

    def __init__(self, username):
        self.validate_username(username)
        User.user_counter += 1
        self.username=username
        self.user_ID = User.user_counter
        self.watched_movies = []

    def watch_movie(self, movie:Movie):
        if not isinstance(movie, Movie):
            raise ValueError('Input must be instance of type Movie')
        if movie not in self.watched_movies:
            self.watched_movies.append(movie)
        else:
            pass

    @staticmethod
    def validate_username(username):
        if not isinstance(username, str):
            raise ValueError('Username should be a string')




