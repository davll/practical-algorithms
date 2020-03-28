from math import inf, isinf

def upper_bound(arr, x):
    l, r = 0, len(arr)
    while l < r:
        m = (l + r) // 2
        if x < arr[m]:
            r = m
        else:
            l = m + 1
    return r

class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        # preprocess
        lookup = [[] for _ in range(3)]
        for c in [1,2,3]:
            for i in range(len(colors)):
                if colors[i] == c:
                    lookup[c-1].append(i)
        # go go go
        result = []
        for i, c in queries:
            if colors[i] == c:
                result.append(0)
                continue
            arr = lookup[c-1]
            if not arr:
                result.append(-1)
                continue
            k = upper_bound(arr, i)
            if k == 0:
                result.append(abs(i - arr[k]))
            elif k == len(arr):
                result.append(abs(i - arr[-1]))
            else:
                x = min(abs(i-arr[k-1]), abs(i-arr[k]))
                result.append(x)
        return result
