'''
Must sort first by start time. 

We can iterate through itervals. 
- If current and previous overlap, then merge together and set merged to previous.
- If not overlap, append previous and set current to previous

Time Complexity: O(n*log(n)), since we must sort
'''


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        prev = intervals[0]
        merged = []
        
        
        for i in range(1, len(intervals)):
            
            # If Overlapping
            if prev[1] >= intervals[i][0]:
                #prev[0] = min(prev[0], intervals[i][0])
                prev[1] = max(prev[1], intervals[i][1])
            else:
                merged.append(prev)
                prev = intervals[i]
        
        merged.append(prev)
        return merged
        
