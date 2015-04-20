import unittest


from sum_of_divisors import sum_of_divisors


class TestSumOfDivisors(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(sum_of_divisors(8), 15)
        self.assertEqual(sum_of_divisors(1000), 2340)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_divisors(-8), 15)
        self.assertEqual(sum_of_divisors(-1000), 2340)

if __name__ == '__main__':
    unittest.main()
