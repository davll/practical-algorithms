# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def _take(ls):
    # List -> (Node, List)
    tmp = ls.next
    ls.next = None
    return (ls, tmp)

def merge_lists(l1, l2):
    head, tail = None, None
    # initialise head and tail
    if l1 and (not l2 or l1.val <= l2.val):
        head, l1 = _take(l1)
    elif l2 and (not l1 or l1.val > l2.val):
        head, l2 = _take(l2)
    tail = head
    # merge
    while l1 and l2:
        if l1.val <= l2.val:
            node, l1 = _take(l1)
            tail.next = node
        else: #l1.val > l2.val
            node, l2 = _take(l2)
            tail.next = node
        tail = tail.next
    if l1:
        tail.next = l1
    if l2:
        tail.next = l2
    return head

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return merge_lists(l1, l2)
