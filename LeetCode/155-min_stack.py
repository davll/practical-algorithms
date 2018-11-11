class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.stack:
            m = min(self.stack[-1][1], x)
        else:
            m = x
        self.stack.append((x, m))
    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()
    def top(self):
        """
        :rtype: int
        """
        x, _ = self.stack[-1]
        return x
    def getMin(self):
        """
        :rtype: int
        """
        _, m = self.stack[-1]
        return m


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
