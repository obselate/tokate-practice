import unittest
from midpoint import midpoint


class MidpointTest(unittest.TestCase):
    def test_equal_inputs(self):
        self.assertEqual(midpoint(3, 3), 3)

    def test_positive_inputs(self):
        self.assertEqual(midpoint(2, 4), 3)

    def test_negative_inputs(self):
        self.assertEqual(midpoint(-2, 4), 1)


if __name__ == "__main__":
    unittest.main()
