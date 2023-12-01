import unittest
from singleLinkedList import Node
from merge_2_list import Merge2List

class Merge2ListTest(unittest.TestCase):

    def test_merge(self):
        # Create the first linked list: 1 -> 3 -> 5
        list1 = Node(1)
        list1.next_node = Node(3)
        list1.next_node.next_node = Node(5)

        # Create the second linked list: 2 -> 4 -> 6
        list2 = Node(2)
        list2.next_node = Node(4)
        list2.next_node.next_node = Node(6)

        # Create an instance of Merge2List
        merger = Merge2List()

        # Merge the two linked lists
        merged_list = merger.merge(list1, list2)

        # Assert the values of the merged linked list
        self.assertEqual(merged_list.data, 1)
        self.assertEqual(merged_list.next_node.data, 2)
        self.assertEqual(merged_list.next_node.next_node.data, 3)
        self.assertEqual(merged_list.next_node.next_node.next_node.data, 4)
        self.assertEqual(merged_list.next_node.next_node.next_node.next_node.data, 5)
        self.assertEqual(merged_list.next_node.next_node.next_node.next_node.next_node.data, 6)
        self.assertIsNone(merged_list.next_node.next_node.next_node.next_node.next_node.next_node)

if __name__ == '__main__':
    unittest.main()