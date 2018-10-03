class Tree23:
    def __init__(self):
        self._root = None
    #
    def __contains__(self, key):
        return _search(self._root, key) is not None
    def __getitem__(self, key):
        node, pos = _search(self._root, key)
        if node is None:
            raise IndexError()
        return node.values[pos]
    #
    def __setitem__(self, key, value):
        self.insert(key, value)
    def insert(self, key, value):
        root = _insert(self._root, key, value)
        self._root = _resolve_root(root)

class Node:
    def __init__(self, keys, values):
        self.keys = list(keys)
        self.values = list(values)
        self.links = [None] * (len(self.keys) + 1)
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

def _insert_at(root, pos, key, value):
    if pos == -1:
        root.keys.append(key)
        root.values.append(value)
        root.links.append(None)
    else:
        root.keys = root.keys[:pos] + [key] + root.keys[pos:]
        root.values = root.values[:pos] + [value] + root.values[pos:]
        root.links = root.links[:pos] + [None] + root.links[pos:]

def _resolve(root, pos):
    node = root.links[pos]
    if node.degree < 4:
        return root
    assert node.degree == 4
    # split the node into 3 nodes
    lnode = Node(node.keys[:1], node.values[:1])
    mnode_kv = (node.keys[1], node.values[1])
    rnode = Node(node.keys[2:], node.values[2:])
    lnode.links[:] = node.links[:2]
    rnode.links[:] = node.links[2:]
    _insert_at(root, pos, mnode_kv[0], mnode_kv[1])
    root.links[pos] = lnode
    root.links[pos+1] = rnode
    return root

def _resolve_root(root):
    if root.degree < 4:
        return root
    assert root.degree == 4
    # split the root node into 3 nodes
    lnode = Node(root.keys[:1], root.values[:1])
    mnode = Node(root.keys[1:2], root.values[1:2])
    rnode = Node(root.keys[2:], root.values[2:])
    lnode.links[:] = root.links[:2]
    rnode.links[:] = root.links[2:]
    mnode.links[0] = lnode
    mnode.links[1] = rnode
    return mnode

def _insert(root, key, value):
    if root is None:
        return Node([key], [value])
    else:
        pos = -1
        for i, k in enumerate(root.keys):
            if key < k:
                pos = i
                break
            elif key == k:
                root.values[i] = value
                return root
        if root.links[pos] is None:
            _insert_at(root, pos, key, value)
        else:
            root.links[pos] = _insert(root.links[pos], key, value)
            root = _resolve(root, pos)
        return root
