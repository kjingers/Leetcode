'''
Option 1: Cyclic Sort

Option 2: XOR Elements
    - XOR all elements together
    - Then XOR result with elements 0 to n
    - Result will be missing Number
'''

# Option 1: Cyclic Sort
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            to_index = nums[i]
            
            if to_index != i and to_index < len(nums):
                nums[i], nums[to_index] = nums[to_index], nums[i]
            else:
                i += 1
                
        for i in range(len(nums)):
            if nums[i] != i:
                return i
            
        return len(nums)
'''
    
# Option 2: XOR
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        out = nums[0]
        for num in nums[1:]:
            out ^= num
            
        for i in range(len(nums) + 1):
            out ^= i
        
        return out
                
        
