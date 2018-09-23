#!/bin/python3

class BinaryTrie:
    def __init__(self):
        self.value = [None]
        self.left = [-1]
        self.right = [-1]
    def insert(self, code):
        node = 0 # root

def method_naive(arr, queries):
    return [
        max(map(lambda x: x ^ q, arr))
        for q in queries
    ]

def method_trie(arr, queries):
    raise NotImplementedError()

# Complete the maxXor function below.
def maxXor(arr, queries):
    return method_naive(arr, queries)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    m = int(input())
    queries = []
    for _ in range(m):
        queries_item = int(input())
        queries.append(queries_item)
    result = maxXor(arr, queries)
    print('\n'.join(map(str, result)))
