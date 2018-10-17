# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals.sort(key = lambda x: (x.start, x.end))
        result = [Interval(intervals[0].start, intervals[0].end)]
        for interval in intervals:
            if result[-1].end >= interval.start:
                result[-1].end = max(result[-1].end, interval.end)
            else:
                result.append(Interval(interval.start, interval.end))
        return result
