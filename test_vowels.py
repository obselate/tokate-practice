import unittest
from vowels import count_vowels


class CountVowelsTest(unittest.TestCase):
    def test_name(self):
        self.assertEqual(count_vowels("Ada Lovelace"), 6)

    def test_empty_text(self):
        self.assertEqual(count_vowels(""), 0)

    def test_no_vowels(self):
        self.assertEqual(count_vowels("rhythm"), 0)

    def test_mixed_case(self):
        self.assertEqual(count_vowels("AEIOU aeiou"), 10)


if __name__ == "__main__":
    unittest.main()
