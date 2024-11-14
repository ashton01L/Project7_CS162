# Author: Ashton Lee
# Github User: ashton01L
# Date: 11/13/2024
# Description: Write a LinkedList class that has recursive implementations of the add and remove methods described
# in the Exploration.
class Node:
    """A class representing a node in a linked list."""

    def __init__(self, data):
        self.data = data  # Value of the node
        self.next = None  # Reference to the next node in the list


class LinkedList:
    """A class representing a singly linked list with recursive methods."""

    def __init__(self):
        self._head = None  # Initialize the head of the list as private

    def get_head(self):
        """Returns the first node in the list."""
        return self._head

    def add(self, data):
        """Recursively adds a node with given data at the front of the list."""

        def _add(node, data):
            """Helper recursive function to add a node at the front."""
            if node is None:
                return Node(data)
            new_node = Node(data)
            new_node.next = node
            return new_node

        self._head = _add(self._head, data)

    def remove(self):
        """Recursively removes the last node from the list."""

        def _remove(node):
            """Helper recursive function to remove the last node."""
            if node is None or node.next is None:
                return None
            node.next = _remove(node.next)
            return node

        self._head = _remove(self._head)

    def contains(self, data):
        """Recursively checks if list contains a node with the given data."""

        def _contains(node):
            """Helper recursive function to check if data exists."""
            if node is None:
                return False
            if node.data == data:
                return True
            return _contains(node.next)

        return _contains(self._head)

    def insert(self, index, data):
        """Recursively inserts a node with given data at the specified index."""

        def _insert(node, index):
            """Helper recursive function to insert at given index."""
            if index == 0:
                new_node = Node(data)
                new_node.next = node
                return new_node
            if node is None:
                raise IndexError("Index out of bounds")
            node.next = _insert(node.next, index - 1)
            return node

        if index < 0:
            raise IndexError("Index out of bounds")
        self._head = _insert(self._head, index)

    def reverse(self):
        """Recursively reverses the linked list."""

        def _reverse(node, prev=None):
            """Helper recursive function to reverse the list."""
            if node is None:
                return prev
            next_node = node.next
            node.next = prev
            return _reverse(next_node, node)

        self._head = _reverse(self._head, prev=None)

    def to_plain_list(self):
        """Recursively converts the linked list to a regular Python list."""

        def _to_plain_list(node):
            """Helper recursive function to convert list to Python list."""
            if node is None:
                return []
            return _to_plain_list(node.next) + [node.data]

        return _to_plain_list(self._head)

    def display(self):
        """Displays contents of the list."""

        def _display(node):
            """Helper recursive function to display the list."""
            if node is None:
                return
            print(node.data, end=" -> ")
            _display(node.next)

        _display(self._head)
        print("None")


# # Example usage and test cases
# ll = LinkedList()
# ll.add(3)
# ll.add(2)
# ll.add(1)
# ll.display()  # Expected: 1 -> 2 -> 3 -> None
#
# ll.insert(2, 4)
# ll.display()  # Expected: 1 -> 2 -> 4 -> 3 -> None
#
# ll.remove()
# ll.display()  # Expected: 1 -> 2 -> 4 -> None
#
# ll.reverse()
# ll.display()  # Expected: 4 -> 2 -> 1 -> None
#
# print("Contains 2:", ll.contains(2))  # Expected: True
# print("Contains 5:", ll.contains(5))  # Expected: False
#
# plain_list = ll.to_plain_list()
# print("Plain list:", plain_list)  # Expected: [4, 2, 1]
