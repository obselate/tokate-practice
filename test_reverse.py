import unittest
from reverse import reverse_text


class ReverseTextTest(unittest.TestCase):
    def test_reverse_text(self):
        self.assertEqual(reverse_text("Ada"), "adA")

    def test_empty_text(self):
        self.assertEqual(reverse_text(""), "")


if __name__ == "__main__":
    unittest.main()
