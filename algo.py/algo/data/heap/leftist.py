# Leftist Heap

class LeftistHeap:
    def __init__(self):
        self._root = None
    # T = O(1)
    def peak(self):
        if self._root:
            return self._root.key
        else:
            return None
    # T = O(log(n))
    def pop(self):
        if self._root:
            node = self._root
            self._root = _meld_trees(self._root.left, self._root.right)
            return node.key
        else:
            return None
    # T = O(log(n))
    def push(self, key):
        node = Node(key)
        self._root = _meld_trees(self._root, node)
    # T = O(log(n))
    def meld(self, other):
        self._root = _meld_trees(self._root, other._root)
        other._root = None

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        # shortest <= log2(n+1)
        self.shortest = 1

def _meld_trees(a, b):
    if a and b:
        # make a be the smaller tree
        if a.key > b.key:
            a, b = b, a
        # create binary tree such that the smallest key in each subtree is in the root
        if not a.right:
            a.right = b
        else:
            a.right = _meld_trees(a.right, b)
        # leftist tree property
        if (not a.left) or (a.left.shortest < a.right.shortest):
            a.left, a.right = a.right, a.left
        # set shortest
        if not a.right:
            a.shortest = 1
        else:
            a.shortest = a.right.shortest + 1
        return a
    elif a:
        return a
    else:
        return b
