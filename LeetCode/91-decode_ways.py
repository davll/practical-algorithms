class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 1
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        for i in range(2, n+1):
            prev, curr = map(int, (s[i-2], s[i-1]))
            if curr == 0:
                dp[i] = dp[i-2]
                if prev not in (1, 2):
                    return 0
            else:
                dp[i] = dp[i-1]
                if prev == 1:
                    dp[i] += dp[i-2]
                elif prev == 2 and curr <= 6:
                    dp[i] += dp[i-2]
        return dp[n]
