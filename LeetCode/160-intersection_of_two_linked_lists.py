# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def intersect(A, B):
    a, b = A, B
    while a and b and id(a) != id(b):
        if a.next:
            a = a.next
        else:
            a = B
            B = None
        if b.next:
            b = b.next
        else:
            b = A
            A = None
    if a and b and id(a) == id(b):
        return a
    else:
        return None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        return intersect(headA, headB)
