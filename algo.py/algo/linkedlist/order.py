from . import Node, pop_head, length, take_n

def merge_sorted(a, b):
    head = tail = Node('dummy')
    while a and b:
        if a.value < b.value:
            t, a = pop_head(a)
        else:
            t, b = pop_head(b)
        tail.next = t
        tail = t
    if a:
        tail.next = a
    elif b:
        tail.next = b
    return head.next

def mergesort(head):
    n = length(head)
    step = 1
    while head and step < n:
        tmp_head = tmp_tail = Node('dummy')
        while head:
            a, head = take_n(head, step)
            b, head = take_n(head, step)
            t = merge_sorted(a, b)
            tmp_tail.next = t
            while tmp_tail.next:
                tmp_tail = tmp_tail.next
        head = tmp_head.next
        step = step * 2
    return head

def reverse(head):
    result = None
    while head:
        tmp, head = head, head.next
        tmp.next = result
        result = tmp
    return result

def interleave(a, b):
    head = tail = Node('dummy')
    while a and b:
        ta, a = pop_head(a)
        tb, b = pop_head(b)
        ta.next = tb
        tail.next = ta
        tail = tb
    if a:
        tail.next = a
    elif b:
        tail.next = b
    return head.next
