# https://leetcode.com/problems/sort-list/description/
# https://leetcode.com/problems/sort-list/discuss/166324/c++-and-java-legit-solution.-O(nlogn)-time-and-O(1)-space!-No-recursion!-With-detailed-explaination
# https://leetcode.com/problems/sort-list/discuss/195646/28ms-C++-no-recursion-O(1)-extra-space-cost-merge-sort

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def _take(ls):
    # List -> (Node, List)
    tmp = ls.next
    ls.next = None
    return (ls, tmp)

def _merge(l1, l2):
    head, tail = None, None
    # initialise head and tail
    if l1 and (not l2 or l1.val <= l2.val):
        head, l1 = _take(l1)
    elif l2 and (not l1 or l1.val > l2.val):
        head, l2 = _take(l2)
    tail = head
    # merge
    while l1 and l2:
        if l1.val <= l2.val:
            node, l1 = _take(l1)
            tail.next = node
        else: #l1.val > l2.val
            node, l2 = _take(l2)
            tail.next = node
        tail = tail.next
    if l1:
        tail.next = l1
    if l2:
        tail.next = l2
    return head

def _split(ls):
    assert ls
    prev, slow, fast = None, ls, ls
    while fast and fast.next:
        fast = fast.next.next
        prev, slow = slow, slow.next
    if prev:
        prev.next = None
    return (ls, slow)

# log(n) space
def merge_sort_v1(head):
    if not head or not head.next:
        return head
    l1, l2 = map(merge_sort_v1, _split(head))
    return _merge(l1, l2)

# constant space
def merge_sort_v2(head):
    raise NotImplementedError()

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return merge_sort_v1(head)
