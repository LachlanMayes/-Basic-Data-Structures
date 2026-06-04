class ArrayStack:
    def __init__(self):
        self.capacity = 1
        self.a = [None] * self.capacity  # The backing array
        self.n = 0                       # Number of elements currently in the stack

    def size(self):
        """Returns the number of elements in the stack."""
        return self.n

    def get(self, i):
        """Returns the element at index i."""
        if i < 0 or i >= self.n:
            raise IndexError("Index out of bounds")
        return self.a[i]

    def set(self, i, x):
        """Replaces the element at index i with x and returns the old element."""
        if i < 0 or i >= self.n:
            raise IndexError("Index out of bounds")
        old_val = self.a[i]
        self.a[i] = x
        return old_val

    def _resize(self):
        """Resizes the backing array to double the current size of n."""
        new_capacity = max(1, 2 * self.n)
        new_a = [None] * new_capacity
        # Copy elements from old array to new array
        for k in range(self.n):
            new_a[k] = self.a[k]
        self.a = new_a
        self.capacity = new_capacity

    def add(self, i, x):
        """Inserts x at index i, shifting subsequent elements to the right."""
        if i < 0 or i > self.n:
            raise IndexError("Index out of bounds")
        
        # If the array is full, double its capacity
        if self.n + 1 > self.capacity:
            self._resize()
            
        # Shift elements from index i to n-1 one position to the right
        for k in range(self.n, i, -1):
            self.a[k] = self.a[k - 1]
            
        self.a[i] = x
        self.n += 1

    def remove(self, i):
        """Removes the element at index i, shifting subsequent elements to the left."""
        if i < 0 or i >= self.n:
            raise IndexError("Index out of bounds")
        
        removed_val = self.a[i]
        
        # Shift elements from index i+1 to n-1 one position to the left
        for k in range(i, self.n - 1):
            self.a[k] = self.a[k + 1]
            
        self.a[self.n - 1] = None  # Clear the reference to avoid memory leaks
        self.n -= 1
        
        # If the array is mostly empty, shrink its capacity
        if self.capacity >= 3 * self.n:
            self._resize()
            
        return removed_val

    def push(self, x):
        """Pushes x to the top of the stack."""
        self.add(self.n, x)

    def pop(self):
        """Pops and returns the element from the top of the stack."""
        if self.n == 0:
            raise IndexError("Pop from empty stack")
        return self.remove(self.n - 1)

    def to_list(self):
        """Utility helper to view active elements as a standard Python list."""
        return [self.a[k] for k in range(self.n)]

