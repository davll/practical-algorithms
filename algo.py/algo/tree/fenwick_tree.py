# Binary Indexed Tree (aka Fenwick Tree)

#
# =======================================
#
# 1D Binary Index Tree
#
# Contraints:
#
# - if i = pow of 2, ft[i] = sum[0:i]
#
# Update view:
#
#          ------x     --x   x x
#         /   / /     / /   /
#      --x   x x     x x   x
#     / /   /       /
#    x x   x       x
#   /
#  x
#
#  1 2 3 4 5 6 7 8 9 A B C D E F
#
# Sum view:
#
#  x x   x--     x------
#     \   \ \     \ \   \
#      x   x x     x x   x--
#             \       \   \ \
#              x       x   x x
#                             \
#                              x
#
#  1 2 3 4 5 6 7 8 9 A B C D E F
#
#
#
# https://visualgo.net/bn/fenwicktree

from typing import TypeVar, List, Sequence, Generic

T = TypeVar('T', int, float)

class FenwickTree1D(Generic[T]):
    def __init__(self, n: int) -> None:
        self._size = n
        self._tree: List[T] = [0] * n
    def __len__(self):
        return self._size
    # returns A[0] + ... + A[i]
    def query(self, i: int) -> T:
        i = i + 1
        result: T = 0
        # traverse ancestors
        while i > 0:
            # add current element to result
            result += self._tree[i-1]
            # move index to parent node in sum view
            i -= _lsb(i)
        return result
    # update A[i]
    def update(self, i: int, delta: T) -> None:
        n, i = len(self._tree), i+1
        # traverse all ancestors
        while i <= n:
            # add val to current node
            self._tree[i-1] += delta
            # move index to parent node in update view
            i += _lsb(i)

def _lsb(x: int) -> int:
    return x & (-x)

class FenwickTree2D(Generic[T]):
    def __init__(self, m: int, n: int) -> None:
        self._rows = m
        self._cols = n
        self._tree: List[List[T]] = [[0] * n for _ in range(m)]
    @property
    def rows(self) -> int:
        return self._rows
    @property
    def cols(self) -> int:
        return self._cols
    # update A[i][j]
    def update(self, i, j, delta):
        m, n = self.rows, self.cols
        i, j = i+1, j+1
        i0, j0 = i, j
        while i <= m:
            j = j0
            while j <= n:
                self._tree[i-1][j-1] += delta
                j += _lsb(j)
            i += _lsb(i)
    # returns A[0][0] + ... + A[0][j] +
    #           ...            ...    +
    #         A[i][0] + ... + A[i][j]
    def query(self, i, j):
        i, j = i+1, j+1
        i0, j0 = i, j
        result = 0
        while i > 0:
            j = j0
            while j > 0:
                result += self._tree[i-1][j-1]
                j -= _lsb(j)
            i -= _lsb(i)
        return result

# References:
#
# https://www.hackerrank.com/topics/binary-indexed-tree
# https://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/
# https://www.geeksforgeeks.org/two-dimensional-binary-indexed-tree-or-fenwick-tree/
# https://www.geeksforgeeks.org/counting-triangles-in-a-rectangular-space-using-2d-bit/
# https://www.topcoder.com/community/data-science/data-science-tutorials/binary-indexed-trees/
# https://brilliant.org/wiki/fenwick-tree/
# https://www.hackerearth.com/practice/notes/binary-indexed-tree-or-fenwick-tree/
# https://www.hackerearth.com/practice/notes/binary-indexed-tree-made-easy-2/
