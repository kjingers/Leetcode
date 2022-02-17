'''
We can solve this problem similar to Largest Rectangle Histogram problem. We use the "Largest Rectandle Histogram"
solution m times for each row. We maintain an array of heights.
-   For each row, if row[i] == 1, heights[i] += 1. Else, reset heights[i] = 0. THis is because our "histogram"
    would have a gap. So we can't use it for calculations.
-   Then, for each row, we use a monotonic increasing stack, because we will calculate a new area when we
    get a height that is smaller than the top of the stack.
    
    width = i (curr) - stack[-1] - 1
    height = heights[stack.pop()]
    
-   NOTE: For boundary conditions, make sure heights[n + 1] = 0 to create right boundary, and
    push index '-1' to stack (heights[-1] = 0 above)
    
    Time Complexity: O(MN)
'''

from collections import deque

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        if not matrix or not matrix[0]:
            return 0
        
        m = len(matrix)
        n = len(matrix[0])
        
        # Initialize heights array. Make it length N + 1 so that we have a 0 on the right boundary
        heights = [0 for _ in range(n + 1)]
        
        maxArea = 0
        
        
        # Now process row by row, making heights array into a historgram
        for row in matrix:
            
            # Add one to histogram if another "1" for current row
            # If a "0", then reset height to 0 (since there would be gap)
            for i in range(n):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
                
            stack = deque([-1])
            
            # Monotonic Increasing Stack
            # Processing length of heights, which is n + 1 (for added 0 on right)
            for i in range(n + 1):
                while stack and heights[stack[-1]] > heights[i]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    maxArea = max(maxArea, h * w)
                stack.append(i)
                
        return maxArea
                
                
                
        
        
        
