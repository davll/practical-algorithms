# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def insertion_sort(head, node):
    if not head:
        return node
    prev, curr = None, head
    while curr:
        if curr.val > node.val:
            node.next = curr
            if prev:
                prev.next = node
                return head
            else:
                return node
        prev, curr = curr, curr.next
    prev.next = node
    node.next = None
    return head

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p, l = head, None
        while p:
            n = p.next
            p.next = None
            l = insertion_sort(l, p)
            p = n
        return l
