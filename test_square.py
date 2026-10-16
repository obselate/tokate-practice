import unittest
from square import square


class SquareTest(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(square(0), 0)

    def test_positive_integer(self):
        self.assertEqual(square(4), 16)

    def test_negative_integer(self):
        self.assertEqual(square(-3), 9)

    def test_fraction(self):
        self.assertEqual(square(0.5), 0.25)


if __name__ == "__main__":
    unittest.main()
