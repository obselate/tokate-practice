import unittest
from even import is_even


class IsEvenTest(unittest.TestCase):
    def test_zero(self):
        self.assertTrue(is_even(0))

    def test_positive_even(self):
        self.assertTrue(is_even(4))

    def test_positive_odd(self):
        self.assertFalse(is_even(3))

    def test_negative_even(self):
        self.assertTrue(is_even(-4))

    def test_negative_odd(self):
        self.assertFalse(is_even(-3))


if __name__ == "__main__":
    unittest.main()
