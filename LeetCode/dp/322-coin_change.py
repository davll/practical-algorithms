class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        for c in coins:
            if c == amount:
                return 1
        dp = [-1 for _ in range(amount+1)]
        dp[0] = 0
        for c in filter(lambda x: x <= amount, coins):
            dp[c] = 1
        for i in range(1, amount+1):
            s = [dp[i-c] + 1 for c in coins if i-c >= 0 and dp[i-c] != -1]
            if s:
                dp[i] = min(s)
        return dp[amount]
