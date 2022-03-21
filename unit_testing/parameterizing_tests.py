import unittest


def times_ten(number):
    return number * 100


class TestTimesTen(unittest.TestCase):
    def test_times_ten(self):
        for num in [0, 1000000, -10]:
            with self.subTest():
                expected_result = num * 100
                message = 'Expected times_ten(' + str(
                    num) + ') to return ' + str(expected_result)
                self.assertEqual(times_ten(num), expected_result, message)
                print(num)


# unittest.main()
