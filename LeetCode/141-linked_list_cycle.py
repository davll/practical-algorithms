# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Tortoise Hare Algorithm
#
# There are two pointers, slow and fast.
#   - slow: move by one step
#   - fast: move by two steps
#
# Theorem:
#     When `slow` and `fast` meet in the list, the list has a cycle
#
# Proof by contradiction:
#     Suppose the list does not have a cycle, the two pointers must meet in the list.
#     `fast` should reach the end of the list before `slow`.
#     Therefore, the two pointers never meet. QED
#
# Time Complexity: T = O(n)
#
#    For worst case, the tortoise reaches the cycle when the hare has just passed the same location.
#    They will meet at the location in the cycle before the enter of the cycle
#

def check_cycle(head) -> bool:
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if id(slow) == id(fast):
            return True
    return False

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        return check_cycle(head)
