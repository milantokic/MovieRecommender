from src.Movies import Movie
from src.User import User


class Rating:

    def __str__(self):
        return f"User {self.user.username} gave the title {self.movie.title} a score of {self.score}\nReview: '{self.review}'"

    def __init__(self, user: User, movie: Movie, score: float, review: str):
        self.validate_user(user)
        self.validate_movie(movie)
        self.validate_score(score)
        self.validate_review(review)
        self.validate_user_watched(user, movie)

        self.user = user
        self.movie = movie
        self.score = score
        self.review = review
        self.movie.reviews[self.user.user_ID] = self.review
        self.user.reviewed_movies[self.movie.title] = self.review

    @staticmethod
    def validate_user(user):
        if not isinstance(user, User):
            raise ValueError('User should be a User instance')

    @staticmethod
    def validate_movie(movie):
        if not isinstance(movie, Movie):
            raise ValueError('Movie should be a movie instance')

    @staticmethod
    def validate_score(score):
        if not isinstance(score, (int, float)) or score < 1.0 or score > 5.0:
            raise ValueError('score should be a number between 1 and 5')

    @staticmethod
    def validate_review(review):
        if not isinstance(review, str):
            raise ValueError('review should be a string')

    def validate_user_watched(self, user, movie):
        if not (movie in user.watched_movies):
            raise ValueError(f"User {user.username} did not watch movie {movie.title}")
