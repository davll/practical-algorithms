# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from heapq import heappush, heappop, heapify

class Element:
    def __init__(self, ls):
        self.node = ls
        self.next = ls.next
        ls.next = None
    def __eq__(self, other):
        return self.node.val == other.node.val
    def __lt__(self, other):
        return self.node.val < other.node.val

def merge_lists(lists):
    queue = list(map(Element, filter(bool, lists)))
    heapify(queue)
    head = tail = None
    while queue:
        e = heappop(queue)
        if e.next:
            heappush(queue, Element(e.next))
        node = e.node
        if tail:
            tail.next = node
            tail = node
        else:
            head = tail = node
    return head

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        return merge_lists(lists)
