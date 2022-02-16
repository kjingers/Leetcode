'''
At each point, we want to find the next greater/equal element. If it's more than one spot away, the
water is trapped.

Monotonic Decreasing Stack can be used to find next greater elevation.
-   For each elevation we add without popping, we can add water to the current trap.
-   One we find the next >= elevation, we can add the water to our output
'''

from collections import deque

class Solution:
    def trap(self, height: List[int]) -> int:
        
        output = 0
        currWater = 0
        stack = deque()
        
        # Monotonic Decreasing Stack
        # Store indices so we can calculate volume when we get a greater height
        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                bottom = stack.pop()
                
                # No left height for trap. Skip
                if not stack:
                    continue
                    
                # At this point, we can calculate water trapped in
                # stack[-1] down to bottom up to h
                trapWidth = i - stack[-1] - 1
                trapHeight = min(height[stack[-1]], h) - height[bottom]
                output += trapWidth * trapHeight
                
            stack.append(i)
            
        return output
                
        
