import unittest
from greet import greet


class GreetTest(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")

    def test_empty_name(self):
        self.assertEqual(greet(""), "Hello, stranger!")

    def test_whitespace_name(self):
        self.assertEqual(greet("   "), "Hello, stranger!")

    def test_padded_name(self):
        self.assertEqual(greet("  Ada "), "Hello, Ada!")


if __name__ == "__main__":
    unittest.main()
