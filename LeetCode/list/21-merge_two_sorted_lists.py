# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def merge_lists(l1, l2):
    head, tail = None, None
    while l1 and l2:
        if l1.val <= l2.val:
            tmp = l1.next
            l1.next = None
            if tail:
                tail.next = l1
                tail = l1
            else:
                head, tail = l1, l1
            l1 = tmp
        elif l1.val > l2.val:
            tmp = l2.next
            l2.next = None
            if tail:
                tail.next = l2
                tail = l2
            else:
                head, tail = l2, l2
            l2 = tmp
    if l1:
        if tail:
            tail.next = l1
        else:
            head, tail = l1, l1
    elif l2:
        if tail:
            tail.next = l2
        else:
            head, tail = l2, l2
    return head

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return merge_lists(l1, l2)
