class BDeque:
    """
    A Bounded Deque implemented using a circular array of fixed capacity (b + 1).
    Allows adding or removing elements at either the front or the back in O(1) time.
    """
    def __init__(self, b):
        self.b = b
        self.capacity = b + 1
        self.a = [None] * self.capacity
        self.j = 0  # Head index
        self.n = 0  # Number of active elements

    def size(self):
        return self.n

    def get(self, i):
        if i < 0 or i >= self.n:
            raise IndexError("BDeque index out of bounds")
        return self.a[(self.j + i) % self.capacity]

    def set(self, i, x):
        if i < 0 or i >= self.n:
            raise IndexError("BDeque index out of bounds")
        val = self.a[(self.j + i) % self.capacity]
        self.a[(self.j + i) % self.capacity] = x
        return val

    def add(self, i, x):
        if i < 0 or i > self.n:
            raise IndexError("BDeque index out of bounds")
        if self.n >= self.capacity:
            raise IndexError("BDeque is full")
        
        # Shift elements to minimize shifts (Circular Buffer optimization)
        if i < self.n / 2:
            self.j = (self.j - 1) % self.capacity
            for k in range(i):
                self.a[(self.j + k) % self.capacity] = self.a[(self.j + k + 1) % self.capacity]
        else:
            for k in range(self.n, i, -1):
                self.a[(self.j + k) % self.capacity] = self.a[(self.j + k - 1) % self.capacity]
                
        self.a[(self.j + i) % self.capacity] = x
        self.n += 1

    def remove(self, i):
        if i < 0 or i >= self.n:
            raise IndexError("BDeque index out of bounds")
        x = self.a[(self.j + i) % self.capacity]
        
        if i < self.n / 2:
            for k in range(i, 0, -1):
                self.a[(self.j + k) % self.capacity] = self.a[(self.j + k - 1) % self.capacity]
            self.a[self.j] = None
            self.j = (self.j + 1) % self.capacity
        else:
            for k in range(i, self.n - 1):
                self.a[(self.j + k) % self.capacity] = self.a[(self.j + k + 1) % self.capacity]
            self.a[(self.j + self.n - 1) % self.capacity] = None
            
        self.n -= 1
        return x

    def to_list(self):
        return [self.get(i) for i in range(self.n)]


class Node:
    """
    A Node in the doubly-linked list. Each node contains a BDeque.
    """
    def __init__(self, b):
        self.d = BDeque(b)
        self.prev = None
        self.next = None


class SEList:
    """
    A Space-Efficient Linked List.
    """
    def __init__(self, b):
        if b < 2:
            raise ValueError("Block size b must be at least 2")
        self.b = b
        self.n = 0  # Total elements in the list
        self.dummy = Node(b)  # Sentinel dummy node to simplify boundary logic
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy

    def size(self):
        return self.n

    def find_it(self, i):
        """
        Locates the node containing the i-th element and returns (node, index_within_node).
        """
        if i < 0 or i > self.n:
            raise IndexError("Index out of bounds")
        
        # Determine whether to search forward from head or backward from tail
        if i < self.n / 2:
            u = self.dummy.next
            while i >= u.d.size():
                i -= u.d.size()
                u = u.next
            return u, i
        else:
            u = self.dummy
            idx = self.n
            while idx > i:
                u = u.prev
                idx -= u.d.size()
            return u, i - idx

    def get(self, i):
        u, j = self.find_it(i)
        return u.d.get(j)

    def set(self, i, x):
        u, j = self.find_it(i)
        return u.d.set(j, x)

    def add_before(self, w):
        """
        Inserts a new empty node before node w.
        """
        u = Node(self.b)
        u.prev = w.prev
        u.next = w
        u.next.prev = u
        u.prev.next = u
        return u

    def remove_node(self, u):
        """
        Removes a node from the doubly-linked list.
        """
        u.prev.next = u.next
        u.next.prev = u.prev

    def spread(self, u):
        """
        Triggered when b consecutive nodes are full. Spreads the elements
        across a newly created node to make room.
        """
        w = u
        for _ in range(self.b):
            w = w.next
        w = self.add_before(w)
        while w != u:
            while w.d.size() < self.b:
                val = w.prev.d.remove(w.prev.d.size() - 1)
                w.d.add(0, val)
            w = w.prev

    def gather(self, u):
        """
        Triggered when b consecutive nodes have size b - 1. Combines elements
        and frees up one node to reclaim space.
        """
        w = u
        for _ in range(self.b - 1):
            while w.d.size() < self.b:
                val = w.next.d.remove(0)
                w.d.add(w.d.size(), val)
            w = w.next
        self.remove_node(w)

    def add(self, i, x):
        if i < 0 or i > self.n:
            raise IndexError("Index out of bounds")
        
        # Optimization for direct appends
        if i == self.n:
            u = self.dummy.prev
            if u == self.dummy or u.d.size() == self.b + 1:
                u = self.add_before(self.dummy)
            u.d.add(u.d.size(), x)
            self.n += 1
            return

        u, j = self.find_it(i)
        r = 0
        curr = u
        # Look for a non-full node within b steps
        while r < self.b and curr != self.dummy and curr.d.size() == self.b + 1:
            curr = curr.next
            r += 1
        
        if r == self.b:
            self.spread(u)
            curr = u
            
        if curr == self.dummy:
            curr = self.add_before(curr)
            
        # Work backwards shifting elements to make room at insertion point u
        while curr != u:
            val = curr.prev.d.remove(curr.prev.d.size() - 1)
            curr.d.add(0, val)
            curr = curr.prev
            
        curr.d.add(j, x)
        self.n += 1

    def remove(self, i):
        if i < 0 or i >= self.n:
            raise IndexError("Index out of bounds")
        
        u, j = self.find_it(i)
        y = u.d.get(j)
        
        r = 0
        curr = u
        # Check if b consecutive nodes have size b - 1
        while r < self.b and curr != self.dummy and curr.d.size() == self.b - 1:
            curr = curr.next
            r += 1
            
        if r == self.b:
            self.gather(u)
            
        u.d.remove(j)
        curr = u
        # Shift elements forward to maintain minimum density threshold
        while curr.d.size() < self.b - 1 and curr.next != self.dummy:
            val = curr.next.d.remove(0)
            curr.d.add(curr.d.size(), val)
            curr = curr.next
            
        if curr.d.size() == 0:
            self.remove_node(curr)
            
        self.n -= 1
        return y

    def to_list(self):
        """
        Utility method to output all elements in a flat Python list.
        """
        res = []
        u = self.dummy.next
        while u != self.dummy:
            res.extend(u.d.to_list())
            u = u.next
        return res

    def get_blocks_repr(self):
        """
        Utility method to show the internal array distribution of the nodes.
        """
        res = []
        u = self.dummy.next
        while u != self.dummy:
            res.append(u.d.to_list())
            u = u.next
        return res
