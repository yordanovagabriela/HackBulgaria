import unittest


import is_prime


class TestPandaNetwork(unittest.TestCase):

    def test_negative_numbers(self):
        self.assertTrue(is_prime(-5))

    def test_positive_numbers(self):
        self.assertTrue(is_prime(5))

if __name__ == '__main':
    unittest.main()
