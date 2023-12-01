import unittest
from isUnique import IsUnique

class TestIsUnique(unittest.TestCase):

    def test_unique_string(self):
        unique_checker = IsUnique("abcde")
        self.assertTrue(unique_checker.is_unique())

    def test_non_unique_string(self):
        non_unique_checker = IsUnique("abcded")
        self.assertFalse(non_unique_checker.is_unique())

if __name__ == '__main__':
    unittest.main()
