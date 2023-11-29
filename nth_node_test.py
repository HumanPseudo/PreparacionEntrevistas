import unittest
from singleLinkedList import Node
from nth_node_to_last import nhNode  # Replace 'your_file_name' with the actual filename

class TestNhNode(unittest.TestCase):
    def setUp(self):
        # Create a sample linked list: 1 -> 2 -> 4 -> 6
        self.head = Node(1)
        self.head.next_node = Node(2)
        self.head.next_node.next_node = Node(4)
        self.head.next_node.next_node.next_node = Node(6)

        # Create an instance of nhNode
        self.nh_instance = nhNode()

    def test_nth_node_from_end(self):
        # Test with N = 2
        n = 2
        result_node = self.nh_instance.find_nth_node_from_end(self.head, n)
        self.assertEqual(result_node.data, 4)

    def test_nth_node_from_end_invalid(self):
        # Test with invalid N
        n = 5
        result_node = self.nh_instance.find_nth_node_from_end(self.head, n)
        self.assertIsNone(result_node)

if __name__ == '__main__':
    unittest.main()
