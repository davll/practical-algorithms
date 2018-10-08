class Node:
    def __init__(self, val, next = None):
        self.value = val
        self.next = next

# Floyd's Tortoise and Hare Algorithm
def detect_cycle(head):
    if not head:
        return False
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if id(slow) == id(fast):
            return True
    return False

def items(head):
    while head:
        yield head.value
        head.next

def find_merge_point(head1, head2):
    p1, p2 = head1, head2
    while id(p1) != id(p2):
        p1, p2 = p1.next, p2.next
        if not p1:
            p1 = head2
        if not p2:
            p2 = head1
    return p1
