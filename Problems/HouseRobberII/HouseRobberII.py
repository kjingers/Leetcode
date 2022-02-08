'''
Only difference from original House Robber problem, is that we cannot rob both the first and lat house.

We can solve using the same algorithm, where we solve twice:
1. rob(nums[0:len(nums) - 1])
2. rob(nums[1:len(nums)])

The max of these two is the overall max
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # Only one house
        if len(nums) == 1:
            return nums[0]
        
        dp1 = [-1 for _ in range(len(nums) + 1)]
        dp2 = [-1 for _ in range(len(nums) + 1)]
               
        skipFirst = self.rob_rec(dp1, nums[1:], 0)
        pickFirst = self.rob_rec(dp2, nums[0:len(nums) - 1], 0)
        
        
        return max(skipFirst, pickFirst)
        
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
    
        
