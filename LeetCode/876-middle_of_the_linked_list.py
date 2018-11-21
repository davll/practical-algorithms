# https://leetcode.com/problems/middle-of-the-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def take_half(head):
    prev, slow, fast = None, head, head
    while fast and fast.next:
        fast = fast.next.next
        prev, slow = slow, slow.next
    if prev:
        prev.next = None
    return (head, slow)

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        _, n = take_half(head)
        return n
