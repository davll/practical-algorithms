# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Hint: Two Pointers

def remove_nth_rev(head, n):
    prev, slow, fast = None, head, head
    for _ in range(n):
        fast = fast.next
    while fast:
        prev, slow = slow, slow.next
        fast = fast.next
    if prev:
        prev.next = slow.next
        return head
    else:
        head = slow.next
        return head

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        return remove_nth_rev(head, n)
