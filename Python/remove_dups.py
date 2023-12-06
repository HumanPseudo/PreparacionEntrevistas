"""
 * Escribe un algoritmo para eliminar los elementos duplicados en una Lista enlazada
 *
 * Ejemplo:
 *  Input: 1->2->2->3->4->1
 *  Output: 1->2->3->4
 *
 *
 *
 * Follow-up: ¿Cuál sería tu solución si no pudieras utilizar memoria adicional?
"""

class RemoveDuplicates:
    """Class to remove duplicates from a linked list."""

    def __init__(self, head):
        """
        Initialize the RemoveDuplicates instance.

        Parameters:
        - head: The head node of the linked list.
        """
        self.head = head

    def remove_duplicates(self):
        """
        Remove duplicates from the linked list.
        """
        if self.head is None:
            return

        found_values = set()
        current = self.head
        found_values.add(current.data)

        while current.next_node is not None:
            if current.next_node.data not in found_values:
                found_values.add(current.next_node.data)
                current = current.next_node
            else:
                current.next_node = current.next_node.next_node

    def display(self):
        """
        Display the elements of the linked list.
        """
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next_node
        print(" -> ".join(map(str, elements)))

# Example usage:
# Assuming you have a linked list created somewhere
# linked_list = ...

# Create an instance of RemoveDuplicates
"""remover = RemoveDuplicates(linked_list.head)

# Display the original linked list
print("Original Linked List:")
remover.display()

# Remove duplicates
remover.remove_duplicates()

# Display the linked list after removing duplicates
print("\nLinked List after Removing Duplicates:")
remover.display()"""
