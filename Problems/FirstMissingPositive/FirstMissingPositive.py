'''
Can use cyclic sort pattern, since we are concerned with number 1 to n in an array of size n.

As we go through array, put each number in its correct index (1 into index 0, 2 into index 1, etc)

Traverse again, the first number not in its correct index is the first missing positive.
'''

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        i = 0
        
        while i < n:
            
            # Ones based - Desired Index
            j = nums[i] - 1
            
            if j >= 0 and j < n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        
        # Now loop through and find first index without expected value
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
            
        return n + 1
                
        
                
        
