# https://practice.geeksforgeeks.org/problems/magic-triplets/0

import math

# O(n^3)
def naive(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] >= arr[j]:
                continue
            for k in range(j+1, n):
                if arr[j] < arr[k]:
                    count += 1
    return count

# O(n^2)
def naive2(arr):
    n = len(arr)
    cnt = [0] * n
    for j in range(1,n):
        for i in range(0,j):
            if arr[i] < arr[j]:
                cnt[j] += 1
    result = 0
    for k in range(2,n):
        for j in range(1,k):
            if arr[j] < arr[k]:
                result += cnt[j]
    return result

# O(nlog(maxval))
def fenwick(arr):
    # init BIT
    def bit_zeros(n):
        return [0] * (n+1)
    # sum of A[0:i] (not including A[i])
    def bit_sum(bit, i):
        result = 0
        while i > 0:
            result += bit[i]
            i -= i & (-i)
        return result
    # update A[i]
    def bit_update(bit, n, i, val):
        i = i + 1
        while i <= n:
            bit[i] += val
            i += i & (-i)
    #
    n, maxval = len(arr), max(arr)
    cnt = [0] * n
    bit = bit_zeros(maxval+1)
    for j in range(n):
        x = arr[j]
        c = bit_sum(bit, x)
        bit_update(bit, maxval, x, 1)
        cnt[j] = c
    bit = bit_zeros(maxval+1)
    result = 0
    for k in range(n):
        x = arr[k]
        c = bit_sum(bit, x)
        bit_update(bit, maxval, x, cnt[k])
        result += c
    return result

# O(nlogn)
def fenwick2(arr):
    # convert array
    tmp = dict(map(lambda t: (t[1],t[0]), enumerate(sorted(arr))))
    ls = [tmp[x] for x in arr]
    # call fenwick
    return fenwick(ls)

class SegmentTree:
    def __init__(self, n):
        ns = 2 * (2 ** int(math.ceil(math.log2(n)))) - 1
        st = [0] * ns
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

# O(nlog(maxval))
def segment(arr):
    n, maxval = len(arr), max(arr)
    cnt = [0] * n
    st = SegmentTree(maxval+1)
    for j in range(n):
        x = arr[j]
        c = st.sum(0, x)
        st.update(x, 1)
        cnt[j] = c
    st = SegmentTree(maxval+1)
    result = 0
    for k in range(n):
        x = arr[k]
        c = st.sum(0, x)
        st.update(x, cnt[k])
        result += c
    return result

if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int, input().strip().split()))
        result = segment(arr)
        print(str(result))
