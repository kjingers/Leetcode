'''
One method (Two-Pointers ish)
Keep pointer to beginning. Loop through nums. 
    - Whenever we get non-zero num, swap it with nums[begPointer], then iterate begPointer. 
    - If we get a zero, then just continue

'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        leftPointer = 0
        
        for i, num in enumerate(nums):
            if num != 0:
                nums[leftPointer], nums[i] = nums[i], nums[leftPointer]
                leftPointer += 1
                
        return nums
        
