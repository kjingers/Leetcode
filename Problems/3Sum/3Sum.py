'''
Since we don't need to return the indicies, we can sort the input aray and not have to worry about
remembering each num's index. 

We can start from beginning and loop through array. For each num, we essentially do a two sum on the
rest of the array to the right.

Time Complexity: O(nlogn + n^2) = O(n^2)
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) < 3:
            return []
        
        result = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            
            # Avoid Duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            target = -nums[i]
            
            # Now normal two sum from i+1 to len(nums) to find target above
            left = i + 1
            right = len(nums) - 1
            while left < right:
                curSum = nums[left] + nums[right]
                
                if curSum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    
                    # Keep incrementting left if duplicate
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
                elif curSum < target:
                    left += 1
                else:
                    right -= 1
                    
        return result
            
