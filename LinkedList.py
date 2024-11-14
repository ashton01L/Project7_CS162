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
        """Returns the first node in list."""
        return self._head

    def insert_front(self, data):
        """Recursively adds a node with given data at front of list."""
        new_node = Node(data)
        new_node.next = self._head
        self._head = new_node

    def delete_last(self):
        """Recursively removes last node from list."""

        def _delete_last(node):
            if node.next is None:
                return None
            elif node.next.next is None:
                node.next = None
            else:
                _delete_last(node.next)

        if self._head is not None:
            if self._head.next is None:
                self._head = None
            else:
                _delete_last(self._head)

    def contains(self, data):
        """Recursively checks if list contains a node with given data."""

        def _contains(node):
            if node is None:
                return False
            if node.data == data:
                return True
            return _contains(node.next)

        return _contains(self._head)

    def insert(self, index, data):
        """Recursively inserts a node with given data at specified index."""

        def _insert(node, index):
            if index == 0:
                new_node = Node(data)
                new_node.next = node
                return new_node
            if node is None:
                raise IndexError("Index out of bounds")
            node.next = _insert(node.next, index - 1)
            return node

        self._head = _insert(self._head, index)

    def reverse(self):
        """Recursively reverses linked list."""

        def _reverse(node, prev=None):
            if node is None:
                return prev
            next_node = node.next
            node.next = prev
            return _reverse(next_node, node)

        self._head = _reverse(self._head)

    def to_plain_list(self):
        """Recursively converts linked list to a regular Python list."""

        def _to_plain_list(node):
            if node is None:
                return []
            return [node.data] + _to_plain_list(node.next)

        return _to_plain_list(self._head)

    def display(self):
        """Displays contents of list."""

        def _display(node):
            if node is None:
                return
            print(node.data, end=" -> ")
            _display(node.next)

        _display(self._head)
        print("None")


# Example usage
ll = LinkedList()
ll.insert_front(3)
ll.insert_front(2)
ll.insert_front(1)
ll.display()  # Expected: 1 -> 2 -> 3 -> None

ll.insert(2, 4)
ll.display()  # Expected: 1 -> 2 -> 4 -> 3 -> None

ll.delete_last()
ll.display()  # Expected: 1 -> 2 -> 4 -> None

ll.reverse()
ll.display()  # Expected: 4 -> 2 -> 1 -> None

print("Contains 2:", ll.contains(2))  # Expected: True
print("Contains 5:", ll.contains(5))  # Expected: False

plain_list = ll.to_plain_list()
print("Plain list:", plain_list)  # Expected: [4, 2, 1]