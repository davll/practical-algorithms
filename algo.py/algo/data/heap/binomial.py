# Binomial Heap

class BinomialHeap:
    def __init__(self):
        self._forest = []
    #
    def peak(self):
        return min(map(lambda t: t.key, filter(bool, self._forest)))
    #
    def pop(self):
        tree = min(filter(bool, self._forest), key=lambda t: t.key)
        tmp = tree.key
        self._forest[tree.order] = None
        for t in _extract_siblings(tree.child):
            self._forest = _forest_append(self._forest, t)
        return tmp
    #
    def push(self, key):
        tree = Node(key)
        self._forest = _forest_append(self._forest, tree)
    #
    def merge(self, other):
        for t in filter(bool, other._forest):
            self._forest = _forest_append(self._forest, t)
        other._forest = []

# Tree node
class Node:
    def __init__(self, key):
        self.key = key
        self.child = None
        self.sibling = None
        self.order = 0

# Note: the sibling list is ordered from high order to low order
def _join_tree(a, b):
    assert a.order == b.order
    assert not a.sibling
    assert not b.sibling
    if a.key > b.key:
        a, b = b, a
    b.sibling = a.child
    a.child = b
    a.order += 1
    return a

def _extract_siblings(tree):
    while tree:
        tmp = tree.sibling
        tree.sibling = None
        yield tree
        tree = tmp

def _forest_append(forest, tree):
    d = tree.order
    while d < len(forest) and forest[d]:
        tree = _join_tree(tree, forest[d])
        forest[d] = None
        d += 1
    if d >= len(forest):
        forest += [None] * (d+1 - len(forest))
    forest[d] = tree
    return forest
