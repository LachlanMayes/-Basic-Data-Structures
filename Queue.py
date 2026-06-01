class Queue:
    def __init__(self):
        self.items =[]

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def enqueue(self, item):
        """Add an item to the back of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if not self.is_empty():
            return self.items.pop(0)
        return "Queue is empty"

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)

    def peek(self):
        """Look at the front item without removing it."""
        if not self.is_empty():
            return self.items[0]
        return "Queue is empty"
