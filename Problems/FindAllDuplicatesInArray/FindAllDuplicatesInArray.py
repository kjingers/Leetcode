'''
Cyclic Sort Works

[4,3,2,7,8,2,3,1]

Another in-place O(n) solution is for each nums[i], mark nums[nums[i]] as negative. Then go through again, all positive indexes are duplicates.
    - Can do one loop by marking as negative. THen if as we are marking, it is already negative, then we know its dupe
'''


# Marking NEgative
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        ans = []
        for i in range(n):
            #print(i)
            #print(nums)
            if nums[abs(nums[i]) - 1] < 0:
                ans.append(abs(nums[i]))
                
            nums[abs(nums[i]) - 1] *= -1
            
        return ans
                

# Cyclic Sort
'''
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        
        i = 0
        while i < n:
            dest_index = nums[i] - 1
            if nums[dest_index] != nums[i]:
                nums[dest_index], nums[i] = nums[i], nums[dest_index]
            else:
                i += 1
        
        ans = []
        for i in range(n):
            if nums[i] != i + 1:
                ans.append(nums[i])
                
        return ans
  
'''
            
        
