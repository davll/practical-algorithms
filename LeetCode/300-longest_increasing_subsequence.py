# https://leetcode.com/problems/longest-increasing-subsequence/description/
# https://leetcode.com/problems/longest-increasing-subsequence/solution/
# https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/

# Idea: Dynamic Programming
#
# F[i] = Length of LIS ends at A[i]
#
# F[0] = 1
#
# F[i] = max { F[j]+1 } for all j < i st. A[j] < A[i]
#      = 1              if no such j exists
#
def lis_v1(A):
    if not A:
        return 0
    n = len(A)
    F = [0] * n
    F[0] = 1
    for i in range(1, n):
        F[i] = max((F[j] + 1 for j in range(0, i) if A[j] < A[i]), default=1)
    return max(F)

# Idea: Greedy Method + Binary Search
def lis_v2(A):
    n = len(A)
    tail = [0] * (n+1)
    max_sz = 0
    for i in range(n):
        j = ceil_search(lambda m: A[tail[m]], 1, max_sz, A[i])
        tail[j] = i
        max_sz = max(max_sz, j)
    return max_sz

def ceil_search(func, l, r, target):
    while l <= r:
        m = (l + r + 1) // 2
        if func(m) < target:
            l = m+1
        else:
            r = m-1
    return l

class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return lis_v2(nums)
