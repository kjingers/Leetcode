'''
Monotonic Decreasing stack can be used. Once we finish going through the heights array,
the resulting stack is the output.

For every height, we want to pop all the smaller heights from the stack.

Similar to Daily Temperatures Problem
'''
from collections import deque

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        stack = deque()
        
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] <= h:
                stack.pop() # Popped building cannot see ocean
            stack.append(i)
            
        return list(stack)
        
