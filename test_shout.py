import unittest
from shout import shout


class ShoutTest(unittest.TestCase):
    def test_shout(self):
        self.assertEqual(shout("hi"), "HI!")

    def test_shout_with_exclamation(self):
        self.assertEqual(shout("hi!"), "HI!")


if __name__ == "__main__":
    unittest.main()
