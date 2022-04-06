'''
Looks like greedy, where we want to attend the events the end the soonest first.

Basically, iterate through days 1 to final day. Each day, 
    - add all events (end day) that start at or before day to minHeap
    - Remove all events that have already ended
    - If minHeap not empty, then pop top (soonest end time) and increment count
'''

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        minHeap = []
        count = 0
        events.sort()
        totalDays = max([x[1] for x in events])
        day = 1
        event_id = 0
        
        while day <= totalDays:
            
            # Skip ahead to next event if no events to attend
            if not minHeap and event_id < len(events):
                day = events[event_id][0]
              
            # Push the end day of all events that start on or before this day
            while event_id < len(events) and events[event_id][0] <= day:
                heappush(minHeap, events[event_id][1])
                event_id += 1
                
            # Remove all events that have already ended
            while minHeap and minHeap[0] < day:
                heappop(minHeap)
                
            if minHeap:
                heappop(minHeap)
                count += 1
            
            day += 1
        
        return count
                
            
                
            
            
            
        
