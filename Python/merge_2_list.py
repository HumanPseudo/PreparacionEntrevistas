"""
    Algorithm to merge two sorted list
    example:
    input: [1,2,4,6] and [2,3,5]
    output: [1,2,2,3,4,5,6]
"""
from singleLinkedList import Node

class Merge2List:
    def merge(self, list1: Node, list2: Node) -> Node:
        """
        Merges two sorted linked lists.

        Args:
            list1: The first linked list.
            list2: The second linked list.

        Returns:
            The merged linked list.
        """
        dummy_head = Node(-1)
        current = dummy_head
        while list1 and list2:
            if list1.data < list2.data:
                current.next_node = list1
                list1 = list1.next_node
            else:
                current.next_node = list2
                list2 = list2.next_node
            current = current.next_node
        current.next_node = list1 or list2
        
        return dummy_head.next_node
    
    def appendTolist(self, current: Node, list_node: Node) -> None:
        while list_node:
            current.next_node = list_node
            list_node = list_node.next_node
            current = current.next_node