# Binary Search Tree
#
# 1. the key in each node >= any keys in the left sub-tree
# 2. the key in each node <= any keys in the right sub-tree
# 3. the leaves contain no key

class BinarySearchTree:
    def __init__(self):
        self._root = None
    @property
    def root(self):
        return self._root
    #
    def __contains__(self, key):
        return _search(self._root, key) is not None
    def __getitem__(self, key):
        node = _search(self._root, key)
        if node is None:
            raise IndexError()
        return node.value
    def __setitem__(self, key, value):
        self.insert(key, value)
    def __delitem__(self, key):
        self.remove(key)
    def insert(self, key, value):
        self._root = _insert(self._root, key, value)
    def remove(self, key):
        self._root = _remove(self._root, key)
    def preorder_traverse(self, visit):
        _preorder_traverse(self._root, visit)
    def inorder_traverse(self, visit):
        _inorder_traverse(self._root, visit)
    def postorder_traverse(self, visit):
        _postorder_traverse(self._root, visit)

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

def _search(root, key):
    if root is None or key == root.key:
        return root
    elif key < root.key:
        return _search(root.left, key)
    else: # key > root.key
        return _search(root.right, key)

def _insert(root, key, value):
    if root is None:
        # return a new node if the tree is empty
        return Node(key, value)
    elif key < root.key:
        # recurse down left subtree
        root.left = _insert(root.left, key)
    elif key > root.key:
        # recurse down right subtree
        root.right = _insert(root.right, key)
    elif key == root.key:
        # update value
        root.value = value
    # return the (unchanged) node
    return root

def _remove(root, key):
    if root is None:
        raise IndexError()
    elif key < root.key:
        root.left = _remove(root.left, key)
    elif key > root.key:
        root.right = _remove(root.right, key)
    else: # key == root.key
        # root with only one child or no child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        # root with two children:
        # 1. find inorder successor
        tmp = root.right
        if tmp.left is not None:
            tmp = tmp.left
        # 2. replace the content of root node
        root.key, root.value = tmp.key, tmp.value
        # 3. delete the inorder successor
        root.right = _remove(tmp.right, tmp.key)
    return root

def _preorder_traverse(root, visit):
    if root is not None:
        visit(root.key, root.value)
        _preorder_traverse(root.left, visit)
        _preorder_traverse(root.right, visit)

def _inorder_traverse(root, visit):
    if root is not None:
        _inorder_traverse(root.left, visit)
        visit(root.key, root.value)
        _inorder_traverse(root.right, visit)

def _postorder_traverse(root, visit):
    if root is not None:
        _postorder_traverse(root.left, visit)
        _postorder_traverse(root.right, visit)
        visit(root.key, root.value)

def reconstruct_from_preorder(key_value_pairs):
    raise NotImplementedError()
