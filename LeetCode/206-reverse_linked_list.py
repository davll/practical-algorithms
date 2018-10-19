# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def reverse_list(head):
    curr = None
    while head:
        tmp = head.next
        head.next = curr
        curr, head = head, tmp
    return curr

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return reverse_list(head)
