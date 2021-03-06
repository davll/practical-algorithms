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

# Idea: Dynamic Programming
#
# suppose a[0:n] is non-decreasing
#
# m[i] => the cost at a[i]
#
# m[i] = m[i-1] + 1                  if a[i-1] < a[i]
#      = 1                           if a[i-1] = a[i]
#      = 1                           if i = 0
#      = 1                           otherwise
#
# then generalize m[i] to allow increasing and decreasing
#
# m1[i] = m1[i-1] + 1       (forward direction)
# m2[i] = m2[i+1] - 1       (reverse direction)
# m[i] = max(m1[i], m2[i])
#
# then answer = sum(m[:])
#
# case 1: [10 10 10 10 10] => [1 1 1 1 1]
# case 2: [10 9 8 7 6] => [5 4 3 2 1]
# case 3: [1 2 2] => [1 2 1]
# case 4: [5 6 7 8 9] => [1 2 3 4 5]
# case 5: [5 6 6 8 9] => [1 2 1 2 3]
# case 6: [1 2 4 3 2 1] => [1 2 4 3 2 1]
# case 7: [1 2 4 4 3 2 1] => [1 2 3 4 3 2 1]
# case 8: [2 4 2 6 1 7 8 9 2 1] => [1 2 1 2 1 2 3 4 2 1]
# case 9: [2 4 3 5 2 6 4 5] => [1 2 1 2 1 2 1 2]
#
def dist_candy_v2(scores):
    n = len(scores)
    m1, m2 = [0] * n, [0] * n
    m1[0] = 1
    m2[-1] = 1
    for i in range(1,n):
        if scores[i-1] < scores[i]:
            m1[i] = m1[i-1] + 1
        elif scores[i-1] == scores[i]:
            m1[i] = 1
        else:
            m1[i] = 1
    for i in range(n-2,-1,-1):
        if scores[i+1] < scores[i]:
            m2[i] = m2[i+1] + 1
        elif scores[i+1] == scores[i]:
            m2[i] = 1
        else:
            m2[i] = 1
    return sum(map(max, zip(m1, m2)))

# Idea: Single Pass
#
# => Count how many ascending points and descending points
#
def dist_candy_v3(scores):
    n = len(scores)
    if n <= 1:
        return n
    candies = 0
    ascend, descend = 0, 0
    old_slope = 0
    for i in range(1, n):
        slope = compute_slope(scores, i-1, i)
        if (old_slope > 0 and slope == 0) or (old_slope < 0 and slope >= 0):
            candies += sum_from_1_to(ascend)
            candies += sum_from_1_to(descend)
            candies += max(ascend, descend)
            ascend, descend = 0, 0
        if slope > 0:
            ascend += 1
        if slope < 0:
            descend += 1
        if slope == 0:
            candies += 1
        old_slope = slope
    candies += sum_from_1_to(ascend)
    candies += sum_from_1_to(descend)
    candies += max(ascend, descend)
    candies += 1
    return candies

def sum_from_1_to(n):
    return (n * (n+1)) // 2

def compute_slope(nums, i, j):
    if nums[i] < nums[j]:
        return 1
    elif nums[i] > nums[j]:
        return -1
    else:
        return 0

class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        return dist_candy_v3(ratings)
