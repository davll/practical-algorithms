# https://leetcode.com/problems/online-stock-span/
# https://www.geeksforgeeks.org/the-stock-span-problem/

class StockSpanner:
    def __init__(self):
        self.stack = []
        self.count = 0
    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        curr = last = self.count
        self.count += 1
        while self.stack:
            i, p = self.stack[-1]
            if p <= price:
                self.stack.pop()
                last = i
            else:
                break
        self.stack.append((last, price))
        return curr - last + 1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
