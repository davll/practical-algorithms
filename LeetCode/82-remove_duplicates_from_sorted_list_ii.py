# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def dedup_v1(head):
    result_head = tail = ListNode('dummy')
    while head:
        if head.next and head.val == head.next.val:
            # duplicates detected !
            x = head.val
            while head and head.val == x:
                head = head.next
        else:
            tmp, head = head, head.next
            tmp.next = None
            tail.next = tmp
            tail = tmp
    return result_head.next

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return dedup_v1(head)
