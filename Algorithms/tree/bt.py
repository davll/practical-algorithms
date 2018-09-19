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

# Degenerate/Pathological Tree

# References:
# https://www.geeksforgeeks.org/binary-tree-set-3-types-of-binary-tree/
# http://web.cecs.pdx.edu/~sheard/course/Cs163/Doc/FullvsComplete.html
# http://web.cecs.pdx.edu/~sheard/course/Cs163/Doc/HeapReview.html
# https://en.wikipedia.org/wiki/Binary_tree
# https://en.wikipedia.org/wiki/Binary_search_tree
# https://en.wikipedia.org/wiki/Tree_traversal

from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(root):
    if root is None:
        return
    yield root
    yield from preorder(root.left)
    yield from preorder(root.right)

def inorder(root):
    if root is None:
        return
    yield from inorder(root.left)
    yield root
    yield from inorder(root.right)

def postorder(root):
    if root is None:
        return
    yield from postorder(root.left)
    yield from postorder(root.right)
    yield root

def levelorder(root):
    q = deque([root])
    while len(q) > 0:
        node = q.popleft()
        if node is None:
            continue
        yield node
        q.append(node.left)
        q.append(node.right)

#
#     ROOT             R
#    /   \            / \
#   A     R    =>  ROOT  C
#        / \       / \
#       B   C     A   B
#
def rotate_left(root):
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
def rotate_right(root):
    assert root is not None
    assert root.left is not None
    l = root.left
    lr = l.right
    root.left = lr
    l.right = root
    return l

# TODO: build from preorder and inorder
# TODO: build complete binary tree from preorder and postorder

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    print(str(list(map(lambda x: str(x.value), preorder(root)))))
    print(str(list(map(lambda x: str(x.value), inorder(root)))))
    print(str(list(map(lambda x: str(x.value), postorder(root)))))
    print(str(list(map(lambda x: str(x.value), levelorder(root)))))
    root = rotate_right(root)
    print(str(list(map(lambda x: str(x.value), inorder(root)))))
    print(str(list(map(lambda x: str(x.value), levelorder(root)))))
    root = rotate_left(root)
    print(str(list(map(lambda x: str(x.value), inorder(root)))))
    print(str(list(map(lambda x: str(x.value), levelorder(root)))))

# https://www.cnblogs.com/AnnieKim/archive/2013/06/15/MorrisTraversal.html
# https://github.com/leetcoders/LeetCode/blob/master/BinaryTreeInorderTraversal.h
# https://en.wikipedia.org/wiki/Threaded_binary_tree#The_array_of_Inorder_traversal
# https://www.geeksforgeeks.org/iterative-preorder-traversal/
# https://www.geeksforgeeks.org/iterative-postorder-traversal/
# https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion-and-without-stack/
# https://www.geeksforgeeks.org/morris-traversal-for-preorder/
# https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
