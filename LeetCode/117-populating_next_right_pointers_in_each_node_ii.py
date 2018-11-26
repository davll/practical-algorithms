# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

def left_child(root):
    if not root:
        return None
    while root:
        if root.left:
            return root.left
        elif root.right:
            return root.right
        root = root.next
    return None

def conn_v1(root):
    if not root:
        return
    nc = left_child(root.next)
    if root.left:
        root.left.next = root.right or nc
    if root.right:
        root.right.next = nc
    conn_v1(root.right)
    conn_v1(root.left)

def conn_v2(root):
    pass

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        return conn_v1(root)
