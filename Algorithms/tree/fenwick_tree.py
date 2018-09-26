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

def ft_zeros(n):
    return [0] * n

def ft_init(arr = []):
    ft = ft_zeros(len(arr))
    for (i, a) in enumerate(arr):
        ft_update(ft, i, a)
    return ft

def _lsb(x):
    return x & (-x)

# returns sum of A[0:i+1]
def ft_query(ft, i):
    i = i+1
    result = 0
    # traverse ancestors
    while i > 0:
        # add current element to result
        result += ft[i-1]
        # move index to parent node in sum view
        i -= _lsb(i)
    return result

# update A[i]
def ft_update(ft, i, val):
    n, i = len(ft), i+1
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

if __name__ == "__main__":
    import unittest
    class TestFenwick1D(unittest.TestCase):
        def test_4_init(self):
            arr = [10, 5, 23, 6]
            ft = ft_init(arr)
            self.assertListEqual(ft, [10, 15, 23, 44])
        def test_4_query(self):
            arr = [10, 5, 23, 6]
            ft = ft_init(arr)
            q = [ft_query(ft, i) for i in range(4)]
            self.assertListEqual(q, [10, 15, 38, 44])
        def test_4_update(self):
            arr = [10, 5, 23, 6]
            ft = ft_init(arr)
            ft_update(ft, 0, 4)
            q = [ft_query(ft, i) for i in range(4)]
            self.assertListEqual(q, [14, 19, 42, 48])
            ft_update(ft, 1, 1)
            q = [ft_query(ft, i) for i in range(4)]
            self.assertListEqual(q, [14, 20, 43, 49])
            ft_update(ft, 2, 3)
            q = [ft_query(ft, i) for i in range(4)]
            self.assertListEqual(q, [14, 20, 46, 52])
            ft_update(ft, 3, 5)
            q = [ft_query(ft, i) for i in range(4)]
            self.assertListEqual(q, [14, 20, 46, 57])
        def test_4_update_neg(self):
            arr = [10, 5, 23, 6]
            ft = ft_init(arr)
            ft_update(ft, 0, -4)
            q = [ft_query(ft, i) for i in range(4)]
            self.assertListEqual(q, [6, 11, 34, 40])
        def test_11(self):
            arr = [68, 94, 79, 80, 88, 69, 14, 28, 17, 78, 70]
            n = len(arr)
            pre = arr[:]
            for i in range(1,n):
                pre[i] += pre[i-1]
            ft = ft_init(arr)
            q = [ft_query(ft, i) for i in range(n)]
            self.assertListEqual(q, pre)
    unittest.main()
