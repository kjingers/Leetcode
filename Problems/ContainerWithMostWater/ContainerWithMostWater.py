'''
1. Start with the widest lines. Since they are the farthest apart, they are a  good candidate for most water.
2. Increment/decrement whichever line is shorter, since it cannot be used to get more water.
    - This is because the amount of water is bounded by the shorter line. 
    - If both heights are the same, then it doesn't matter which we move from. 
'''



class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        water = 0
        
        while left < right:
            
            # Calculate area of water containeed with current left and right
            currWater = (right - left) * min(height[left], height[right])
            
            water = max(water, currWater)
            
            # Increment/decrement the shorter of the current heights
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
    
        return water
            
        
        
