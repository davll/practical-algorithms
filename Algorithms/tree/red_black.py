# Red-Black Tree
#
# 1. Every node has a colour either red or black
# 2. Root is always black
# 3. There are no two adjacent red nodes
# 4. Every path from root to a NIL node has same number of black nodes
#

from enum import Enum

class Colour(Enum):
    RED = 1
    BLACK = 2

class Branch(Enum):
    UNKNOWN = -1
    LEFT = 0
    RIGHT = 1

class BaseNode:
    def __init__(self):
        self._parent = None
        self._left = None
        self._right = None
        self._branch = Branch.UNKNOWN
    @property
    def is_root(self):
        return self.parent is None
    @property
    def is_leaf(self):
        return self.left is None and self.right is None
    @property
    def parent(self):
        return self._parent
    @property
    def left(self):
        return self._left
    @property
    def right(self):
        return self._right
    @property
    def branch(self):
        return self._branch
    @property
    def grandparent(self):
        if self.parent:
            return self.parent.parent
        else:
            return None
    @property
    def sibling(self):
        if self.parent:
            if self._branch == Branch.LEFT:
                return self.parent.right
            else:
                return self.parent.left
        else:
            return None
    @property
    def uncle(self):
        if self.parent:
            return self.parent.sibling
        else:
            return None
    @left.setter
    def set_left(self, node):
        node, self._left = self._left, node
        if self._left:
            assert self._left.parent is None
            self._left._parent = self
            self._left._branch = Branch.LEFT
        if node:
            assert node.parent is self
            assert node._branch == Branch.LEFT
            node._parent = None
            node._branch = Branch.UNKNOWN
    @right.setter
    def set_right(self, node):
        node, self._right = self._right, node
        if self._right:
            assert self._right.parent is None
            self._right._parent = self
            self._right._branch = Branch.RIGHT
        if node:
            assert node.parent is self
            assert node._branch == Branch.RIGHT
            node._parent = None
            node._branch = Branch.UNKNOWN
    # detach from parent
    def detach(self):
        p = self.parent
        if p is not None:
            if self.branch == Branch.LEFT:
                assert p.left == self
                p.left = None
            else:
                assert p.right == self
                p.right = None
        assert self.parent is None
    #
    #      SELF                 R
    #     /    \      =>       / \
    #    L      R          SELF   RR
    #          / \         /  \
    #         RL  RR      L   RL
    #
    def left_rotate(self):
        assert self.right is not None
        p, b, r = self.parent, self.branch, self.right
        rl = r.left
        self.detach()
        self.right = None
        r.left = self
        self.right = rl
        if p is not None:
            if b == Branch.LEFT:
                p.left = r
            else:
                p.right = r
        return r
    #
    #       SELF           L
    #      /   \     =>   / \
    #     L     R       LL   SELF
    #    / \                 /   \
    #   LL LR               LR    R
    #
    def right_rotate(self):
        assert self.left is not None
        p, b, l = self.parent, self.branch, self.left
        lr = l.right
        self.detach()
        self.left = None
        l.right = self
        self.left = lr
        if p is not None:
            if b == Branch.LEFT:
                p.left = l
            else:
                p.right = l
        return l

class Node(BaseNode):
    def __init__(self, key, val, colour = Colour.RED):
        super().__init__()
        self.colour = colour
        self.key = key
        self.value = val
    #
    def __repr__(self):
        return '{c}-Node({k},{v})'.format(c = self.colour, k = self.key, v = self.value)

class RBTree:
    def __init__(self):
        self.root = None
    def insert(self, key, val):
        if self.root is None:
            self.root = Node(key, val, colour = Colour.BLACK)
            assert self.root.is_root
            return
        # traverse to find place to insert
        node = self.root
        while True:
            if key < node.key:
                if node.left is None:
                    node.left = Node(key, val)
                    node = node.left
                    break
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = Node(key, val)
                    node = node.right
                    break
                else:
                    node = node.right
        # keep balanced
        while not node.is_root and node.colour == Colour.RED and node.parent.colour == Colour.RED:
            uncle, parent, grandparent = node.uncle, node.parent, node.grandparent
            assert uncle is not None
            assert grandparent is not None
            assert grandparent.colour == Colour.BLACK
            if uncle.colour == Colour.RED:
                #
                #        GP(B)             GP(R)
                #       /    \            /    \
                #     P(R)   U(R)  =>   P(B)   U(B)
                #     /                 /
                #    X(R)              X(R)
                #
                uncle.colour = Colour.BLACK
                parent.colour = Colour.BLACK
                grandparent.colour = Colour.RED
                node = grandparent
            else if parent.branch == Branch.LEFT:
                if node.branch == Branch.LEFT:
                    #
                    #        GP(B)            P(B)
                    #       /    \           /    \
                    #     P(R)   U(B)  =>  X(R)   GP(R)
                    #     /  \                   /    \
                    #   X(R)  PR                PR    U(B)
                    #
                    parent.colour = Colour.BLACK
                    grandparent.colour = Colour.RED
                    node = grandparent.right_rotate()
                    if node.is_root:
                        self.root = node
                    break
                else:
                    #
                    #        GP(B)
                    #       /    \
                    #     P(R)   U(B)
                    #    /   \
                    #   PL   X(R)
                    #
                    node = parent.left_rotate()
            else:
                if node.branch == Branch.LEFT:
                    #
                    #       GP(B)
                    #      /    \
                    #    U(B)   P(R)
                    #           /  \
                    #         X(R)  PR
                    #
                    node = parent.right_rotate()
                else:
                    #
                    #       GP(B)
                    #      /    \
                    #    U(B)   P(R)
                    #          /   \
                    #         PL   X(R)
                    #
                    parent.colour = Colour.BLACK
                    grandparent.colour = Colour.RED
                    node = grandparent.left_rotate()
                    if node.is_root:
                        self.root = node
                    break
        # make root black
        assert self.root.is_root
        self.root.colour = Colour.BLACK
    def remove(self, key):

# References:
# https://www.geeksforgeeks.org/red-black-tree-set-1-introduction-2/
