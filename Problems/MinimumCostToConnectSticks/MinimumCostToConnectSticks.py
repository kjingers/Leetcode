'''
Always want to combine the two sticks with the smallest lengths to minimize cost. Can use minHeap to get the two sticks with lowest cost. One we combine sticks. We put back into heap

Time: heapify: O(n) + O(nlog(n))
'''

from heapq import *

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)
        totalCost = 0
        
        while len(sticks) > 1:
            cost = heappop(sticks) + heappop(sticks)
            heappush(sticks, cost)
            totalCost += cost
            
        return totalCost
            
            
        
