'''
Get array of heights fom the vertical cuts. Get array of heaights from vertical cuts.

Since we have to do the same process for horizontal cuts and vertical cuts, good idea to createa a function.
    - By updating the max each loop, we can save space for creating a whole new array of gaps
    - I don't think we can get around sorting the arrays. Maybe there is an algorithm
'''

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        horizontalCuts.sort()
        verticalCuts.sort()
        
        maxHeight = self.getMaxGap(horizontalCuts, h)
        maxWidth = self.getMaxGap(verticalCuts, w)        
        
        return (self.getMaxGap(horizontalCuts, h) * self.getMaxGap(verticalCuts, w)) % (10**9 + 7)
        
    
    def getMaxGap(self, nums, max_size):
        maxGap = max(nums[0], max_size - nums[-1])
        
        for i in range(1, len(nums)):
            maxGap = max(maxGap, nums[i] - nums[i - 1])
            
        return maxGap

        
