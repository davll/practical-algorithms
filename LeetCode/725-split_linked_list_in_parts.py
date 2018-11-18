# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def ll_size(root):
    n = 0
    while root:
        n += 1
        root = root.next
    return n

# (left, right)
def ll_split(root, k):
    head = tail = ListNode('dummy')
    for _ in range(k):
        if not root:
            break
        tmp, root = root, root.next
        tmp.next = None
        tail.next = tmp
        tail = tmp
    return (head.next, root)

class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        n = ll_size(root)
        base = n // k
        extra = n % k
        result = []
        for i in range(k):
            tmp, root = ll_split(root, base + int(i < extra))
            result.append(tmp)
        return result
