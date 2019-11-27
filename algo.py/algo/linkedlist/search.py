from . import Node

def detect_cycle(head) -> bool:
    """
    Floyd's Tortoise and Hare Algorithm
    """
    if not head:
        return False
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if id(slow) == id(fast):
            return True
    return False

def find_merge_point(h1, h2):
    p1, p2 = h1, h2
    while p1 and p2 and id(p1) != id(p2):
        p1, p2 = p1.next, p2.next
        if not p1:
            p1, h2 = h2, None
        if not p2:
            p2, h1 = h1, None
    return p1
