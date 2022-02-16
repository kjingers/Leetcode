'''
Very similar to trapping rain water.

We loop through the heights. Each height can be a candidate for calculation.

We can use monotonic stack to track increasing heights. For each height, if it is smaller than
largest on stack, then we pop the top of stack and calculate the bar area from:

stack[-1] to currIndex, with a height of stack.pop()

'''

from collections import deque

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = deque()
        maxArea = 0
        
        # Handle Boundaries with dummy buildings
        heights.append(0)
        stack.append(-1)
        
        # Monotonic Increasing Stack
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                barHeight = stack.pop() # Index for bar height to try. "Peak"
                width = i - stack[-1] - 1
                area = heights[barHeight] * width
                maxArea = max(maxArea, area)
            stack.append(i)
        
        return maxArea
                
        
