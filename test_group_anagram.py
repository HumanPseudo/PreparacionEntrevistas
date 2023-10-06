import unittest
from group_anagram import GroupAnagram

class TestGroupAnagram(unittest.TestCase):

    def test_build_anagram_map(self):
        # Test to verify the function build_anagram_map
        words = ["saco", "arresto", "programa", "rastreo", "caso"]
        expected_result = {
            str([1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]): ['saco', 'caso'],
            str([1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]): ['arresto', 'rastreo'],
            str([1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]): ['programa']
        }
        result = GroupAnagram.build_anagram_map(words)
        self.assertEqual(result, expected_result)

    def test_get_anagram_hash(self):
        # Test to verify the function get_anagram_hash
        word = "saco"
        expected_hash = str([1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0])
        result_hash = GroupAnagram.get_anagram_hash(word)
        self.assertEqual(result_hash, expected_hash)

if __name__ == '__main__':
    unittest.main()
