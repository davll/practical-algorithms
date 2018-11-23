# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

def conn_v1(root):
    if not root:
        return
    if root.left:
        root.left.next = root.right
    if root.right and root.next:
        root.right.next = root.next.left
    conn_v1(root.left)
    conn_v1(root.right)

# input is a perfect binary tree
#   1) all leaves are at the same level
#   2) every branch node has two children
#
# BFS-like iteration
#
def conn_v2(root):
    if not root:
        return
    first = root
    while first.left:
        curr = first
        while curr:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
            curr = curr.next
        first = first.left

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        conn_v2(root)
