from singleLinkedList import Node
import matplotlib.pyplot as plt

class AddTwoNumbers:
    def __init__(self, list1, list2):
        self.result = Node(-1)
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

            self.current.next_node = Node(digit_sum % 10)
            self.current = self.current.next_node
            self.carry = digit_sum // 10

            # Print lists to console
            print("List 1:", self.linked_list_to_list(list1) if list1 else [])
            print("List 2:", self.linked_list_to_list(list2) if list2 else [])
            print("Result:", self.linked_list_to_list(self.result))

            # Update plot data
            self.plot_data['list1'].append(self.linked_list_to_list(list1) if list1 else [])
            self.plot_data['list2'].append(self.linked_list_to_list(list2) if list2 else [])
            self.plot_data['result'].append(self.linked_list_to_list(self.result))

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

# Plotting example
plt.plot(add_two_numbers.plot_data['list1'], label='List 1')
plt.plot(add_two_numbers.plot_data['list2'], label='List 2')
plt.plot(add_two_numbers.plot_data['result'], label='Result')
plt.legend()
plt.show()