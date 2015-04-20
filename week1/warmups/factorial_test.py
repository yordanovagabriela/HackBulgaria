import unittest

from fact import fact


class TestFactorial(unittest.TestCase):

    def test_negative(self):
        with self.assertRaises(ValueError):
            fact(-5)

    def test_positive(self):
        self.assertEqual(fact(5), 120)

    def test_zero(self):
        self.assertEqual(fact(0), 1)

if __name__ == '__main__':
    unittest.main()
