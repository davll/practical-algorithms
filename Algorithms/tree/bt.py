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

def preorder_traverse(root):
    if root is None:
        return
    yield root
    yield from preorder_traverse(root.left)
    yield from preorder_traverse(root.right)

def inorder_traverse(root):
    if root is None:
        return
    yield from inorder_traverse(root.left)
    yield root
    yield from inorder_traverse(root.right)

def postorder_traverse(root):
    if root is None:
        return
    yield from postorder_traverse(root.left)
    yield from postorder_traverse(root.right)
    yield root

def levelorder_traverse(root):
    q = deque([root])
    while len(q) > 0:
        node = q.popleft()
        if node is None:
            continue
        yield node
        q.append(node.left)
        q.append(node.right)

def is_full(root):
    def check(node):
        if node.left is None:
            if node.right is None:
                return True
            else:
                return False
        elif node.right is None:
            return False
        else:
            return True
    levelorder_traverse(root, check)

# TODO: build from preorder and inorder
# TODO: build complete binary tree from preorder and postorder

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    print(str(list(map(lambda x: str(x.value), preorder_traverse(root)))))
    print(str(list(map(lambda x: str(x.value), inorder_traverse(root)))))
    print(str(list(map(lambda x: str(x.value), postorder_traverse(root)))))
    print(str(list(map(lambda x: str(x.value), levelorder_traverse(root)))))
