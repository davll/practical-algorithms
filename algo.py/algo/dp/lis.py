# Longest Increasing Subsequence

# Idea: Dynamic Programming
#
# T = O(n^2)
#
# F[i] = Length of LIS ends at A[i]
#
# F[0] = 1
#
# F[i] = max { F[j]+1 } for all j < i st. A[j] < A[i]
#      = 1              if no such j exists
#
def lis_v1(A):
    n = len(A)
    F = [1] * n
    for i in range(1, n):
        F[i] = max((F[j] + 1 for j in range(0, i) if A[j] < A[i]), default=1)
    return max(F)

# Idea: Greedy + Binary Search
#
# T = O(nlogn)
#
# active lists:
#    [
#      [],
#      ...
#      [..., A[tail[j]]]
#    ]
#
# - j: length of an active list
#
# - tail[j]: the index of the smallest value A[k] such that it exists an
#            increasing subsequence of length j ending at A[k] on the range
#            k <= i
#
# - prev[k]: the index of the predecessor of A[k] in the LIS ending at A[k]
#
# See also: patience sorting
#
def lis_v2(A):
    n = len(A)
    # Note: tail[0] is not used
    tail = [0] * (n+1)
    prev = [-1] * n
    max_sz = 0
    for i in range(n):
        # binary search for the largest positive 1 <= j <= max_sz
        # such that A[tail[j]] < A[i]
        #
        # note that A[tail[1]] ... A[tail[L]] is an increasing sequence
        j = ceil_search(lambda m: A[tail[m]], 1, max_sz, A[i])
        # the predecessor of A[i] = the last index of the subsequence of length j-1
        prev[i] = tail[j-1]
        tail[j] = i
        max_sz = max(max_sz, j)
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

def ceil_search(func, l, r, target):
    while l <= r:
        m = (l + r + 1) // 2
        if func(m) < target:
            l = m+1
        else:
            r = m-1
    return l

# https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
# https://www.geeksforgeeks.org/construction-of-longest-monotonically-increasing-subsequence-n-log-n/
# https://stackoverflow.com/questions/2631726/how-to-determine-the-longest-increasing-subsequence-using-dynamic-programming
