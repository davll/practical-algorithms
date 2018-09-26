# Binary Indexed Tree (aka Fenwick Tree)

#
# =======================================
#
# 1D Binary Index Tree
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
#  
#
#  1 2 3 4 5 6 7 8 9 A B C D E F
#
# https://visualgo.net/bn/fenwicktree

def ft_init(n, arr = []):
    assert n >= len(arr)
    ft = [0] * n
    for (i, a) in enumerate(arr):
        ft_update(bit, n, i, a)
    return bit

def _lsb(x):
    return x & (-x)

# returns sum of A[0:i]
def ft_sum(ft, i):
    result = 0
    # traverse ancestors
    while i > 0:
        # add current element to result
        result += ft[i-1]
        # move index to parent node in sum view
        i -= _lsb(i)
    return result

# update A[i]
def ft_update(ft, n, i, val):
    i = i + 1
    # traverse all ancestors
    while i <= n:
        # add val to current node
        ft[i-1] += val
        # move index to parent node in update view
        i += _lsb(i)

#
# =======================================
#
# 2D Binary Index Tree
#

def bit2d_zeros(m, n):
    return [[0] * (n+1) for _ in range(m+1)]

# sum of A[0:i,0:j]
def bit2d_sum(bit, i, j):
    result, s_j = 0, j
    while i > 0:
        j = s_j
        while j > 0:
            result += bit[i][j]
            j -= j & (-j)
        i -= i & (-i)
    return result

# update A[i,j]
def bit2d_update(bit, i, j, val):
    m, n, s_j = len(bit), len(bit[0]), j
    while i <= m:
        j = s_j
        while j <= n:
            bit[i][j] += val
            j += j & (-j)
        i += i & (-i)

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
