# Segment Tree

# 1. The root represents the whole array A[0:N]
# 2. Each leaf represents a single element A[i]
# 3. The internal nodes represents the union of elementary intervals A[i:j]

import math

class SegmentTree:
    def __init__(self, arr):
        n = len(arr)
        ns = 2 * (2 ** int(math.ceil(math.log2(n)))) - 1
        st = [None] * ns
        def fill_data(ss, se, si):
            # check if arr[ss:se] is a one-element array
            if se - ss == 1:
                st[si] = arr[ss]
            else:
                mid = (ss + se-1) // 2
                a1 = fill_data(ss, mid+1, si * 2 + 1)
                a2 = fill_data(mid+1, se, si * 2 + 2)
                st[si] = a1 + a2
            return st[si]
        fill_data(0, n, 0)
        self.storage = st
        self.n = n
    # sum of A[qs:qe]
    def sum(self, qs, qe):
        st, n = self.storage, self.n
        def find_sum(ss, se, qs, qe, si):
            if qs <= ss and qe >= se:
                return st[si]
            if se <= qs or ss >= qe:
                return 0
            mid = (ss + se-1) // 2
            a1 = find_sum(ss, mid+1, qs, qe, 2 * si + 1)
            a2 = find_sum(mid+1, se, qs, qe, 2 * si + 2)
            return a1 + a2
        return find_sum(0, n, qs, qe, 0)
    # update A[i]
    def update(self, i, val):
        st, n = self.storage, self.n
        def find_update(ss, se, i, diff, si):
            if i < ss or i >= se:
                return
            st[si] += diff
            if se - ss > 1:
                mid = (ss + se-1) // 2
                find_update(ss, mid+1, i, diff, 2 * si + 1)
                find_update(mid+1, se, i, diff, 2 * si + 2)
        find_update(0, n, i, val, 0)


# References:
# https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/
# https://www.geeksforgeeks.org/segment-tree-set-1-range-minimum-query/

if __name__ == "__main__":
    pass
