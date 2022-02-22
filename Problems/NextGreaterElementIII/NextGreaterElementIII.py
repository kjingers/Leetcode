'''
Looks very similar to "Next Permutation"


'''

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        
        i = len(nums) - 1
        
        # Want to find longest non-increasing subsequence to end
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        
        # If digits are all non-increasing, then return -1
        if i == 0:
            return -1
        
        pivot = i - 1
                   
        # Want right-most number that is bigger
        j = len(nums) - 1

        while j > pivot and nums[j] <= nums[pivot]:
            j -= 1

        nums[pivot], nums[j] = nums[j], nums[pivot]
        

        self.reverseSublist(nums, i, len(nums) - 1)
        resultNum = int(''.join(nums))
        
        # Need to check if it fits in 32 bit integer
        
        return resultNum if resultNum < 1<<31 else -1
          
      
    # Reverse sublist in-place
    def reverseSublist(self, nums, i, j):
        
        while j > i:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        

                
            
                
        
