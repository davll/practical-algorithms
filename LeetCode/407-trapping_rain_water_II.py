# https://leetcode.com/problems/trapping-rain-water-ii/description/

# Hint: BFS

def trap_water_v1(heights):
    from heapq import heapify, heappush, heappop
    #
    m, n = len(heights), len(heights[0])
    #print("m = {m}, n = {n}".format(m=m, n=n))
    heap = []
    visited = [[False for _ in range(n)] for _ in range(m)]
    # visit borders
    for j in range(0, n, max(n-1, 1)):
        if j not in range(n):
            continue
        for i in range(m):
            assert not visited[i][j]
            #print("visit h[{i}, {j}] = {h}".format(i=i,j=j,h=heights[i][j]))
            heap.append((heights[i][j], i, j))
            visited[i][j] = True
    for i in range(0, m, max(m-1, 1)):
        if i not in range(m):
            continue
        for j in range(1,n-1):
            assert not visited[i][j]
            #print("visit h[{i}, {j}] = {h}".format(i=i,j=j,h=heights[i][j]))
            heap.append((heights[i][j], i, j))
            visited[i][j] = True
    heapify(heap)
    # visit cells
    max_height = 0
    water = 0
    while heap:
        h, i, j = heappop(heap)
        assert h == heights[i][j]
        #print("process h[{i}, {j}] = {h}".format(i=i,j=j,h=h))
        #print("max_height = {mh}, water = {w}".format(mh=max_height, w=water))
        if h > max_height:
            max_height = h
        else:
            water += max_height - h
        for ni, nj in ((i-1,j), (i+1,j), (i,j-1), (i,j+1)):
            #print("try [{i}, {j}]".format(i=ni, j=nj))
            if ni not in range(m) or nj not in range(n):
                continue
            if not visited[ni][nj]:
                #print("visit h[{i}, {j}] = {h}".format(i=ni,j=nj,h=heights[ni][nj]))
                heappush(heap, (heights[ni][nj], ni, nj))
                visited[ni][nj] = True
    return water

class Solution:
    def trapRainWater(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        if not heights:
            return 0
        return trap_water_v1(heights)
