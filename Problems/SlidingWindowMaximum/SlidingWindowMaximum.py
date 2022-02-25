'''
Monotonic Decreasing Queue ensures max element at head.

After pushing to queue, if head index is out of window, then pop it out. 
Then update output array if we have gone atleast k loops.

I think a heap could work too, but that would make the Time Complexity: O(nlog(k))
Monotonic queue works better, because once we pop a smaller value, we don't need to keep track of it anymore.
'''


from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        output = []
        
        queue = deque()
        
        for i, val in enumerate(nums):
            
            # Pop smaller elements so montonically decreasing
            while queue and nums[queue[-1]] < val:
                queue.pop()
                
            queue.append(i)
            
            # Remove head from deque if outside of window
            if queue[0] <= i - k:
                queue.popleft()
                
            
            if i >= k - 1:
                output.append(nums[queue[0]])
                
        return output
        
