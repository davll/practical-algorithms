# https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem

# Hint: Floyd's Tortoise and Hare

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    if not head:
        return False
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if id(slow) == id(fast):
            return True
    return False
