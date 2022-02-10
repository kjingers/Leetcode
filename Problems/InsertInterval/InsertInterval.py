'''
If list was unsorted, we could simply append newInterval and merge intervals in nlog(n)

Since list is sorted, we can do better.
- Iterate though inervals while newInterval.start > interval[i].end
- Once this condition breaks, our new interval either comes completely before current interval,
  or, our new interval overlaps the current interval.
- So, if current interval overlaps new interval, merge them together. Keep doing this until
  current interval does not overlap our merged interval/
- Insert merged interval
- Insert the rest of the intervals


Time Complexity: O(n)

'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        i = 0
        output = []
        
        
        # 1. Skip through all intervals that end before our newInterval starts
        while i < len(intervals) and newInterval[0] > intervals[i][1]:
            output.append(intervals[i])
            i += 1
            
        # 2. While our newIntervals overlaps intervals[i], merge them together
        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
            
        output.append(newInterval)
        
        # Add the rest of the non-overlapping intervals
        while i < len(intervals):
            output.append(intervals[i])
            i += 1
            
        return output
            
        
        
