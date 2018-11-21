# https://leetcode.com/problems/sort-list/description/
# https://leetcode.com/problems/sort-list/discuss/166324/c++-and-java-legit-solution.-O(nlogn)-time-and-O(1)-space!-No-recursion!-With-detailed-explaination
# https://leetcode.com/problems/sort-list/discuss/195646/28ms-C++-no-recursion-O(1)-extra-space-cost-merge-sort

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def _pop_head(ls):
    # List -> (Node, List)
    tmp, ls.next = ls.next, None
    return (ls, tmp)

def _merge(l1, l2):
    head = tail = ListNode('dummy')
    while l1 and l2:
        if l1.val < l2.val:
            tmp, l1 = _pop_head(l1)
        else:
            tmp, l2 = _pop_head(l2)
        tail.next = tmp
        tail = tail.next
    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2
    return head.next

def _merge_to_tail(tail, l1, l2):
    while l1 and l2:
        if l1.val < l2.val:
            tmp, l1 = _pop_head(l1)
        else:
            tmp, l2 = _pop_head(l2)
        tail.next = tmp
        tail = tail.next
    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2
    while tail.next:
        tail = tail.next
    return tail

def _split(ls):
    assert ls
    prev, slow, fast = None, ls, ls
    while fast and fast.next:
        fast = fast.next.next
        prev, slow = slow, slow.next
    if prev:
        prev.next = None
    return (ls, slow)

def _split_n(ls, n):
    prev, curr = None, ls
    while curr and n > 0:
        prev, curr = curr, curr.next
        n -= 1
    if prev:
        prev.next = None
    return (ls, curr)

def _length(ls):
    n = 0
    while ls:
        n += 1
        ls = ls.next
    return n

# log(n) space
def merge_sort_v1(head):
    if not head or not head.next:
        return head
    l1, l2 = map(merge_sort_v1, _split(head))
    return _merge(l1, l2)

# constant space
def merge_sort_v2(head):
    n = _length(head)
    step = 1
    while head and step < n:
        tmp_head = tmp_tail = ListNode('dummy')
        while head:
            a, head = _split_n(head, step)
            b, head = _split_n(head, step)
            tmp_tail = _merge_to_tail(tmp_tail, a, b)
        head = tmp_head.next
        step *= 2
    return head

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return merge_sort_v2(head)
