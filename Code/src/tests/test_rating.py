import unittest
from src.User import User
from src.Movies import Movie
from src.Rating import Rating


class TestRatingClass(unittest.TestCase):
    def setUp(self):
        self.user = User('John')
        self.movie = Movie('Inception', ['Action', 'Sci-Fi'], 2010, 148)

    def test_valid_rating_instance(self):
        self.user.watch_movie(self.movie)
        rating = Rating(self.user, self.movie, 4.5, 'Great movie!')

        self.assertEqual(rating.user, self.user)
        self.assertEqual(rating.movie, self.movie)
        self.assertEqual(rating.score, 4.5)
        self.assertEqual(rating.review, 'Great movie!')

        # Check that the review is added to the movie's reviews
        self.assertEqual(self.movie.reviews[self.user.id], 'Great movie!')

        # Check that the review is added to the user's reviewed movies
        self.assertEqual(self.user.reviewed_movies[self.movie.title], 'Great movie!')

    def test_invalid_user_not_watched(self):
        # Create a movie but the user hasn't watched it
        with self.assertRaises(ValueError) as context:
            Rating(self.user, self.movie, 3.0, 'Good movie.')

        self.assertEqual(str(context.exception), f"User {self.user.username} did not watch movie {self.movie.title}")

    def test_invalid_user_type(self):
        # Passing an invalid user type
        with self.assertRaises(ValueError) as context:
            Rating('InvalidUser', self.movie, 2.0, 'Okay movie.')

        self.assertEqual(str(context.exception), 'User should be a User instance')

    def test_invalid_movie_type(self):
        # Passing an invalid movie type
        with self.assertRaises(ValueError) as context:
            Rating(self.user, 'InvalidMovie', 2.5, 'Enjoyable.')

        self.assertEqual(str(context.exception), 'Movie should be a movie instance')

    def test_invalid_score_out_of_range(self):
        # Trying to create a rating with an invalid score
        with self.assertRaises(ValueError) as context:
            Rating(self.user, self.movie, 6.0, 'Too high score.')

        self.assertEqual(str(context.exception), 'score should be a number between 1 and 5')

    def test_invalid_review_type(self):
        # Trying to create a rating with an invalid review type
        with self.assertRaises(ValueError) as context:
            Rating(self.user, self.movie, 3.5, 123)

        self.assertEqual(str(context.exception), 'review should be a string')


if __name__ == '__main__':
    unittest.main()
