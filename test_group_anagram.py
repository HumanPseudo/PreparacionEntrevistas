import unittest
from group_anagram import GroupAnagram

class TestGroupAnagram(unittest.TestCase):

    def test_group_anagrams(self):
        words = ["saco", "arresto", "programa", "rastreo", "caso"]
        expected_result = [["saco", "caso"], ["arresto", "rastreo"], ["programa"]]
        result = GroupAnagram.group_anagrams(words)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
