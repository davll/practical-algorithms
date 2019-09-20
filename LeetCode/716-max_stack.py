# https://leetcode.com/problems/max-stack/

class MaxStackV1:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.sp = []
        self.mx = []
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.sp.append(x)
        if not self.mx:
            self.mx.append(x)
        else:
            self.mx.append(max(self.mx[-1], x))
    def pop(self):
        """
        :rtype: int
        """
        _ = self.mx.pop()
        return self.sp.pop()
    def top(self):
        """
        :rtype: int
        """
        return self.sp[-1]
    def peekMax(self):
        """
        :rtype: int
        """
        return self.mx[-1]
    def popMax(self):
        """
        :rtype: int
        """
        n = len(self.sp)
        if n == 1:
            return self.pop()
        tmp = []
        while self.mx[-1] != self.sp[-1]:
            tmp.append(self.sp.pop())
            _ = self.mx.pop()
        result = self.mx.pop()
        _ = self.sp.pop()
        for x in reversed(tmp):
            self.push(x)
        return result

MaxStack = MaxStackV1

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
