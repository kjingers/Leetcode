'''

Top-Down DP: 

Looks similar to other Fibonocci programs: staircase, unique paths, etc

At each index, we try all jump lengths from 1 to nums[index]

Top Down w/ Memoization Time Complexity: O(n^2) (causes TLE)

Option 2 - keeping track of Max position so far at each index:

Time Complexity: O(n)




'''

# Max Position so Far
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        maxPos = 0
        i = 0
        n = len(nums)
        
        while i <= maxPos:
            
            # Update max position we can get jumping from 0 to i
            maxPos = max(maxPos, i + nums[i])
            
            # If our max position is last index or beyond, return True
            if maxPos >= n - 1:
                return True
            
            i += 1
        
        # If we exit loop, then our maxPos could not keep moving forward
        # ie. We hit a 0, and could not move past 0 at any previous jumps
        return False
        
        
        
        
        
        
# Top-Down DP (TLE)
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [-1 for _ in range(len(nums))]
        return self.canJump_rec(dp, nums, 0)
        
    def canJump_rec(self, dp, nums, index):
        
        # Base Case
        if index == len(nums) - 1:
            return True
        
        if dp[index] != -1:
            return dp[index]
        
        res = False
        
        
        
        for i in range(1, nums[index] + 1):
            
            
            if i > len(nums) - index - 1:
                break
            
            res = self.canJump_rec(dp, nums, index + i)
            
            if res:
                break
        
        dp[index] = res
        return res
        
'''
        
