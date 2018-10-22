# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def max_profit_v1(prices):
    n, result = len(prices), 0
    for i in range(n):
        for j in range(i+1, n):
            profit = prices[j] - prices[i]
            result = max(result, profit)
    return result

def max_profit(prices):
    from heapq import heappush
    n, result = len(prices), 0
    if n == 0:
        return 0
    minheap = [prices[0]]
    for i in range(1,n):
        prev = minheap[0]
        result = max(result, (prices[i] - prev))
        heappush(minheap, prices[i])
    return result

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return max_profit(prices)
