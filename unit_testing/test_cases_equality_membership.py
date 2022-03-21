"""
The full list for equality and membership

assertEqual(a, b) ------> a == b
assertNotEqual(a, b) ------> a != b
assertTrue(x) ------> bool(x) is True
assertFalse(x) ------> bool(x) is False
assertIs(a, b) ------> a is b
assertIsNot(a, b) ------> a is not b
assertIsNone(x) ------> x is None
assertIsNotNone(x) ------> x is not None
assertIn(a, b) ------> a in b
assertNotIn(a, b) ------> a not in b
assertIsInstance(a, b) ------> isinstance(a, b)
assertNotIsInstance(a, b) ------> not isinstance(a, b)
"""

import unittest
import entertainment


# Write your code below:
class EntertainmentSystemTests(unittest.TestCase):

    def test_movie_license(self):
        daily_movie = entertainment.get_daily_movie()
        licensed_movies = entertainment.get_licensed_movies()
        self.assertIn(daily_movie, licensed_movies, 'Movie is licensed')

    def test_wifi_status(self):
        wifi_enabled = entertainment.get_wifi_status()
        self.assertTrue(wifi_enabled, 'Wi-Fi is turned on')


unittest.main()
