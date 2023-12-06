from singleLinkedList import Node

class AddTwoNumbers:
    def __init__(self, list1, list2):
        self.result = Node(-1)  # Initialize with a placeholder value
        self.current = self.result
        self.carry = 0
        self.plot_data = {'list1': [], 'list2': [], 'result': []}

        while list1 or list2 or self.carry:
            digit_sum = self.carry

            if list1:
                digit_sum += list1.data
                list1 = list1.next_node
            if list2:
                digit_sum += list2.data
                list2 = list2.next_node

            self.carry = digit_sum // 10
            self.current.next_node = Node(digit_sum % 10)
            self.current = self.current.next_node

        if self.carry > 0:
            self.current.next_node = Node(self.carry)

        # Move to the actual result node
        self.result = self.result.next_node

    def linked_list_to_list(self, node):
        result = []
        while node:
            result.append(node.data)
            node = node.next_node
        return result

# Example usage
list1 = Node(2)
list1.next_node = Node(4)
list1.next_node.next_node = Node(3)

list2 = Node(5)
list2.next_node = Node(6)
list2.next_node.next_node = Node(4)

add_two_numbers = AddTwoNumbers(list1, list2)

# Print the result
result_list = add_two_numbers.linked_list_to_list(add_two_numbers.result)
print(result_list)
