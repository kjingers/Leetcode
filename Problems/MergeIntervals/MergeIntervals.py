'''
Sort by start time.
    - Append first interval to result.
    - For the following intervals, if interval's start is <= previous end, then update previous end (which is in result list)
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])
        result = []
        
        result.append(intervals[0])
        
        for interval in intervals:
            if interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)
        return result
        
        
        
