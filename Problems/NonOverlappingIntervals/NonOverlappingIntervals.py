'''
https://leetcode.com/problems/non-overlapping-intervals/discuss/91768/Python-greedy-solution-with-explanation


We can sort intervals by start time. As we iterate through, if current interval overlaps with previous
interval, pick the one that ends sooner and iterate removal counter.

The interval that ends later will always have a greater chance to overlap future intervals.

Time Complexity: O(n*log(n)) for sort
'''


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # Sort intervals by start
        intervals.sort(key=lambda x: x[0])
        
        prevEnd = intervals[0][1]
        count = 0
        
        for i in range(1, len(intervals)):
            
            # If current interval overlaps previous
            if prevEnd > intervals[i][0]:
                
                # Pick the smaller end. Iterate removal count
                prevEnd = min(prevEnd, intervals[i][1])
                count += 1
            else:
                prevEnd = intervals[i][1]
        
        return count
                
            
        
        
        
