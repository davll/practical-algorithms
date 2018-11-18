# https://leetcode.com/problems/rectangle-area-ii/

class Solution:
    def rectangleArea(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        # rectangle: (x1, y1, x2, y2) => (left, bottom, right, top)
        return rect_area_v1(rectangles)

# Binary Search
def rect_area_v1(rectangles):
    X = [x for x1, _, x2, _ in rectangles for x in (x1, x2)]
    X.sort()
    X = dedup(X)
    NX = len(X)
    Y = [[] for _ in range(NX)]
    M = [None for _ in range(NX)]
    for x1, y1, x2, y2 in rectangles:
        l = bsearch(X, 0, NX-1, x1)
        r = bsearch(X, 0, NX-1, x2)
        for i in range(l, r):
            Y[i].append(y1)
            Y[i].append(y2)
    for i in range(NX):
        Y[i].sort()
        Y[i] = dedup(Y[i])
        M[i] = [False] * len(Y[i])
    for x1, y1, x2, y2 in rectangles:
        l = bsearch(X, 0, NX-1, x1)
        r = bsearch(X, 0, NX-1, x2)
        for i in range(l, r):
            b = bsearch(Y[i], 0, len(Y[i])-1, y1)
            t = bsearch(Y[i], 0, len(Y[i])-1, y2)
            for j in range(b, t):
                M[i][j] = True
    #
    result = 0
    mod = 10 ** 9 + 7
    for i in range(NX-1):
        w = X[i+1] - X[i]
        for j in range(len(Y[i])-1):
            if not M[i][j]:
                continue
            h = Y[i][j+1] - Y[i][j]
            result += (w * h) % mod
    return result % mod

# Idea: Line Sweap

# Idea: Segment Tree

def bsearch(nums, l, r, t):
    while l <= r:
        m = (l + r) // 2
        if nums[m] == t:
            return m
        elif nums[m] < t:
            l = m + 1
        else:
            r = m - 1
    return None

def dedup(arr):
    n = len(arr)
    k = 0
    for i in range(n):
        if k == 0 or arr[k-1] != arr[i]:
            arr[k] = arr[i]
            k += 1
    return arr[:k]
