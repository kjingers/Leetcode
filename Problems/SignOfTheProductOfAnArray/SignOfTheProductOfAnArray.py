'''
Pretty straightforward one pass solution. When we hit a negative, toggle bool negative
'''

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        ans = 1
        for num in nums:
            if num == 0:
                return 0
            if num <= 0:
                ans *= -1
        
        return ans
        
