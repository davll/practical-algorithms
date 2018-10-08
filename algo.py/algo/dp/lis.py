# Longest Increasing Subsequence
#
# f(i): LIS of A[0:i+1] including A[i]
#
# f(i) = []                                    if i < 0
#      = [A[0]]                                if i = 0
#      = max {
#            f(j) + [A[i]] for j in [0,i)      if A[j] < A[i],
#            [A[i]]
#        }                                     if i > 0
#


# O(n^2)
def lis(A):
    n = len(A)
    sz = [1] * n
    for i in range(1, n):
        l = 1
        for j in range(0, i):
            if A[j] < A[i]:
                l = max(l, sz[j] + 1)
        sz[i] = l
    return max(sz)

# O(nlogn)
def lis2(A):
    n = len(A)
    # After processing A[i]:
    #
    # tail[j]: the index k of the smallest value X[k] such that it exists an
    #       increasing subsequence of length j ending at A[k] on the range
    #       k <= i
    #
    # prev[k]: the index of the predecessor of A[k] in the LIS ending at A[k]
    #
    tail = [0] * (n+1)
    prev = [-1] * n
    # Note: tail[0] is not used
    max_sz = 0
    for i in range(n):
        # binary search for the largest positive j <= max_sz
        # such that A[tail[j]] < A[i]
        #
        # note that A[tail[1]] ... A[tail[L]] is an increasing sequence
        lo, hi = 1, max_sz
        while lo <= hi:
            mid = (lo + hi + 1) // 2
            if A[tail[mid]] < A[i]:
                lo = mid+1
            else:
                hi = mid-1
        # lo is 1 greater than the length of the longest prefix of X[i]
        new_sz = lo
        # the predecessor of A[i] = the last index of the subsequence of length newL-1
        prev[i] = tail[new_sz-1]
        tail[new_sz] = i
        if new_sz > max_sz:
            max_sz = new_sz
    #
    # reconstruct the LIS
    # ls = []
    # k = tail[max_sz]
    # for i in range(max_sz-1, -1, -1):
    #     ls.append(A[k])
    #     k = prev[k]
    # ls.reverse()
    #
    return max_sz
