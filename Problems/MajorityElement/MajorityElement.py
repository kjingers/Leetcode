'''
Iterate through and count elements. Check if greater than n // 2 times
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        d = {}
        
        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1
            if d[num] > len(nums) // 2:
                return num
        
        
