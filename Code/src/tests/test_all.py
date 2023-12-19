import unittest
from src.tests.test_rating import TestRatingClass
from src.tests.test_movies import TestMovieClass
from src.tests.test_users import TestUserClass

if __name__ == '__main__':
    test_suite = unittest.TestSuite()

    test_suite.addTest(unittest.makeSuite(TestMovieClass))
    test_suite.addTest(unittest.makeSuite(TestUserClass))
    test_suite.addTest(unittest.makeSuite(TestRatingClass))

    unittest.TextTestRunner(verbosity=2).run(test_suite)