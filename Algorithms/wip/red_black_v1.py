# Red-Black Tree
#
# 1. Every node has a colour either red or black
# 2. Root is always black
# 3. There are no two adjacent red nodes
# 4. Every path from root to a NIL node has same number of black nodes
#

from enum import Enum

class RedBlackTree:
    def __init__(self):
        self._root = Nil()
    def insert(self, key, value):
        node = Node(Nil(), key, Nil(), value, color = Color.RED)
        self.root = self.root.update(node).blacken()
    def remove(self, key):
        self.root = self.root.remove(key)

class Color(Enum):
    RED = 1
    BLACK = 2

class Node:
    def __init__(self, left, key, right, value, color = Color.RED):
        self._color = color
        self._left = left
        self._right = right
        self._key = key
        self._value = value
        self._count = 1 + len(left) + len(right)
    def __len__(self):
        return self._count
    @property
    def key(self):
        return self._key
    @property
    def value(self):
        return self._value
    @property
    def left(self):
        return self._left
    @property
    def right(self):
        return self._right
    #
    def is_nil(self):
        return False
    def is_black(self):
        return self._color == Color.BLACK
    def is_red(self):
        return self._color == Color.RED
    def __contains__(self, key):
        if key < self.key:
            return key in self.left
        elif key > self.key:
            return key in self.right
        else:
            return True
    def __getitem__(self, key):
        if key < self.key:
            return self.left[key]
        elif key > self.key:
            return self.right[key]
        else:
            return self.value
    #
    def rotate_left(self):
        right = self.right
        left = Node(self.left, self.key, right.left, self.value, color = self.color)
        return Node(left, right.key, right.right, right.value, color = right.color)
    def rotate_right(self):
        left = self.left
        right = Node(self.right, self.key, left.right, self.value, color = self.color)
        return Node(left.left, left.key, right, left.value, color = left.color)
    def blacken(self):
        if self.is_red:
            return Node(self.left, self.key, self.right, self.value, color = Color.BLACK)
        else:
            return self
    def recolor(self):
        return Node(self.left.blacken(), self.key, self.right.blacken(), self.value, color = Color.RED)
    def maintain(self):
        if self.is_red():
            return self
        elif self.left.is_red():
            if self.right.is_red():
                return self.recolor()
            elif self.left.left.is_red():
                return self.rotate_right().recolor()
            elif self.left.right.is_red():
                node = Node(self.left.rotate_left(), self.key, self.right, self.value, color = self.color)
                return node.rotate_right().recolor()
            else:
                return self
        elif self.right.is_red():
            # self.left.is_red() == False
            if self.right.right.is_red():
                return self.rotate_left().recolor()
            elif self.right.left.is_red():
                node = Node(self.left, self.key, self.right.rotate_right(), self.value, color = self.color)
                return node.rotate_left().recolor()
            else:
                return self
        else:
            return self
    def update(self, node):
        if node.is_nil():
            return self
        if node.key < self.key:
            l = self.left.update(node).maintain()
            return Node(l, self.key, self.right, self.value, color = self.color).maintain()
        else:
            r = self.right.update(node).maintain()
            return Node(self.left, self.key, r, self.value, color = self.color).maintain()
    def remove(self, key):
        if key == self.key:
            return self._remove().maintain()
        elif key < self.key:
            l = self.left.remove(key).maintain()
            return Node(l, self.key, self.right, self.value, color = self.color).maintain()
        else:
            r = self.right.remove(key).maintain()
            return Node(self.left, self.key, r, self.value, color = self.color).maintain()
    def _remove(self):
        if self.left.is_nil() and self.right.is_nil():
            return Nil()
        elif not self.left.is_nil() and not self.right.is_nil():
            def scan_inorder_successor():
            node = self.right
            stack = []
            while True:
                stack.append(node)
                if node.left.is_nil():
                    break
                node = node.left
            r = self.right.remove(node.key)
            node = Node(self.left, node.key, r, node.value, color = self.color)
            return node
        else if self.left.is_nil():
            return self.right
        else:
            return self.left
class Nil:
    @property
    def left(self):
        return Nil()
    @property
    def right(self):
        return Nil()
    #
    def is_nil(self):
        return True
    def is_black(self):
        return True
    def is_red(self):
        return False
    def __contains__(self, key):
        return False
    def __getitem__(self, key):
        raise IndexError()
    #
    def update(self, node):
        return node
    def remove(self, key):
        raise IndexError()
    def maintain(self):
        return self

# References:
# https://www.geeksforgeeks.org/red-black-tree-set-1-introduction-2/
# https://www.geeksforgeeks.org/red-black-tree-set-2-insert/
# https://www.geeksforgeeks.org/red-black-tree-set-3-delete-2/
# http://scottlobdell.me/2016/02/purely-functional-red-black-trees-python/
