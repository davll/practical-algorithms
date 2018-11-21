class Node:
    def __init__(self, val, next = None):
        self.value = val
        self.next = next

def pop_head(head):
    tmp, head.next = head.next, None
    return (head, tmp)

def push_head(head, x):
    return Node(x, head)

def list_items(head):
    while head:
        yield head.value
        head.next

def build_list(items):
    head = tail = Node('dummy')
    for x in items:
        tail.next = Node(x)
        tail = tail.next
    return head.next

def take_half(head):
    prev, slow, fast = None, head, head
    while fast and fast.next:
        fast = fast.next.next
        prev, slow = slow, slow.next
    if prev:
        prev.next = None
    return (head, slow)

def take_n(head, n):
    prev, curr = None, head
    while curr and n > 0:
        prev, curr = curr, curr.next
        n -= 1
    if prev:
        prev.next = None
    return (head, curr)

def length(head):
    n = 0
    while head:
        head = head.next
        n += 1
    return n
