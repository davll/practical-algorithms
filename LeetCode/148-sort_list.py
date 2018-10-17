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

def merge_sort(head, n):
    if n == 1 or n == 0:
        return head
    else:
        # split the list
        m = n // 2
        prev, mid = None, head
        for _ in range(0, m):
            prev, mid = mid, mid.next
        prev.next = None
        # recursive down
        l1 = merge_sort(head, m)
        l2 = merge_sort(mid, n - m)
        # merge two sorted lists
        return merge_lists(l1, l2)

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        n, p = 0, head
        while p != None:
            n, p = n+1, p.next
        return merge_sort(head, n)
