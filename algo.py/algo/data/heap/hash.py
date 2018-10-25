from collections import namedtuple
import operator as op

Entry = namedtuple('Entry', ['key', 'value'])

class HashHeap:
    def __init__(self, lt=op.lt):
        self._heap = [0]
        self._hash = {}
        self._less = lt
    #
    def __len__(self):
        return self._heap[0]
    def __bool__(self):
        return self._heap[0] > 0
    def __contains__(self, key):
        return key in self._hash
    def __getitem__(self, key):
        return self._heap[self._hash[key]].value
    def __str__(self):
        return "[{h}]".format(h=', '.join(map(lambda e: "{k}: {v}".format(k=e.key, v=e.value), self._heap[1:])))
    #
    @property
    def size(self):
        return self._heap[0]
    #
    def peak(self):
        if self._heap[0] == 0:
            raise IndexError()
        k, v = self._heap[1]
        return (k, v)
    #
    def pop(self):
        if self._heap[0] == 0:
            raise IndexError()
        k, v = self._heap[1]
        self._remove(1)
        return (k, v)
    #
    def add(self, key, value):
        if key in self._hash:
            raise IndexError()
        self._heap.append(Entry(key, value))
        index = self._heap[0] + 1
        self._hash[key] = index
        assert self._heap[index].key == key
        self._heap[0] += 1
        self._heapify(index)
    #
    def remove(self, key):
        if key not in self._hash:
            raise IndexError()
        index = self._hash[key]
        self._remove(index)
    #
    def _remove(self, index):
        last = self._heap[0]
        self._swap(index, last)
        del self._hash[self._heap[last].key]
        self._heap.pop()
        self._heap[0] -= 1
        if index <= self._heap[0]:
            self._heapify(index)
    #
    def _swap(self, a, b):
        h = self._heap
        h[a], h[b] = h[b], h[a]
        self._hash[h[a].key] = a
        self._hash[h[b].key] = b
    #
    def _heapify(self, i):
        n = self._heap[0]
        h = self._heap
        # upward
        while i > 1:
            p = i // 2 # parent
            if self._less(h[p].value, h[i].value):
                self._swap(p, i)
                i = p
            else:
                break
        # downward
        while i <= n:
            l = i * 2     # left child
            r = i * 2 + 1 # right child
            maxi = i
            if l <= n and self._less(h[maxi].value, h[l].value):
                maxi = l
            if r <= n and self._less(h[maxi].value, h[r].value):
                maxi = r
            if maxi != i:
                self._swap(i, maxi)
                i = maxi
            else:
                break
        return i

def MinHashHeap():
    return HashHeap(lt=op.lt)

def MaxHashHeap():
    return HashHeap(lt=op.gt)
