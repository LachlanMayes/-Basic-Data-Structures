class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Check if the deque is empty."""
        return len(self.items) == 0

    def add_front(self, item):
        """Add an item to the front of the deque."""
        self.items.insert(0, item)

    def add_rear(self, item):
        """Add an item to the rear of the deque."""
        self.items.append(item)

    def remove_front(self):
        """Remove and return the item from the front of the deque."""
        if not self.is_empty():
            return self.items.pop(0)
        return "Deque is empty"

    def remove_rear(self):
        """Remove and return the item from the rear of the deque."""
        if not self.is_empty():
            return self.items.pop()
        return "Deque is empty"

    def peek_front(self):
        """Get the item at the front without removing it."""
        if not self.is_empty():
            return self.items[0]
        return "Deque is empty"

    def peek_rear(self):
        """Get the item at the rear without removing it."""
        if not self.is_empty():
            return self.items[-1]
        return "Deque is empty"

    def size(self):
        """Return the number of items in the deque."""
        return len(self.items)
