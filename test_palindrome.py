import unittest
from palindrome import is_palindrome


class PalindromeTest(unittest.TestCase):
    def test_mixed_case(self):
        self.assertTrue(is_palindrome("Racecar"))

    def test_spaces_and_punctuation(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))


if __name__ == "__main__":
    unittest.main()
