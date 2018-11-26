# https://leetcode.com/problems/insert-interval/

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

def insert_interval(intervals, newint):
    if not intervals:
        return [newint]
    result = []
    for iv in intervals:
        if iv.end < newint.start:
            result.append(iv)
        elif iv.start > newint.end:
            result.append(newint)
            newint = iv
        else:
            newint.start = min(newint.start, iv.start)
            newint.end = max(newint.end, iv.end)
    result.append(newint)
    return result

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        return insert_interval(intervals, newInterval)
