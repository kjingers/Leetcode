'''
We can traverse the list. For each num, we have two options:
1. If num[i] > num[i-1], then we add num to curent subsequence and recursively solve the rest
2. We recursively solve the rest without adding current num

Since previousIndex can be -1, we will always store [previousIndex + 1] into array

Alternative faster approach is to populate an array to keep track of the smallest values at 
each subsequence length. For each num, we binary search our array, and replace the next larger number.
If num is larger than all numbers in our array, we append to the end of the array. The length of the array
at the end is the longest subsequence.

Time Complexity: O(nlog(n))

'''

import bisect

class Solution:
    
    def lengthOfLIS(self, nums):
        
        dp = []
        
        for i in range(len(nums)):
            
            index = bisect_left(dp, nums[i])
            
            if index == len(dp):
                dp.append(nums[i])
            else:
                dp[index] = nums[i]
                
        return len(dp)

    
    
'''
# Brute Force -> DP Solution.
# TLE with Time Complexity: O(n^2)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        #dp = [[-1 for _ in range(len(nums) + 1)] for _ in range(len(nums))]
        dp = [-1 for _ in range(len(nums) + 1)]
        #dp = {}
        
        return self.lengthOfLIS_rec(dp, nums, -1, 0)
        
    def lengthOfLIS_rec(self, dp, nums, previousIndex, currentIndex):
        
        # Base Case
        if currentIndex == len(nums):
            return 0
        
        #if dp[currentIndex][previousIndex + 1] != -1:
        #    return dp[currentIndex][previousIndex + 1]
        
        if dp[previousIndex + 1] != -1:
            return dp[previousIndex + 1]
        
        #if (currentIndex, previousIndex) in dp:
        #    return dp[(currentIndex, previousIndex)]
        
        
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
        
        #dp[(currentIndex, previousIndex)] = max(c1, c2)
        #return dp[(currentIndex, previousIndex)]
        
'''
        
        
