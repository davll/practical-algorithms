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
    def __init__(self, nums: Sequence[T]) -> None:
        n = len(nums)
        self._tree: List[T] = [0] * n
        for i, x in enumerate(nums):
            self.update(i, x)
    # returns sum(A[0:i])
    def query(self, i: int) -> T:
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

#
# =======================================
#
# 2D Binary Index Tree
#

def ft2d_zeros(m, n):
    return [[0] * n for _ in range(m)]

# sum of A[0:i+1,0:j+1]
def ft2d_query(ft, i, j):
    i, j = i+1, j+1
    result, s_j = 0, j
    while i > 0:
        j = s_j
        while j > 0:
            result += ft[i-1][j-1]
            j -= _lsb(j)
        i -= _lsb(i)
    return result

# update A[i,j]
def ft2d_update(ft, i, j, val):
    m, n, i, j, s_j = len(ft), len(ft[0]), i+1, j+1, j+1
    while i <= m:
        j = s_j
        while j <= n:
            ft[i-1][j-1] += val
            j += _lsb(j)
        i += _lsb(i)

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
