class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(1, n+1):
            for w in wordDict:
                if len(w) <= i and w == s[i-len(w):i]:
                    dp[i] = dp[i] or dp[i-len(w)]
        return dp[n]
