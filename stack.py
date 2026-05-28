class Stack:
    """A standard LIFO (Last-In, First-Out) stack implementation."""
    def __init__(self):
        self._storage = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self._storage.append(item)

    def pop(self):
        """Remove and return the top item. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")
        return self._storage.pop()

    def peek(self):
        """Return the top item without removing it. Returns None if empty."""
        if self.is_empty():
            return None
        return self._storage[-1]

    def is_empty(self):
        """Return True if the stack has no elements, False otherwise."""
        return len(self._storage) == 0

    def __len__(self):
        """Return the number of elements in the stack using len()."""
        return len(self._storage)

    def __repr__(self):
        return f"Stack({self._storage})"
