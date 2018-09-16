# Binary Tree
#
# 1. every node has at most two children
#

# Full Binary Tree
#
# 1. every node has either 0 or 2 children

# Complete Binary Tree
#
# 1. every level (except possibly the last) is completely filled
# 2. all nodes are as far left as possible

# Perfect Binary Tree
#
# 1. all internal nodes have two children
# 2. all leaves are at the same level

# Balanced Binary Tree
#
# 1.

# Degenerate/Pathological Tree


# Binary Search Tree
#
# 1. the key in each node >= any keys in the left sub-tree
# 2. the key in each node <= any keys in the right sub-tree
# 3. the leaves contain no key

from collections import deque

class BinarySearchTree:
    def __init__(self):
        self._root = BSTNil()
    @property
    def root(self):
        return self._root
    #
    def __contains__(self, key):
        return self._root.search(key) is not None
    #
    def __getitem__(self, key):
        node = self._root.search(key)
        if node is None or node.is_nil():
            raise IndexError()
        return node.value
    #
    def insert(self, key, value):
        raise NotImplementedError()
    #
    def remove(self, key):
        raise NotImplementedError()

class Node:
    def __init__(self, left, right):
        self._left = left
        self._right = right
    @property
    def left(self):
        return self._left
    @property
    def right(self):
        return self._right
    def is_nil(self):
        return False
    # N-L-R DFS
    def preorder_traverse(self, f):
        f(self)
        self.left.preorder_traverse(f)
        self.right.preorder_traverse(f)
    # L-N-R DFS
    def inorder_traverse(self, f):
        self.left.inorder_traverse(f)
        f(self)
        self.right.inorder_traverse(f)
    # L-R-N DFS
    def postorder_traverse(self, f):
        self.left.postorder_traverse(f)
        self.right.postorder_traverse(f)
        f(self)
    # breadth-first search
    # aka Level-order traversal
    def bfs(self, f):
        q = deque([self])
        while len(q) > 0:
            node = q.popleft()
            if node.is_nil():
                continue
            f(node)
            q.append(node.left)
            q.append(node.right)

class Nil:
    @property
    def left(self):
        return Nil()
    @property
    def right(self):
        return Nil()
    def is_nil(self):
        return True
    def preorder_traverse(self, f):
        pass
    def inorder_traverse(self, f):
        pass
    def postorder_traverse(self, f):
        pass

class BSTNode(Node):
    def __init__(self, key, value, left, right):
        super().__init__(left, right)
        self._key = key
        self._value = value
    @property
    def key(self):
        return self._key
    @property
    def value(self):
        return self._value
    #
    def search(self, key):
        if key == self.key:
            return self
        elif key < self.key:
            return self.left.search(key)
        else:
            return self.right.search(key)
    #
    def insert(self, key, value):
        raise NotImplementedError()
    #
    def remove(self, key):
        raise NotImplementedError()

class BSTNil(Nil):
    def search(self, key):
        return None
    def insert(self, key, value):
        raise NotImplementedError()
    def remove(self, key):
        raise NotImplementedError()

# References:
# https://www.geeksforgeeks.org/binary-tree-set-3-types-of-binary-tree/
# http://web.cecs.pdx.edu/~sheard/course/Cs163/Doc/FullvsComplete.html
# http://web.cecs.pdx.edu/~sheard/course/Cs163/Doc/HeapReview.html
# https://en.wikipedia.org/wiki/Binary_tree
# https://en.wikipedia.org/wiki/Binary_search_tree
# https://en.wikipedia.org/wiki/Tree_traversal
