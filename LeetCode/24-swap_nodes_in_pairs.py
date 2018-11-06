# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, curr = None, head
        while curr and curr.next:
            tmp = curr.next.next
            a, b = curr, curr.next
            a.next = tmp
            b.next = curr
            if prev:
                prev.next = b
            else:
                head = b
            prev, curr = a, tmp
        return head
