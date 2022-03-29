'''
Sliding Window + Monotonic queues:

So, we can see that sliding window can be used. The problem is, how do we efficiently find the max and min values within the window? And how do we shrink the window?
    - Can use two heaps for O(nlogn)?
    - Two monotonic queues can give O(n)
    
Let's store the indexes in the queues. With the queues, using both increasing and decreasing queues, the elements from front to back are in order that they appear in nums. 

So, nums[maxQueue[0]] - nums[minQueue[0]] is the max - min. When this is invalidated, we can shrink the window by incrementing the left index. So, we increment left index, and popleft from queues if max/min index is < left. We keep doing this until difference is within limit. Then, we update our max.



'''
from collections import deque

# Sliding WIndow
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        maxQueue = deque()
        minQueue = deque()
        
        left = 0
        maxLen = 0
        
        for right, num in enumerate(nums):
            
            # Update queues
            
            while maxQueue and nums[maxQueue[-1]] <= num:
                maxQueue.pop()
            
            while minQueue and nums[minQueue[-1]] >= num:
                minQueue.pop()
                
            maxQueue.append(right)
            minQueue.append(right)
            
            # Now, front of both queues have max and min values of window
            
            # Shrink Winodw if difference is > limit
            while nums[maxQueue[0]] - nums[minQueue[0]] > limit:
                left += 1
                
                if maxQueue[0] < left:
                    maxQueue.popleft()
                
                if minQueue[0] < left:
                    minQueue.popleft()
                    
            
            maxLen = max(maxLen, right - left + 1)
            
        return maxLen
                
