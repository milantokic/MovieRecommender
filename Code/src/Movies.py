from src.database_config import setup_movie_table, create_connection

connection = create_connection()
cursor = connection.cursor()
setup_movie_table(connection)


class Movie:
    ALLOWED_GENRES = ['Game-Show',
                      'Drama',
                      'Sci-Fi',
                      'Action',
                      'Western',
                      'News',
                      'War',
                      'Talk-Show',
                      'Biography',
                      'Documentary',
                      'Reality-TV',
                      'Film-Noir',
                      'Adventure',
                      'Crime',
                      'Mystery',
                      'Sport',
                      'Family',
                      'Fantasy',
                      'Animation',
                      'Music',
                      'Comedy',
                      'Thriller',
                      'History',
                      'Romance',
                      'Musical',
                      'Adult',
                      'Horror']
    movie_counter = 0

    def __init__(self, title: str, genres: list, year: int, runtime):
        # Calling the Static-methods for input validation#
        self.validate_title(title)
        Movie.movie_counter += 1
        self.validate_year(year)
        self.validate_genre(genres)
        self.movie_id = Movie.movie_counter

        self.title = title
        self.genres = genres
        self.year = year
        self.runtime = runtime
        self.reviews = {}

        self.insert_to_db()

    def __repr__(self):
        return repr(
            f'ID: {self.movie_id} Title: {self.title}, year: {self.year}, genres: {self.genres} with runtime: {self.runtime}')

    def insert_to_db(self):
        cursor.execute("INSERT INTO movies (id, title, genres, year, runtime) VALUES (?, ?, ?, ?, ?)",
                       (self.movie_id, self.title, ','.join(self.genres), self.year, self.runtime))
        connection.commit()

    # Static methods are functions on classes, not on instances, there is no self.variable#
    @staticmethod
    def validate_title(title):
        if not isinstance(title, str):
            raise ValueError('Title should be a string')

    @staticmethod
    def validate_genre(genres):
        if not isinstance(genres, list):
            raise ValueError('Genre should be a list')
        if not all(genre in Movie.ALLOWED_GENRES for genre in genres):
            raise ValueError(f'Invalid genre. Allowed genres are: {Movie.ALLOWED_GENRES}')

    @staticmethod
    def validate_year(year):
        if not isinstance(year, int):
            raise ValueError('Year should be an integer')
