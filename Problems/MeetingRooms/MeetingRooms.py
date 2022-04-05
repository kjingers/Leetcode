'''
Unlike Meeting Rooms II, we can just compare start time of current meeting with end time of previous meeting. If anyoverlap, return false.
'''

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x:x[0])
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
            
        return True
        
