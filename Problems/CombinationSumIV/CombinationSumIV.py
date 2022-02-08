'''
The problem looks similar to staircase problem. Except, instead of 1 to m steps, our "steps" can be 
any num in nums.

Top Down: Start with target = target, and recursively solve by picking each num. 

Time Complexity: O(n) where n is target

Can reduce space compelxity by using bottom-up. We won't have large recursion stack.
'''


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = [-1 for _ in range(target + 1)]
        return self.combinationSum4_rec(dp, nums, target)
        
    
    def combinationSum4_rec(self, dp, nums, target):
        
        # Base case. If target == 0, we have a valid combination
        if target == 0:
            return 1
        
        if dp[target] != -1:
            return dp[target]
        
        res = 0
        
        for num in nums:
            
            # We cannot pick this num since > than target
            if num > target:
                continue
                
            res += self.combinationSum4_rec(dp, nums, target - num)
            
        dp[target] = res
        return res

    
'''
# Brute Force
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        return self.combinationSum4_rec(nums, target)
        
    
    def combinationSum4_rec(self, nums, target):
        
        # Base case. If target == 0, we have a valid combination
        if target == 0:
            return 1
        
        res = 0
        
        for num in nums:
            
            # We cannot pick this num since > than target
            if num > target:
                continue
                
            res += self.combinationSum4_rec(nums, target - num)
            
        return res
                
'''
