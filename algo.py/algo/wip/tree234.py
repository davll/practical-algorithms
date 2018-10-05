from itertools import chain

MAX_DEGREE = 4

class Tree234:
    def __init__(self):
        self._root = None
    #
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
        node, pos = node
        return node.values[pos]
    def __setitem__(self, key, value):
        self.insert(key, value)
    def insert(self, key, value):
        node = _insert(self._root, key, value)
        if node.degree > MAX_DEGREE:
            node = _split(node)
        self._root = node
    def get(self, key, default_value=None):
        node = _search(self._root, key)
        if node is None:
            if default_value is not None:
                return default_value
            else:
                raise IndexError()
        else:
            node, pos = node
            return node.values[pos]
    #
    def inorder(self):
        yield from _inorder(self._root)

class Node:
    def __init__(self, keys, values):
        self.keys = tuple(keys)
        self.values = list(values)
        assert len(self.keys) == len(self.values)
        self.links = [None] * (len(self.keys) + 1)
    #
    @property
    def degree(self):
        return len(self.links)

def _search(root, key):
    if root is None:
        return None
    else:
        for i, k in enumerate(root.keys):
            if key < k:
                return _search(root.links[i], key)
            elif key == k:
                return (root, i)
        return _search(root.links[-1], key)

def _insert(root, key, value):
    if root is None:
        return Node([key], [value])
    else:
        pos = root.degree - 1
        for i, k in enumerate(root.keys):
            if key < k:
                pos = i
                break
            elif key == k:
                root.values[i] = value
                return root
        if root.links[pos] is None:
            node = Node([key], [value])
            return _merge(root, pos, node)
        else:
            node = root.links[pos]
            root.links[pos] = None
            node = _insert(node, key, value)
            if node.degree <= MAX_DEGREE:
                root.links[pos] = node
                return root
            else:
                assert node.degree == MAX_DEGREE+1
                node = _split(node)
                return _merge(root, pos, node)

def _split(root):
    assert root.degree >= 4
    # deg = 4 -> k = 1
    #
    #                   M(1)
    #  (0 1 2)         /   \
    #  / / \ \   => L(0)   R(2)
    #               /  \   /  \
    #
    k = (root.degree-1) // 2
    lnode = Node(root.keys[:k], root.values[:k])
    mnode = Node([root.keys[k]], [root.values[k]])
    rnode = Node(root.keys[k+1:], root.values[k+1:])
    lnode.links[:] = root.links[:k+1]
    rnode.links[:] = root.links[k+1:]
    mnode.links[0] = lnode
    mnode.links[1] = rnode
    return mnode

def _merge(root, pos, node):
    assert root.links[pos] is None
    assert node.degree == 2
    #
    #  (0 2) + (1) = (0 1 2)
    #  / | \   / \   / / \ \
    #
    i, n = pos, node.degree
    keys = chain(root.keys[:i], node.keys[:], root.keys[i:])
    values = chain(root.values[:i], node.values[:], root.values[i:])
    fused = Node(keys, values)
    # fused.degree = root.degree + node.degree - 1
    fused.links[:i] = root.links[:i]
    fused.links[i:i+n] = node.links[:]
    fused.links[i+n:] = root.links[i+1:]
    return fused

def _inorder(root):
    if root is None:
        return
    for i, (k, v) in enumerate(zip(root.keys, root.values)):
        yield from _inorder(root.links[i])
        yield (k, v)
    yield from _inorder(root.links[-1])

if __name__ == "__main__":
    t = Tree234()
    keys = [3, 1, 5, 4, 2, 9, 10, 8, 7, 6]
    vals = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for k, v in zip(keys, vals):
        t[k] = v
    print(' '.join(map(lambda x: str(x[0]), t.inorder())))
