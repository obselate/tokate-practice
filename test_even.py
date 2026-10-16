import unittest
from even import is_even


class IsEvenTest(unittest.TestCase):
    def test_zero(self):
        self.assertTrue(is_even(0))

    def test_positive_even_integer(self):
        self.assertTrue(is_even(8))

    def test_positive_odd_integer(self):
        self.assertFalse(is_even(7))

    def test_negative_integer(self):
        self.assertTrue(is_even(-4))


if __name__ == "__main__":
    unittest.main()
