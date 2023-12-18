class Movie():
    def __init__(self, title: str, genres, year: int, runtime):
        # Calling the Staticmethods for input validation#
        self.validate_title(title)
        self.validate_year(year)
        self.validate_genre(genres)

        self.title = title
        self.genres = genres
        self.year = year
        self.runtime = runtime

    def __repr__(self):
        return repr(f'Title: {self.title}, year: {self.year}, genres: {self.genres} with runtime: {self.runtime}')

    # Static methods are functions on classes, not on instances, there is no self.variable#
    @staticmethod
    def validate_title(title):
        if not isinstance(title, str):
            raise ValueError('Title should be a string')

    @staticmethod
    def validate_genre(genres):
        if not isinstance(genres, list):
            raise ValueError('Genre should be a list')

    @staticmethod
    def validate_year(year):
        if not isinstance(year, int):
            raise ValueError('Year should be an integer')
