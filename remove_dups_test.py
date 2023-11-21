import unittest
from singleLinkedList import Node, LinkedList
from remove_dups import RemoveDuplicates

class RemoveDuplicatesTest(unittest.TestCase):
    def test_remove_duplicates(self):
        # Create a linked list with duplicates
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)
        linked_list.append(1)

        # Create an instance of RemoveDuplicates
        remover = RemoveDuplicates(linked_list.head)

        # Display the original linked list
        print("Original Linked List:")
        linked_list.display()

        # Remove duplicates
        remover.remove_duplicates()

        # Display the linked list after removing duplicates
        print("\nLinked List after Removing Duplicates:")
        linked_list.display()

        # Assert the expected values after removing duplicates
        self.assertEqual(1, linked_list.head.data)
        self.assertEqual(2, linked_list.head.next_node.data)
        self.assertEqual(3, linked_list.head.next_node.next_node.data)
        self.assertEqual(4, linked_list.head.next_node.next_node.next_node.data)
        self.assertIsNone(linked_list.head.next_node.next_node.next_node.next_node)

if __name__ == '__main__':
    unittest.main()
