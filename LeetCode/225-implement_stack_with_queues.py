from collections import deque

class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = deque()
    #
    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue1.append(x)
    #
    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        n = len(self.queue1)
        for _ in range(n-1):
            x = self.queue1.popleft()
            self.queue1.append(x)
        return self.queue1.popleft()
    #
    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        n = len(self.queue1)
        for _ in range(n-1):
            x = self.queue1.popleft()
            self.queue1.append(x)
        x = self.queue1.popleft()
        self.queue1.append(x)
        return x
    #
    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue1) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
