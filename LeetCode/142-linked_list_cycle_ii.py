# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def detect_cycle(head):
    slow, fast = head, head
    cycle = False
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if id(slow) == id(fast):
            cycle = True
            break
    if not cycle:
        return None
    fast = head
    while id(slow) != id(fast):
        fast = fast.next
        slow = slow.next
    return slow

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return detect_cycle(head)
