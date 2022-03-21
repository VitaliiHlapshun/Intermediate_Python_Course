"""
Quantitative methods

assertAlmostEqual(a, b) ------> round(a-b, 7) == 0
assertNotAlmostEqual(a, b) ------> round(a-b, 7) != 0
assertGreater(a, b) ------> a > b
assertGreaterEqual(a, b) ------> a >= b
assertLess(a, b) ------> a < b
assertLessEqual(a, b) ------> a <= b
assertRegex(s, r) ------> r.search(s)
assertNotRegex(s, r) ------> not r.search(s)
assertCountEqual(a, b) ------> a and b have the same elements in the same
number, regardless of their order.
"""


import unittest
import entertainment


class EntertainmentSystemTests(unittest.TestCase):

    def test_movie_license(self):
        daily_movie = entertainment.get_daily_movie()
        licensed_movies = entertainment.get_licensed_movies()
        self.assertIn(daily_movie, licensed_movies)

    def test_wifi_status(self):
        wifi_enabled = entertainment.get_wifi_status()
        self.assertTrue(wifi_enabled)

    # Write your code below:
    def test_maximum_display_brightness(self):
        brightness = entertainment.get_maximum_display_brightness()
        self.assertAlmostEqual(brightness, 400)

    def test_device_temperature(self):
        device_temp = entertainment.get_device_temp()
        self.assertGreater(device_temp, 35)


unittest.main()
