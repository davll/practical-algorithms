# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def dedup_list(head):
    prev, curr = None, head
    while curr:
        if prev and prev.val == curr.val:
            # skip curr
            prev.next = curr.next
            curr = curr.next
        else:
            prev, curr = curr, curr.next
    return head

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return dedup_list(head)
