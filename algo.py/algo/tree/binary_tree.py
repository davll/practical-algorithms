# Binary Tree
#
# 1. every node has at most two children

from collections import deque

def bt_preorder(root):
    if not root:
        return
    yield root
    yield from bt_preorder(root.left)
    yield from bt_preorder(root.right)

def bt_inorder(root):
    if not root:
        return
    yield from bt_inorder(root.left)
    yield root
    yield from bt_inorder(root.right)

def bt_postorder(root):
    if not root:
        return
    yield from bt_postorder(root.left)
    yield from bt_postorder(root.right)
    yield root

def bt_levelorder(root):
    if not root:
        return
    q = deque([root])
    while len(q) > 0:
        node = q.popleft()
        assert node
        yield node
        if node.left:
            q.append(node.left)
        if node.right:
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

def bt_preorder_i(root):
    if root is None:
        return
    stack = [root]
    while len(stack) > 0:
        node = stack.pop()
        assert node is not None
        yield node
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)

def bt_inorder_i(root):
    if root is None:
        return
    stack = []
    curr = root
    while True:
        if curr is not None:
            stack.append(curr)
            curr = curr.left
        elif len(stack) > 0:
            curr = stack.pop()
            assert curr is not None
            yield curr
            curr = curr.right
        else:
            break

def bt_postorder_i(root):
    if root is None:
        return
    stack = []
    curr = root
    while True:
        while curr is not None:
            if curr.right is not None:
                stack.append(curr.right)
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        if stack[-1] == curr.right:
            stack.pop()
            stack.append(curr)
            curr = curr.right
        else:
            yield curr
            curr = None
        if len(stack) == 0:
            break

def bt_inorder_morris(root):
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

def bt_leftmost(root):
    if not root:
        return root
    while root.left:
        root = root.left
    return root

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
