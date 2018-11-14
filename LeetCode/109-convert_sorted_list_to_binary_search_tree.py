# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def list_size(head):
    n = 0
    while head:
        n += 1
        head = head.next
    return n

# returns (tree, head)
def construct(head, start, end):
    if start > end:
        return (None, head)
    mid = (start + end) // 2
    # construct left subtree
    left, head = construct(head, start, mid-1)
    # extract node from list
    assert head
    node = head
    head = head.next
    node.next = None
    # construct right subtree
    right, head = construct(head, mid+1, end)
    # compose tree
    root = TreeNode(node.val)
    root.left = left
    root.right = right
    return (root, head)

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        n = list_size(head)
        t, _ = construct(head, 0, n-1)
        return t
