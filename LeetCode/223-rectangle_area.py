class Rect:
    def __init__(self, l, b, r, t):
        self.left = l
        self.bottom = b
        self.right = r
        self.top = t
    @property
    def area(self):
        w = max(0, self.right - self.left)
        h = max(0, self.top - self.bottom)
        return w * h

def intersection(rt1, rt2):
    l = max(rt1.left, rt2.left)
    r = min(rt1.right, rt2.right)
    b = max(rt1.bottom, rt2.bottom)
    t = min(rt1.top, rt2.top)
    return Rect(l, b, r, t)

class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        rt1 = Rect(A, B, C, D)
        rt2 = Rect(E, F, G, H)
        rt3 = intersection(rt1, rt2)
        return rt1.area + rt2.area - rt3.area
