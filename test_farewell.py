import unittest
from farewell import farewell


class FarewellTest(unittest.TestCase):
    def test_farewell(self):
        self.assertEqual(farewell("Ada"), "Goodbye, Ada!")


if __name__ == "__main__":
    unittest.main()
