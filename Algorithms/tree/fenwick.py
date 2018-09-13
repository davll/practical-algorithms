# Binary Indexed Tree (aka Fenwick Tree)

#
#
#
#

def bit_zeros(n):
    return [0] * (n+1)

def bit_init(n, arr = []):
    bit = bit_zeros()
    for (i, a) in enumerate(arr):
        fenwick_update(bit, n, i, a)
    return bit

# returns sum of A[0:i]
def bit_sum(bit, i):
    result = 0
    # traverse ancestors
    while i > 0:
        # add current element to result
        result += bit[i]
        # move index to parent node in sum view
        i -= i & (-i)
    return result

# update A[i]
def bit_update(bit, n, i, val):
    i = i + 1
    # traverse all ancestors
    while i <= n:
        # add val to current node
        bit[i] += val
        # move index to parent node in update view
        i += i & (-i)

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
