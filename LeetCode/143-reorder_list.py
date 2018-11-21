# https://leetcode.com/problems/reorder-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def length(head):
    n = 0
    while head:
        head = head.next
        n += 1
    return n

def take_n(head, n):
    prev, curr = None, head
    while curr and n > 0:
        prev, curr = curr, curr.next
        n -= 1
    if prev:
        prev.next = None
    return (head, curr)

def reverse(head):
    result = None
    while head:
        tmp, head = head, head.next
        tmp.next = result
        result = tmp
    return result

def pop_head(head):
    tmp, head = head, head.next
    tmp.next = None
    return (tmp, head)

def interleave(a, b):
    head = tail = ListNode('dummy')
    while a and b:
        ta, a = pop_head(a)
        tb, b = pop_head(b)
        ta.next = tb
        tail.next = ta
        tail = tb
    if a:
        tail.next = a
    elif b:
        tail.next = b
    return head.next

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        n = length(head)
        left, right = take_n(head, (n+1) // 2)
        right = reverse(right)
        interleave(left, right)
