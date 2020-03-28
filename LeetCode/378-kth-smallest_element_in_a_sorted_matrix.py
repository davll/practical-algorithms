from heapq import merge, heapify, heappush, heappop

def kth_smallest_v1(mat, k):
    return list(merge(*mat))[k-1]

class FItem:
    def __init__(self, mat, row, idx):
        self.mat = mat
        self.row = row
        self.idx = idx
    @property
    def val(self):
        return self.mat[self.row][self.idx]
    def next(self):
        if self.idx < len(self.mat[self.row])-1:
            return FItem(self.mat, self.row, self.idx+1)
        else:
            return None
    def __lt__(self, other):
        return self.val < other.val
    def __eq__(self, other):
        return self.val == other.val

def kth_smallest_v2(mat, k):
    n = len(mat)
    h = [FItem(mat, r, 0) for r in range(n)]
    heapify(h)
    result = None
    for _ in range(k):
        x = heappop(h)
        result = x.val
        y = x.next()
        if y:
            heappush(h, y)
    return result

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return kth_smallest_v2(matrix, k)
