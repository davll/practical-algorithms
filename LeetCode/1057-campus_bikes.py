def manhattan(ax, ay, bx, by):
    return abs(ax - bx) + abs(ay - by)

def assign_bikes_v1(workers, bikes):
    n = len(workers)
    m = len(bikes)
    assert n <= m
    pairs = []
    for wi, wp in enumerate(workers):
        for bi, bp in enumerate(bikes):
            wx, wy = wp
            bx, by = bp
            dist = manhattan(wx, wy, bx, by)
            pairs.append((dist, wi, bi))
    pairs.sort(key = lambda t: (t[0], t[1], t[2]))
    used = [False] * m
    assigned = [False] * n
    ans = [-1] * n
    for _, wi, bi in pairs:
        if not assigned[wi] and not used[bi]:
            ans[wi] = bi
            assigned[wi] = True
            used[bi] = True
    return ans

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        return assign_bikes_v1(workers, bikes)
