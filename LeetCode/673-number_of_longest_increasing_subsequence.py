# https://leetcode.com/problems/number-of-longest-increasing-subsequence/

# Idea: Dynamic Programming => TLE :(
#
# C[k,i] = Number of k-length increasing subsequences ending at A[i]
#
def num_lis_v1(A):
    n = len(A)
    L = lis(A)
    C = [[0] * n for _ in range(L+1)]
    for i in range(n):
        C[1][i] = 1
    for k in range(2, L+1):
        for i in range(n):
            C[k][i] = sum(C[k-1][j] for j in range(i) if A[j] < A[i])
    return sum(C[L])

# Idea: Dynamic Programming => Improved
#
# L[i] = the length of LIS ending at A[i]
# C[i] = the number of LIS ending at A[i]
#
# If [.. A[k], A[i]] is a LIS, L[k] must be L[i]-1 (proof by contradiction)
#
def num_lis_v2(A):
    n = len(A)
    L = [1] * n
    C = [1] * n
    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i]:
                lj = L[j] + 1
                if lj > L[i]:
                    L[i] = lj
                    C[i] = C[j]
                elif lj == L[i]:
                    C[i] += C[j]
    maxlen = max(L, default=0)
    return sum(map(lambda i: C[i], filter(lambda i: L[i] == maxlen, range(n))))

def lis(A):
    n = len(A)
    L = [1] * n
    for i in range(1, n):
        L[i] = max((L[j]+1 for j in range(i) if A[j] < A[i]), default=1)
    return max(L, default=0)

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return num_lis_v2(nums)
