import unittest


from factorial_digit import factorial_digits


class TestFactorialDigits(unittest.TestCase):

    def test_factorial_digits(self):
        self.assertEqual(factorial_digits(13), 7)
        self.assertEqual(factorial_digits(14), 25)

    def test_negative(self):
        self.assertEqual(factorial_digits(-13), 7)
        self.assertEqual(factorial_digits(-14), 25)

if __name__ == '__main__':
    unittest.main()
