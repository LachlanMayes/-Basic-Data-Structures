class Node:
    """Represents a single node in the doubly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """Represents the doubly linked list structure."""
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """Adds a new node with the specified data to the end of the list."""
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            self.tail = new_node
            return
        
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def prepend(self, data):
        """Adds a new node with the specified data to the beginning of the list."""
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            self.tail = new_node
            return
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def delete(self, data):
        """Deletes the first occurrence of a node with the specified data."""
        current = self.head
        
        while current:
            if current.data == data:
                # Case 1: The list has only one node
                if current == self.head and current == self.tail:
                    self.head = None
                    self.tail = None
                # Case 2: Deleting the head node
                elif current == self.head:
                    self.head = self.head.next
                    self.head.prev = None
                # Case 3: Deleting the tail node
                elif current == self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = None
                # Case 4: Deleting a node in the middle
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return True  # Node found and deleted
            
            current = current.next
        return False  # Node not found

    def display_forward(self):
        """Prints the list from head to tail."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" <-> ".join(elements) if elements else "Empty List")

    def display_backward(self):
        """Prints the list from tail to head."""
        elements = []
        current = self.tail
        while current:
            elements.append(str(current.data))
            current = current.prev
        print(" <-> ".join(elements) if elements else "Empty List")
