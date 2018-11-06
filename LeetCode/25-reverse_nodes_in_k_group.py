# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        prev, curr = None, head
        while curr:
            subhead, subtail = curr, curr
            for _ in range(k-1):
                if subtail.next:
                    subtail = subtail.next
                else:
                    return head
            curr = subtail.next
            subtail.next = None
            top = None
            while subhead:
                tmp = subhead.next
                subhead.next = top
                top = subhead
                subhead = tmp
            if prev:
                prev.next = top
            else:
                head = top
            prev = top
            while prev.next:
                prev = prev.next
            prev.next = curr
        return head
