def reverse_list(head, m, n):
    prev, curr = None, head
    for _ in range(m-1):
        prev, curr = curr, curr.next
    top, bottom = None, curr
    for _ in range(n-m+1):
        tmp = curr.next
        curr.next = top
        top, curr = curr, tmp
    if bottom:
        bottom.next = curr
    if prev:
        prev.next = top
    else:
        head = top
    return head

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        return reverse_list(head, m, n)
