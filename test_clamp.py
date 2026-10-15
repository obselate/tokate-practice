import unittest
from clamp import clamp


class ClampTest(unittest.TestCase):
    def test_value_in_range(self):
        self.assertEqual(clamp(5, 0, 10), 5)

    def test_value_below_range(self):
        self.assertEqual(clamp(-3, 0, 10), 0)

    def test_value_above_range(self):
        self.assertEqual(clamp(42, 0, 10), 10)

    def test_lower_bound(self):
        self.assertEqual(clamp(0, 0, 10), 0)

    def test_upper_bound(self):
        self.assertEqual(clamp(10, 0, 10), 10)


if __name__ == "__main__":
    unittest.main()
