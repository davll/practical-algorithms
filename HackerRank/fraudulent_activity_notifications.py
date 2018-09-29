# Median in a stream of numbers

from collections import deque
from sys import stdin, stdout, stderr
import operator as op

class RunningMedian:
    def __init__(self, maxval, maxlen):
        self._count = [0] * (maxval + 1)
        self._maxlen = maxlen
        self._queue = deque()
    def push(self, x):
        self._queue.append(x)
        self._count[x] += 1
        if len(self._queue) > self._maxlen:
            x = self._queue.popleft()
            self._count[x] -= 1
    def median(self):
        d = self._maxlen // 2
        mid1, mid2 = None, None
        rs = 0
        for x, n in enumerate(self._count):
            rs += n
            if rs >= d and mid1 is None:
                mid1 = x
            if rs >= d+1:
                mid2 = x
                break
        if self._maxlen % 2 == 0:
            return (mid1 + mid2) / 2
        else:
            return mid2

if __name__ == "__main__":
    n, d = map(int, stdin.readline().rstrip().split())
    expe = list(map(int, stdin.readline().rstrip().split()))
    ans = 0
    q = RunningMedian(200, d)
    for i in range(d):
        q.push(expe[i])
    for i in range(d, n):
        m = q.median()
        if m * 2 <= expe[i]:
            ans += 1
        q.push(expe[i])
    stdout.write(str(ans) + '\n')
