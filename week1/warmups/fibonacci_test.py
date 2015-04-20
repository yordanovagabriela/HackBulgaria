import unittest

from fibonacci import fibonacci


class TestFibonacci(unittest.TestCase):

    def test_fibonacci_seq(self):
        self.assertEqual(fibonacci(10), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
        self.assertEqual(fibonacci(1), [1])
        self.assertEqual(fibonacci(0), [])


if __name__ == '__main__':
    unittest.main()
