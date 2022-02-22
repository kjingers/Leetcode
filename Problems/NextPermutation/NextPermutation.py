'''
The optimal solution requires a specific trick/algorithm. Technically a form of 2 pointers

1. From right, find longest non-increasing subsequence
2. Find pivot (num just before start of longest non-increasing subsequence to end)
3. Find right-most successor to pivot (right-most num that is > than pivot)
4. Swap pivot with successor.
5. Reverse the suffix
'''


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        
        # From right, find longest non-increasing subsequence
        i = len(nums) - 1
        
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        
        # If i == 0, then entire list is non-increasing.
        # Dn't need to swap pivot, just reverse list
        if i > 0:
            pivot = i - 1
            
            j = len(nums) - 1
            while nums[j] <= nums[pivot]:
                j -= 1
                
            nums[pivot], nums[j] = nums[j], nums[pivot]
        
        self.reverseSublist(nums, i, len(nums) - 1)
        return nums
    
    # Helper Function to reverse sublist in-place from i to j inclusive
    def reverseSublist(self, nums, i, j):
        
        while j > i:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        
        
            
            
        
