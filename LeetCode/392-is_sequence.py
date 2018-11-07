# https://leetcode.com/problems/is-subsequence/

# Idea: Dynamic Programming
def is_subseq_v1(S, T):
    m, n = len(S), len(T)
    dp = [[False] * n for _ in range(m)]
    # initial: check if S[:1] is subseq of T
    dp[0][0] = S[0] == T[0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] or S[0] == T[j]
    # iteration
    for i in range(1, m):
        for j in range(i, n):
            dp[i][j] = dp[i][j-1] or (dp[i-1][j-1] and S[i] == T[j])
    return dp[m-1][n-1]

# Idea: Greedy Method
def is_subseq_v2(S, T):
    m, n = len(S), len(T)
    i = 0
    # Time = O(N)
    for j in range(n):
        if i == m:
            return True
        if S[i] == T[j]:
            i += 1
    return i == m

# Idea: Binary Search
def is_subseq_v3(S, T):
    def upper_bound(arr, l, r, t):
        ans = r
        while l < r:
            m = (l+r) // 2
            k = arr[m]
            if t < k:
                ans = m
                r = m
            else:
                l = m+1
        return ans
    # M = len(S), N = len(T)
    # Space = O(N)
    pos = [[] for _ in range(26)]
    # Time = O(N)
    for i, c in enumerate(T):
        c = ord(c) - ord('a')
        pos[c].append(i)
    # Time = O(M * log(N))
    idx = -1
    for i, c in enumerate(S):
        c = ord(c) - ord('a')
        j = upper_bound(pos[c], 0, len(pos[c]), idx)
        if j < len(pos[c]):
            idx = pos[c][j]
        else:
            return False
    return True

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        if not t:
            return False
        return is_subseq_v3(s, t)
