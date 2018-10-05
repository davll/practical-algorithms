# https://www.hackerrank.com/challenges/maximum-subarray-sum/problem

from sys import stdin, stdout, stderr

def maximumSum(n, arr, m):
    # compute prefix sum
    # O(n)
    prefix = arr[:]
    for i in range(1, n):
        prefix[i] = (prefix[i] + prefix[i-1]) % m
    # O(n^2)
    result = max(max(prefix), max(arr))
    bst = RedBlackTree()
    #stderr.write("prefix = {s}\n".format(s=' '.join(map(str, prefix))))
    for i in range(n):
        bst.insert(prefix[i])
        #stderr.write("bst[{i}] = {s}\n".format(i=i, s=' '.join(map(lambda x: str(x.key), bt_inorder(bst.root)))))
        # naive search => O(n^2)
        #for j in range(i):
        #    if prefix[i] < prefix[j]:
        #        modu = (prefix[i] - prefix[j] + m) % m
        #        stderr.write('p[{i}] = {pi}, p[{j}] = {pj}, modulo = {m}\n'.format(i=i, j=j, pi=prefix[i], pj=prefix[j], m=modu))
        #        result = max(result, modu)
        # BST search => O(nlogn)
        this = bst_search(bst.root, prefix[i])
        succ = bst_inorder_succ(bst.root, this)
        if succ is not None:
            modu = (prefix[i] - succ.key + m) % m
            #stderr.write('suss[{i}] = {s}, modulo = {m}\n'.format(i=i, s=succ.key, m=modu))
            result = max(result, modu)
    return result

def main():
    for _ in range(int(stdin.readline().rstrip())):
        n, m = map(int, stdin.readline().rstrip().split())
        a = list(map(lambda x: int(x) % m, stdin.readline().rstrip().split()))
        assert len(a) == n
        ans = maximumSum(n, a, m)
        stdout.write(str(ans) + '\n')

class RedBlackTree:
    def __init__(self):
        self._root = None
    @property
    def root(self):
        return self._root
    def insert(self, key):
        self._root = _insert(self._root, key)
        self._root.black = True

class Node:
    def __init__(self, key, value, black=False):
        self.key = key
        self.value = value
        self.black = black
        self.left = None
        self.right = None

def _is_black(node):
    return node is None or node.black

def _is_red(node):
    return not _is_black(node)

def _need_maintain(node):
    return _is_red(node) and (_is_red(node.left) or _is_red(node.right))

def _recolor(root):
    root.left.black = True
    root.right.black = True
    root.black = False

def _insert(root, key):
    if root is None:
        return Node(key, 1)
    if key == root.key:
        root.value += 1
        return root
    elif key < root.key:
        root.left = _insert(root.left, key)
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
        root.right = _insert(root.right, key)
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

def bst_search(root, key):
    while root is not None and root.key != key:
        if key < root.key:
            root = root.left
        else:
            root = root.right
    return root

def bt_inorder(root):
    if root is None:
        return
    yield from bt_inorder(root.left)
    yield root
    yield from bt_inorder(root.right)

def bst_inorder_succ(root, node):
    if node is None:
        return None
    if node.right is not None:
        return bt_leftmost(node.right)
    succ = None
    while root is not None:
        if node.key < root.key:
            succ = root
            root = root.left
        elif node.key > root.key:
            root = root.right
        else:
            break
    return succ

#
#     ROOT             R
#    /   \            / \
#   A     R    =>  ROOT  C
#        / \       / \
#       B   C     A   B
#
def bt_rotate_left(root):
    assert root is not None
    assert root.right is not None
    r = root.right
    rl = r.left
    root.right = rl
    r.left = root
    return r

#
#      ROOT          L
#     /   \         / \
#    L     C   =>  A   ROOT
#   / \               /   \
#  A   B             B     C
#
def bt_rotate_right(root):
    assert root is not None
    assert root.left is not None
    l = root.left
    lr = l.right
    root.left = lr
    l.right = root
    return l

def bt_leftmost(root):
    if root is None:
        return None
    while root.left is not None:
        root = root.left
    return root

if __name__ == "__main__":
    main()
