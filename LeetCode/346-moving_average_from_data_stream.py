from collections import deque

class MovingAverage:
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.queue = deque()
        self.total = 0
    #
    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        while len(self.queue) >= self.size:
            self.total -= self.queue.popleft()
        self.queue.append(val)
        self.total += val
        return self.total / len(self.queue)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
