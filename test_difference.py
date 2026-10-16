import unittest

from difference import difference


class DifferenceTests(unittest.TestCase):
    def test_equal_inputs(self):
        self.assertEqual(difference(4, 4), 0)

    def test_positive_inputs(self):
        self.assertEqual(difference(2, 5), 3)

    def test_negative_inputs(self):
        self.assertEqual(difference(-2, 3), 5)
        self.assertEqual(difference(-5, -2), 3)


if __name__ == "__main__":
    unittest.main()
