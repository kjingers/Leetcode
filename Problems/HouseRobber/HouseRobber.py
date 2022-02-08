'''
Cannot choose any two adjacent houses. So, as we loop from end to beginning of array we have two options:
1. Choose current house i. Solve for (i + 2), since we can't pick (i + 1)
2. Do not choose current house, solve for (i + 1)

At each step, we recursively solve for both options and pick the max.

Recurrence Relation:

rob(i) = max( rob(i + 2) + currentHouseValue, rob(i + 1) )

'''


class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [-1 for _ in range(len(nums))]
        
        return self.rob_rec(dp, nums, 0)
        
        
        
    def rob_rec(self, dp, nums, index):
        
        # Base Case
        if index >= len(nums):
            return 0
        
        if dp[index] != -1:
            return dp[index]
        
        
        choose = nums[index] + self.rob_rec(dp, nums, index + 2)
        dontChoose = self.rob_rec(dp, nums, index + 1)
        
        dp[index] = max(choose, dontChoose)
        return dp[index]

    
'''
# Brute Force

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        return self.rob_rec(nums, 0)
        
        
        
    def rob_rec(self, nums, index):
        
        # Base Case
        if index >= len(nums):
            return 0
        
        
        choose = nums[index] + self.rob_rec(nums, index + 2)
        dontChoose = self.rob_rec(nums, index + 1)
        
        return max(choose, dontChoose)
        
'''
        
        
