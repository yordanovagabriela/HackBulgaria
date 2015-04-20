import unittest


from sum_all_digits_of_a_number import sum_of_digits


class TestSumDigits(unittest.TestCase):

    def test_negative_number(self):
        self.assertEqual(sum_of_digits(-111), 3)
        self.assertEqual(sum_of_digits(-99), 18)

    def test_positive_number(self):
        self.assertEqual(sum_of_digits(111), 3)
        self.assertEqual(sum_of_digits(99), 18)

    def test_zero(self):
        self.assertEqual(sum_of_digits(0), 0)

if __name__ == '__main__':
    unittest.main()
