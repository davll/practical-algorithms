# Binomial Heap

# operations
# - create
# - peak
# - push
# - pop
# - decreasing a key => hash?
# - remove node => hash?

class Node:
    def __init__(self, key):
        self.key = key
        self.sibling = None
        self.child = None
        self.parent = None
        self.order = 1

def _merge_tree(root0, root1):
    assert root0.order == root1.order
    assert not root0.parent
    assert not root1.parent
    assert not root0.sibling
    assert not root1.sibling
    if root0.key < root1.key:
        root1.sibling = root0.child
        root0.child = root1
        root1.parent = root0
        root0.order += 1
        return root0
    else:
        root0.sibling = root1.child
        root1.child = root0
        root0.parent = root1
        root1.order += 1
        return root1

# returns (tree, forest)
def _extract_tree(forest):
    tmp, forest.sibling = forest.sibling, None
    return (forest, tmp)

# returns tail
def _push_tree(tail, tree):
    assert tail.order < tree.order
    assert not tail.sibling
    assert not tree.sibling
    tail.sibling = tree
    return tree

def _merge_forest(forest0, forest1):
    dummy = Node(0)
    dummy.order = -1
    head = tail = dummy
    carry = None
    while forest0 and forest1:
        if carry:
            assert carry.order <= forest0.order
            assert carry.order <= forest1.order
            if carry.order < forest0.order and carry.order < forest1.order:
                tail = _push_tree(tail, carry)
                carry = None
        if forest0.order == forest1.order:
            tree0, forest0 = _extract_tree(forest0)
            tree1, forest1 = _extract_tree(forest1)
            if carry:
                tail = _push_tree(tail, carry)
            carry = _merge_tree(tree0, tree1)
        elif forest0.order < forest1.order:
            tree0, forest0 = _extract_tree(forest0)
            if carry:
                if carry.order < tree0.order:
                    tail = _push_tree(tail, carry)
                    carry = tree0
                else:
                    carry = _merge_tree(tree0, carry)
            else:
                tail = _push_tree(tail, tree0)
        else:
            # TODO
            pass
    if forest0:
        assert tail.order <= forest0.order
        assert not tail.sibling
        tail.sibling = forest0
    elif forest1:
        assert tail.order <= forest1.order
        assert not tail.sibling
        tail.sibling = forest1
    assert head.order < 0
    return head.sibling

def _shiftup(node):
    while node and node.parent and node.key < node.parent.key:
        node.key, node.parent.key = node.parent.key, node.key
        node = node.parent

def _find_min(forest):
    if not forest:
        return None
    result = forest.key
    forest = forest.sibling
    while forest:
        if result > forest.key:
            result = forest.key
        forest = forest.sibling
    return result
