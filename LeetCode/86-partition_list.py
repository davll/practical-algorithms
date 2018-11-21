# https://leetcode.com/problems/partition-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def pop_head(head):
    tmp, head = head, head.next
    tmp.next = None
    return (tmp, head)

def partition(head, x):
    left_head = left_tail = ListNode('dummy')
    right_head = right_tail = ListNode('dummy')
    while head:
        tmp, head = pop_head(head)
        if tmp.val < x:
            left_tail.next = tmp
            left_tail = tmp
        else:
            right_tail.next = tmp
            right_tail = tmp
    left_tail.next = right_head.next
    return left_head.next

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        return partition(head, x)
