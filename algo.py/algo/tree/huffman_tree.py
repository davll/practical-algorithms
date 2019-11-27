# Huffman Coding Tree

import heapq
#from ..heap.binary import heap_init, heap_peak, heap_pop, heap_push

class Node:
    def __init__(self, k, f):
        self.key = k
        self.freq = f
        self.left = None
        self.right = None
    def __eq__(self, other):
        assert other is Node
        return self.freq == other.freq
    def __lt__(self, other):
        assert other is Node
        return self.freq < other.freq
    def __gt__(self, other):
        assert other is Node
        return self.freq > other.freq

class HuffmanTree:
    def __init__(self, key_freq_iter):
        # init min-heap
        q = list(map(lambda x: Node(x[0], x[1]), key_freq_iter))
        heapq.heapify(q)
        # repeat until only one element left in heap
        while len(q) > 1:
            # extract two minimum freq nodes
            a = heapq.heappop(q)
            b = heapq.heappop(q)
            # create a node
            x = Node(None, a.f + b.f)
            x.left = a
            x.right = b
            # push to min-heap
            heapq.heappush(q, x)
        # finished, store root node
        self.root = q[0]
    #
    def codes(self):
        table = {}
        def traverse(node, c):
            if node.left:
                traverse(node.left, (c << 1))
            if node.right:
                traverse(node.right, ((c << 1) | 1))
            if node.key != None:
                assert node.left == None
                assert node.right == None
                table[node.key] = c
        traverse(self.root, 0)
        return table
    #
    def decode(self, s):
        t = self.root
        decoded = []
        for x in map(int, s):
            assert x == 0 or x == 1
            if x == 0:
                t = t.left
            elif x == 1:
                t = t.right
            # check if the node is a leaf
            if not t.left and not t.right:
                decoded.append(t.key)
                t = self.root
        return decoded

# References:
# https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/

if __name__ == "__name__":
    pass
