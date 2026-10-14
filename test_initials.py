import unittest
from initials import initials


class InitialsTest(unittest.TestCase):
    def test_full_name(self):
        self.assertEqual(initials("Ada Lovelace"), "AL")

    def test_padded_lowercase_name(self):
        self.assertEqual(initials("  alan   turing "), "AT")

    def test_empty_name(self):
        self.assertEqual(initials(""), "")

    def test_whitespace_only(self):
        self.assertEqual(initials(" \t\n\r "), "")

    def test_mixed_whitespace(self):
        self.assertEqual(initials("ada\tlovelace\nbyron\rking"), "ALBK")


if __name__ == "__main__":
    unittest.main()
