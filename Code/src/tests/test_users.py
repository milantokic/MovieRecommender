import unittest
from src.User import User
from src.Movies import Movie


class TestUserClass(unittest.TestCase):
    def test_valid_user_instance(self):
        username = 'Username1'

        user = User(username)

        self.assertEqual(user.username, username)

    def test_invalid_username(self):
        with self.assertRaises(ValueError):
            User(1234)

    def test_watch_movie(self):
        user = User('Milan')
        movie = Movie('The Movie', ['Action'], 2022, 120)
        user.watch_movie(movie)

        self.assertIn(movie, user.watched_movies)

    def test_duplicate_watched_movie(self):
        user = User('Milan')
        movie1 = Movie('The Movie', ['Action'], 2022, 120)
        user.watch_movie(movie1)
        user.watch_movie(movie1)

        self.assertEqual(len(user.watched_movies),1)

    def test_id_counter(self):
        user1 = User('Milan')
        user2 = User('Milan2')

        self.assertEqual(user1.user_ID, 1)
        self.assertEqual(user2.user_ID, 2)


if __name__ == '__main__':
    unittest.main()
