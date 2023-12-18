import unittest
from src.Movies import Movie


class TestMovieClass(unittest.TestCase):
    def test_valid_movie_instance(self):
        title = 'The Movie'
        genres = ["Action", "Adventure"]
        year = 2022
        runtime = 120

        movie = Movie(title, genres, year, runtime)

        self.assertEqual(movie.title, title)
        self.assertEqual(movie.genres, genres)
        self.assertEqual(movie.year, year)
        self.assertEqual(movie.runtime, runtime)

    def test_invalid_title(self):
        # Test creating a Movie instance with an invalid title
        with self.assertRaises(ValueError):
            Movie(123, ["Action", "Adventure"], 2022, 120)

    def test_invalid_genres(self):
        # Test creating a Movie instance with invalid genres
        with self.assertRaises(ValueError):
            Movie("The Movie", "Action", 2022, 120)

    def test_not_allowed_genre(self):
        with self.assertRaises(ValueError):
            Movie("The Movie", ['Fun', 'Party'], 2022, 120)

    def test_invalid_year(self):
        # Test creating a Movie instance with an invalid year
        with self.assertRaises(ValueError):
            Movie("The Movie", ["Action", "Adventure"], "2022", 120)


if __name__ == '__main__':
    unittest.main()
