# Fibonacci Heap

class FibonacciHeap:
    def __init__(self):
        self.min_root = None
        self.forest_head = None
        self.forest_tail = None
    #
    def empty(self):
        return not bool(self.min_root)
    #
    # T = O(1)
    def peak(self):
        return self.min_root.key
    #
    # T = O(1)
    def push(self, key):
        node = Node(key)
        if self.forest_head:
            self.forest_tail.next = node
        else:
            self.forest_head = node
        self.forest_tail = node
        if (not self.min_root) or self.min_root.key > key:
            self.min_root = node
    #
    # T = O(log(n))
    def pop(self):
        pass
    #
    # T = O(1)
    def merge(self, other):
        if self.forest_head:
            self.forest_tail.next = other.forest_head
        else:
            self.forest_head = other.forest_head
        self.forest_tail = other.forest_tail
        if (not self.min_root) or (other.min_root and self.min_root.key > other.min_root):
            self.min_root = other.min_root
        other.min_root = None
        other.forest_head = None
        other.forest_tail = None

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.child = None
        self.order = 0
        self.marked = False
