# https://leetcode.com/problems/meeting-rooms/

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals.sort(key=lambda i: (i.start, i.end))
        curr = Interval(0, 0)
        for iv in intervals:
            if curr.end > iv.start:
                return False
            curr = iv
        return True
