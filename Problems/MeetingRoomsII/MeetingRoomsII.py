'''
Can use minHeap for meeting end times. As we iterate through, if current meeting starts after the earliest end time,
then we pop from heap. At each point, the number of rooms needed is the size of the heap.

Time Complexity: O(nlogn)
    - nlogn to sort
    - nlogn worst-case to iterate through n intervals and inert into heap
    
Space Complexity: O(n)

Another strategy is to create two seperate lists: sorted start times and sorted end times.
    - start and end pointers both start at 0
    - Iterate through s. if start[i] < end[j], then add 1 to output.
    - Else if start[i] >= end[j], then j += 1




from heapq import *
'''
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x:x[0])
        
        minHeap = []
        minRooms = 0
        
        for interval in intervals:
            
            # Pop all meetings that end before the start of current interval
            while minHeap and minHeap[0][0] <= interval[0]:
                
                heappop(minHeap)
                
            # Push as Tuple with end time first
            heappush(minHeap, (interval[1], interval))
            
            minRooms = max(minRooms, len(minHeap))
            
        return minRooms


'''
class Solution:
    def minMeetingRooms(self, intervals):
            e = ret = 0
            start = sorted(i[0] for i in intervals)
            end = sorted(i[1] for i in intervals)

            for s in range(len(start)):
                if start[s] < end[e]: 
                    ret += 1
                else: 
                    e += 1
            return ret
            
'''           
        
