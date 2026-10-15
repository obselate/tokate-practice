import unittest
from titlecase import title_case


class TitleCaseTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(title_case("hello world"), "Hello World")

    def test_padded_and_mixed_case(self):
        self.assertEqual(title_case("  hELLO   wORLD "), "Hello World")

    def test_empty(self):
        self.assertEqual(title_case(""), "")


if __name__ == "__main__":
    unittest.main()
