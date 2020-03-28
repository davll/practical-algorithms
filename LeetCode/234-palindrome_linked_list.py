# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def copy_reverse_list(head):
    curr = None
    while head:
        node = ListNode(head.val)
        node.next = curr
        curr, head = node, head.next
    return curr

# T = O(n)
# S = O(n)
def is_palindrome_v1(head):
    tail = copy_reverse_list(head)
    while head and tail:
        if head.val != tail.val:
            return False
        head, tail = head.next, tail.next
    return True

def count_list(head):
    n = 0
    while head:
        n += 1
        head = head.next
    return n

# T = O(n)
# S = O(1)
# it changes input list inplace
def is_palindrome_v2(head):
    n = count_list(head)
    tail = None
    for _ in range(n // 2):
        node, head = head, head.next
        node.next = tail
        tail = node
    if n % 2 == 1:
        head = head.next
    while tail and head:
        if head.val != tail.val:
            return False
        head, tail = head.next, tail.next
    return True

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        return is_palindrome_v2(head)
