from heapq import heapify, heappop

def dist_candy_v1(scores):
    n = len(scores)
    queue = [(s, i) for (i, s) in enumerate(scores)]
    candy = [0] * n
    heapify(queue)
    while queue:
        s, i = heappop(queue)
        c = 0
        if i > 0 and s > scores[i-1]:
            c = max(candy[i-1], c)
        if i < n-1 and s > scores[i+1]:
            c = max(candy[i+1], c)
        candy[i] = c + 1
    return sum(candy)

class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        return dist_candy_v1(ratings)
