import unittest
from count import count_words


class CountWordsTest(unittest.TestCase):
    def test_empty_text(self):
        self.assertEqual(count_words(""), 0)

    def test_padded_text(self):
        self.assertEqual(count_words(" a  b "), 2)

    def test_whitespace_only(self):
        self.assertEqual(count_words(" \t\n\r "), 0)

    def test_mixed_whitespace(self):
        self.assertEqual(count_words("one\ttwo\nthree\rfour"), 4)


if __name__ == "__main__":
    unittest.main()
