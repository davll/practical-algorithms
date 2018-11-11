# https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def _compute_length(head):
    n = 0
    while head:
        n = n + 1
        head = head.next
    return n

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        n = _compute_length(head)
        slow = fast = head
        for _ in range(k % n):
            if fast.next:
                fast = fast.next
            else:
                fast = head
        while fast.next:
            fast = fast.next
            slow = slow.next
        fast.next = head
        head, slow.next = slow.next, None
        return head
