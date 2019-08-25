from collections import Counter

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        x1, y1 = p1
        x2, y2 = p2
        dx, dy = x2 - x1, y2 - y1
        self.normal = (-dy, dx)
        self.d = -dy * x1 + dx * y1
    def _apply(self, p):
        x, y = p
        nx, ny = self.normal
        return nx * x + ny * y - self.d
    def __contains__(self, p):
        return self._apply(p) == 0

def enumerate_lines(points):
    n = len(points)
    for i in range(n):
        p1 = points[i]
        for j in range(1, n):
            p2 = points[j]
            if p1 == p2:
                continue
            yield Line(p1, p2)

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points = Counter(map(lambda x: tuple(x), points))
        result = max(points.values())
        for line in enumerate_lines(list(points.keys())):
            count = 0
            for p, c in points.items():
                if p in line:
                    count += c
            result = max(result, count)
        return result
