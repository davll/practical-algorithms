# https://leetcode.com/problems/rectangle-area-ii/

class Solution:
    def rectangleArea(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        # rectangle: (x1, y1, x2, y2) => (left, bottom, right, top)
        return rect_area_v2(rectangles)

# Idea: Binary Search
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
#
# Scan from bottom to top
#
def rect_area_v2(rectangles):
    # compress coordinates
    X = [x for x1, _, x2, _ in rectangles for x in (x1, x2)]
    Y = [y for _, y1, _, y2 in rectangles for y in (y1, y2)]
    X.sort()
    Y.sort()
    X = dedup(X)
    Y = dedup(Y)
    # build events from bottom to top, from left to right
    OPEN, CLOSE = 1, -1
    events = []
    for x1, y1, x2, y2 in rectangles:
        events.append((y1, OPEN, x1, x2))
        events.append((y2, CLOSE, x1, x2))
    events.sort(reverse = True)
    # scan from bottom to top
    MOD = 10 ** 9 + 7
    result = 0
    flags = [0] * len(X)
    for i in range(len(Y)):
        # compute the height
        if i > 0:
            h = Y[i] - Y[i-1]
            for j in range(len(X)-1):
                if not flags[j]:
                    continue
                w = X[j+1] - X[j]
                result = (result + w * h) % MOD
        # update intervals
        while events and events[-1][0] == Y[i]:
            _, kind, x1, x2 = events.pop()
            l = bsearch(X, 0, len(X)-1, x1)
            r = bsearch(X, 0, len(X)-1, x2)
            for j in range(l, r):
                flags[j] += kind
    #
    return result

# Idea: Segment Tree
def rect_area_v3(rectangles):
    pass

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
