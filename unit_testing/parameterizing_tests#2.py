import unittest

class EntertainmentSystemTests(unittest.TestCase):

  def test_movie_license(self):
    daily_movies = ['Scarlet', 'Johanson']
    licensed_movies = ['Johanson',]
    for movie in daily_movies:
      print(movie)
      with self.subTest(movie):
        self.assertIn(movie, licensed_movies)

# unittest.main()