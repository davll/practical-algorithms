# https://leetcode.com/problems/lru-cache/

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._capacity = capacity
        self._storage = {}
        self._head = None
        self._tail = None
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self._storage:
            return -1
        node = self._storage[key]
        self._shift(node)
        return node.value
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = self._storage.get(key)
        if node:
            node.value = value
            self._shift(node)
        else:
            node = Node(key, value)
            self._storage[key] = node
            self._append(node)
            if len(self._storage) > self._capacity:
                node = self._popleft()
                del self._storage[node.key]
    def _shift(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self._head = self._head.next
        if node.next:
            node.next.prev = node.prev
        else:
            self._tail = self._tail.prev
        node.next = node.prev = None
        self._append(node)
    def _append(self, node):
        assert not node.prev
        assert not node.next
        if self._tail:
            self._tail.next = node
            node.prev = self._tail
            self._tail = node
        else:
            self._head = node
            self._tail = node
    def _popleft(self):
        head = self._head
        self._head = self._head.next
        self._head.prev = None
        head.next = None
        if not self._head:
            self._tail = None
        return head

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
