# Idea: Recursion
def compute_v1(n):
    def generate(p, l, r):
        if r >= l >= 0:
            if r == 0:
                yield p
            for q in generate(p + '(', l-1, r):
                yield q
            for q in generate(p + ')', l, r-1):
                yield q
    return list(generate('', n, n))

# Idea: Dynamic Programming
def compute_v2(n):
    dp = [[""]]
    for i in range(1, n+1):
        dp.append([])
        for sub in dp[i-1]:
            for j in range(0, len(sub)+1):
                dp[i].append('(' + sub[:j] + ')' + sub[j:])
        dp[i].sort()
        k = 1
        for j in range(1, len(dp[i])):
            if dp[i][k-1] != dp[i][j]:
                dp[i][k] = dp[i][j]
                k += 1
        dp[i] = dp[i][:k]
    return dp[n]

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return compute_v2(n)
