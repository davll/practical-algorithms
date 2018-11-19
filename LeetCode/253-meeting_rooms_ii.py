# https://leetcode.com/problems/meeting-rooms-ii/

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

from heapq import heappush, heappushpop

# Idea: Chronological Ordering
def meeting_rooms_v1(intervals):
    OPEN, CLOSE = 1, 0
    events = []
    for iv in intervals:
        events.append((iv.start, OPEN))
        events.append((iv.end, CLOSE))
    events.sort()
    #
    rooms = 0
    result = 0
    for _, kind in events:
        # close room first, open room then
        if kind == OPEN:
            rooms += 1
        else:
            rooms -= 1
        result = max(result, rooms)
    return result

# Idea: Priority Queue
def meeting_rooms_v2(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda i: i.start)
    rooms = []
    for iv in intervals:
        if rooms and rooms[0] <= iv.start:
            heappushpop(rooms, iv.end)
        else:
            heappush(rooms, iv.end)
    return len(rooms)

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        return meeting_rooms_v2(intervals)
