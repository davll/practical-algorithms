# https://leetcode.com/problems/copy-list-with-random-pointer/description/

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

from collections import deque

def clone_v1(head):
    table = {}
    queue = deque([head])
    # create new nodes
    while queue:
        old = queue.popleft()
        if not old or id(old) in table:
            continue
        new = RandomListNode(old.label)
        new.next = old.next
        new.random = old.random
        table[id(old)] = new
        if new.next and id(new.next) not in table:
            queue.append(new.next)
        if new.random and id(new.random) not in table:
            queue.append(new.random)
    # relocate pointers
    for node in table.values():
        if node.next:
            node.next = table[id(node.next)]
        if node.random:
            node.random = table[id(node.random)]
    #
    return table[id(head)]

def clone_v2(head):
    # interleave original and cloned nodes
    curr = head
    while curr:
        tmp = curr.next
        curr.next = RandomListNode(curr.label)
        curr.next.next = tmp
        curr = tmp
    # redirect random pointers of cloned nodes
    curr = head
    while curr:
        cloned = curr.next
        if curr.random:
            cloned.random = curr.random.next
        curr = cloned.next
    # separate original and cloned nodes
    curr = head
    cloned_head = cloned_tail = None
    while curr:
        cloned = curr.next
        curr.next = cloned.next
        curr = curr.next
        cloned.next = None
        if cloned_tail:
            cloned_tail.next = cloned
            cloned_tail = cloned
        else:
            cloned_head = cloned_tail = cloned
    return cloned_head

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        return clone_v2(head)
