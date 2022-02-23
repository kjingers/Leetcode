'''
At each point, we want to find the next greater/equal element. If it's more than one spot away, the
water is trapped.

Monotonic Decreasing Stack can be used to find next greater elevation.
-   For each elevation we add without popping, we can add water to the current trap.
-   One we find the next >= elevation, we can add the water to our output


First did this problem with monotonic decreasing stack. 

Another method is using left and right pointers.
    - Maintain leftPointer, leftMax, rightPointer, leftMax
    - If leftmax < rightMax, then iterate left pointer
        - if height[left] >= leftMax, then just update leftMax. No water to add
        - If height[left] < leftMax, then add water += leftMax - height[left]
    - Same with decrementing right pointer
    
NOTE: left <= right to get the last water at the end.

Since we move the side that is shorter, when current height is less than max, we are guarenteed to hold water,
since we've seen a higher left end (leftMax) and know there is a higher right end (rightMax > leftMax)
'''

# Two Pointer Method

class Solution:
    def trap(self, height: List[int]) -> int:
        
        if len(height) < 3:
            return 0
        
        n = len(height)
        
        leftMax, rightMax = height[0], height[n - 1]
        left, right = 1, n - 2
        water = 0
        
        while left <= right:
            if leftMax < rightMax:
                if height[left] > leftMax:
                    leftMax = height[left]
                else:
                    water += leftMax - height[left]
                    
                left += 1
            
            else:
                if height[right] > rightMax:
                    rightMax = height[right]
                else:
                    water += rightMax - height[right]
                    
                right -= 1
                
        return water



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
                
        
