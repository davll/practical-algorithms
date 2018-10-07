# Red-Black Tree
#
# 1. Every node has a color either red or black
# 2. Root is always black
# 3. There are no two adjacent red nodes
#    => a red node cannot have a red parent or red child
# 4. Every path from root to Nil node has same number of black nodes
#
# https://www.cs.usfca.edu/~galles/visualization/RedBlack.html
# http://cs.armstrong.edu/liang/animation/web/RBTree.html

from algo.data.tree.binary_tree import bt_rotate_left, bt_rotate_right
from algo.data.tree.binary_search_tree import bst_search

class RedBlackTree:
    def __init__(self):
        self._root = None
    #
    @property
    def root(self):
        return self._root
    #
    def __contains__(self, key):
        return bst_search(self._root, key) is not None
    def __getitem__(self, key):
        node = bst_search(self._root, key)
        if node is None:
            raise IndexError()
        return node.value
    def __setitem__(self, key, value):
        self.insert(key, value)
    def __delitem__(self, key):
        self.remove(key)
    def insert(self, key, value):
        self._root = _insert(self._root, key, value)
        self._root.black = True
    def remove(self, key):
        self._root = _remove(self._root, key)

class Node:
    def __init__(self, key, value, black=False):
        self.key = key
        self.value = value
        self.black = black
        self.left = None
        self.right = None

class DoubleBlack:
    def __init__(self, node):
        self.node = node

def _is_black(node):
    return node is None or node.black

def _is_red(node):
    return not _is_black(node)

def _is_leaf(node):
    return node is not None and node.left is None and node.right is None

def _need_maintain(node):
    return _is_red(node) and (_is_red(node.left) or _is_red(node.right))

def _recolor(root):
    root.left.black = True
    root.right.black = True
    root.black = False

def _insert(root, key, value):
    if root is None:
        return Node(key, value)
    if key == root.key:
        root.value = value
        return root
    elif key < root.key:
        root.left = _insert(root.left, key, value)
        # maintain
        if _need_maintain(root.left): # parent
            assert _is_black(root)
            if _is_red(root.right): # uncle
                _recolor(root)
            else:
                if _is_red(root.left.left):
                    root.black = False
                    root.left.black = True
                    root = bt_rotate_right(root)
                else: # _is_red(root.left.right)
                    root.left = bt_rotate_left(root.left)
                    root.black = False
                    root.left.black = True
                    root = bt_rotate_right(root)
    else: # k > root.key
        root.right = _insert(root.right, key, value)
        # maintain
        if _need_maintain(root.right): # parent
            assert _is_black(root)
            if _is_red(root.left): # uncle
                _recolor(root)
            else:
                if _is_red(root.right.right):
                    root.black = False
                    root.right.black = True
                    root = bt_rotate_left(root)
                else: # _is_red(root.right.left)
                    root.right = bt_rotate_right(root.right)
                    root.black = False
                    root.right.black = True
                    root = bt_rotate_left(root)
    return root

def _remove(root, key):
    if not root:
        raise IndexError()
    if key == root.key:
        if _is_leaf(root):
            if _is_red(root):
                return None
            else:
                raise NotImplementedError()
        elif root.left and not root.right:
            raise NotImplementedError()
        # TODO
        raise NotImplementedError()
    elif key < root.key:
        root.left = _remove(root.left, key)
        # TODO: maintain
    else: # key > root.key
        root.right = _remove(root.right, key)
        # TODO: maintain
    return root

def _validate(root):
    if not _is_black(root):
        return False
    def _max_black_path(node, d):
        if _is_black(node):
            d += 1
        if not node:
            return d
        else:
            l = _max_black_path(node.left, d)
            r = _max_black_path(node.right, d)
            return max(l, r)
    def _check_black_path(node, d, exp):
        if _is_black(node):
            d += 1
        if not node:
            return d == exp
        else:
            l = _check_black_path(node.left, d, exp)
            r = _check_black_path(node.right, d, exp)
            return l and r
    def _check_red(node, parent):
        if _is_red(node) and _is_red(parent):
            return False
        if not node:
            return True
        l = _check_red(node.left, node)
        r = _check_red(node.right, node)
        return l and r
    d = _max_black_path(root, 0)
    cond1 = _check_black_path(root, 0, d)
    cond2 = _check_red(root, None)
    return cond1 and cond2
