# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def max_profit_v1(prices):
    n, result = len(prices), 0
    for i in range(n):
        for j in range(i+1, n):
            profit = prices[j] - prices[i]
            result = max(result, profit)
    return result

def max_profit_v2(prices):
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

def max_profit_v3(prices):
    minprice = float('inf')
    maxprofit = 0
    for price in prices:
        if price < minprice:
            minprice = price
        else:
            maxprofit = max(maxprofit, price - minprice)
    return maxprofit

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return max_profit_v3(prices)
