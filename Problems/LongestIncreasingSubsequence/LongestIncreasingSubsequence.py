'''
We can traverse the list. For each num, we have two options:
1. If num[i] > num[i-1], then we add num to curent subsequence and recursively solve the rest
2. We recursively solve the rest without adding current num

Since previousIndex can be -1, we will always store [previousIndex + 1] into array
DP solution is O(n^2) and times out in Leetcode

A better less straightforward solution is to use binary search to populate an array

https://leetcode.com/problems/longest-increasing-subsequence/discuss/1326552/Optimization-From-Brute-Force-to-Dynamic-Programming-Explained!

'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        #dp = [[-1 for _ in range(len(nums) + 1)] for _ in range(len(nums))]
        dp = [-1 for _ in range(len(nums) + 1)]
        
        return self.lengthOfLIS_rec(dp, nums, -1, 0)
        
    def lengthOfLIS_rec(self, dp, nums, previousIndex, currentIndex):
        
        # Base Case
        if currentIndex == len(nums):
            return 0
        
        #if dp[currentIndex][previousIndex + 1] != -1:
        #    return dp[currentIndex][previousIndex + 1]
        
        if dp[previousIndex + 1] != -1:
            return dp[previousIndex + 1]
    
        
        
        c1 = 0
        
        # 1. Including current number
        if previousIndex == -1 or nums[currentIndex] > nums[previousIndex]:
            c1 = 1 + self.lengthOfLIS_rec(dp, nums, currentIndex, currentIndex + 1)
            
        # 2. Skipping current index. 
        c2 = self.lengthOfLIS_rec(dp, nums, previousIndex, currentIndex + 1)
        
        #dp[currentIndex][previousIndex + 1] = max(c1, c2)
        #return dp[currentIndex][previousIndex + 1]
        
        dp[previousIndex + 1] = max(c1, c2)
        return dp[previousIndex + 1]
        
        
        
