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
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def bt_preorder(root):
    if root is None:
        return
    yield root
    yield from bt_preorder(root.left)
    yield from bt_preorder(root.right)

def bt_inorder(root):
    if root is None:
        return
    yield from bt_inorder(root.left)
    yield root
    yield from bt_inorder(root.right)

def bt_postorder(root):
    if root is None:
        return
    yield from bt_postorder(root.left)
    yield from bt_postorder(root.right)
    yield root

def bt_levelorder(root):
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

def bt_inverse(root):
    if root is None:
        return None
    l, r = root.left, root.right
    root.left, root.right = bt_inverse(r), bt_inverse(l)
    return root

def bt_morris_inorder(root):
    curr = root
    while curr is not None:
        if curr.left is None:
            yield curr
            curr = curr.right
        else:
            # find the inorder predecessor of curr
            pre = curr.left
            while pre.right is not None and pre.right != curr:
                pre = pre.right
            # mark current as right child of its inorder predecessor
            if pre.right is None:
                pre.right = curr
                curr = curr.left
            else: # revert the change
                pre.right = None
                yield curr
                curr = curr.right

# TODO: build from preorder and inorder
# TODO: build complete binary tree from preorder and postorder

# https://www.cnblogs.com/AnnieKim/archive/2013/06/15/MorrisTraversal.html
# https://github.com/leetcoders/LeetCode/blob/master/BinaryTreeInorderTraversal.h
# https://en.wikipedia.org/wiki/Threaded_binary_tree#The_array_of_Inorder_traversal
# https://www.geeksforgeeks.org/iterative-preorder-traversal/
# https://www.geeksforgeeks.org/iterative-postorder-traversal/
# https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion-and-without-stack/
# https://www.geeksforgeeks.org/morris-traversal-for-preorder/
# https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
