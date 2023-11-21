import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self, data=None):
        """
        Initialize a new Node object.

        Args:
            data: The data to be stored in the node.
        """
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        """
        Initialize a new LinkedList object.
        """
        self.head = None

    def is_empty(self):
        """
        Check if the linked list is empty.

        Returns:
            True if the linked list is empty, False otherwise.
        """
        return self.head is None

    def append(self, data):
        """
        Append a new node with the given data to the end of the linked list.

        Args:
            data: The data to be stored in the new node.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next_node:
            last_node = last_node.next_node
        last_node.next_node = new_node

    def prepend(self, data):
        """
        Prepend a new node with the given data to the beginning of the linked list.

        Args:
            data: The data to be stored in the new node.
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def delete(self, data):
        """
        Delete the first occurrence of a node with the given data from the linked list.

        Args:
            data: The data of the node to be deleted.
        """
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next_node
            return

        current_node = self.head
        while current_node.next_node and current_node.next_node.data != data:
            current_node = current_node.next_node

        if current_node.next_node:
            current_node.next_node = current_node.next_node.next_node

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

    def draw(self):
        """
        Display a graphical representation of the linked list using networkx and matplotlib.
        """
        G = nx.DiGraph()
        current_node = self.head
        while current_node:
            G.add_node(current_node.data)
            if current_node.next_node:
                G.add_edge(current_node.data, current_node.next_node.data)
            current_node = current_node.next_node

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", arrowsize=20)
        plt.show()

# Example usage:
# linked_list = LinkedList()
# linked_list.append(1)
# linked_list.append(2)
# linked_list.prepend(0)
# linked_list.display()  # Output: 0 -> 1 -> 2
# linked_list.draw()  # Display a graphical representation of the linked list
# linked_list.delete(1)
# linked_list.display()  # Output: 0 -> 2
# linked_list.draw()  # Display a graphical representation of the updated linked list