from src.database_config import create_connection, setup_user_table, setup_user_watched_table
from src.Movies import Movie

connection = create_connection()
cursor = connection.cursor()
setup_user_table(connection)
setup_user_watched_table(connection)


class User:
    user_counter = 0

    def __repr__(self):
        return repr(f"Id: {self.id} Username: {self.username}")

    def __init__(self, username):
        self.validate_username(username)
        User.user_counter += 1
        self.id = User.user_counter
        self.username = username
        self.watched_movies = []
        self.reviewed_movies = {}

        self.insert_to_db()

    def watch_movie(self, movie: Movie):
        if not isinstance(movie, Movie):
            raise ValueError('Input must be instance of type Movie')
        if movie not in self.watched_movies:
            self.watched_movies.append(movie)
            self.insert_watched_dv(movie)
        else:
            pass

    def insert_to_db(self):
        cursor.execute("INSERT INTO user (id, username) VALUES (?, ?)", (self.id, self.username,))
        connection.commit()

    def insert_watched_dv(self, movie: Movie):
        cursor.execute("INSERT INTO user_watched (user_id, movie_id) VALUES (?, ?)", (self.id, movie.movie_id))
        connection.commit()

    @staticmethod
    def validate_username(username):
        if not isinstance(username, str):
            raise ValueError('Username should be a string')
