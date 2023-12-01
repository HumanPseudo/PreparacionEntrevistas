from singleLinkedList import Node  # Assuming you have a Node class defined
from add_two_numbers import AddTwoNumbers  # Assuming you saved the previous code in addTwoNumbers.py

# Helper function to convert a linked list to a Python list
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.data)
        node = node.next_node
    return result

# Helper function to create a linked list from a list
def create_linked_list(lst):
    dummy = Node(-1)
    current = dummy
    for val in lst:
        current.next_node = Node(val)
        current = current.next_node
    return dummy.next_node

# Test data
list1 = create_linked_list([2, 4, 3])
list2 = create_linked_list([5, 6, 4])

# Instantiate AddTwoNumbers class
add_two_numbers_instance = AddTwoNumbers(list1, list2)

# Print the intermediate results
print("List 1:", linked_list_to_list(list1))
print("List 2:", linked_list_to_list(list2))
add_two_numbers_instance.plot_lists()
print("Result:", linked_list_to_list(add_two_numbers_instance.result))
