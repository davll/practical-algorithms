# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head, tail, carry = None, None, 0
        while l1 and l2:
            tmp = l1.val + l2.val + carry
            node = ListNode(tmp % 10)
            carry = tmp // 10
            if not tail:
                head = tail = node
            else:
                tail.next = node
                tail = node
            l1, l2 = l1.next, l2.next
        while l1:
            tmp = l1.val + carry
            tail.next = ListNode(tmp % 10)
            tail = tail.next
            carry = tmp // 10
            l1 = l1.next
        while l2:
            tmp = l2.val + carry
            tail.next = ListNode(tmp % 10)
            tail = tail.next
            carry = tmp // 10
            l2 = l2.next
        while carry > 0:
            tail.next = ListNode(carry % 10)
            tail = tail.next
            carry = carry // 10
        return head
