'''
Longest / shortest substring. SInce we can shrink window to invalidate the condition, we can use sliding window.
'''


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        maxLen = 0
        left = 0
        zerosCount = 0
        
        for right, num in enumerate(nums):
            if num == 0:
                zerosCount += 1
                
            # Shrink window
            while zerosCount > k:
                leftNum = nums[left]
                
                if leftNum == 0:
                    zerosCount -= 1
                
                left += 1
                
            maxLen = max(maxLen, right - left + 1)
            
        return maxLen
        
