'''
DP Top Down:

We only need to store dp[prev_index]. If you use dp[prev][current], for a given dp[prev][i], the max value will
always be at dp[prev][prev]. The subsequence either stays the same or increases.

So, dp[i] is the max increasing subsequence that starts at i


Bottom Up

if num[i] > num[j] => dp[i] = dp[j] + 1 if there is no bigger LIS for 'i'

For each index, calculate the LIS for all indexes before

Binary Search - Fastest Method

Not sure how I would ever come up with this. keep a dp array. For each num, seach dp array for number that is next largest, and replace it. If num would be the largest number, then append to end. The length of dp array at end is the longest increasing subsequence.

'''

# Binary Search

import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        
        for num in nums:
            idx = bisect_left(dp, num)
            
            if idx == len(dp):
                dp.append(num)
            else:
                dp[idx] = num
                
        return len(dp)
        

# Bottom Up
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        # Initialize to 1, since all substrings are length 1 by themselves
        dp = [1 for _ in range(n)]
        maxLen = 1
        
        
        for i in range(1, n):
            for j in range(i):
                    
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    maxLen = max(maxLen, dp[i])
                    
                    
        return maxLen
'''


'''
# Top Down (TLE)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [-1 for _ in range(len(nums) + 1)]
        #return self.solve(nums, -1, 0, dp)
        
        self.solve(nums, -1, 0, dp)
        print(dp)
        return dp[0]
        
    def solve(self, nums, prevIndex, currIndex, dp):
        
        if currIndex >= len(nums):
            return 0
        
        if dp[prevIndex + 1] != -1:
            return dp[prevIndex + 1]
        
        # Try taking
        c1 = 0
        if prevIndex == -1 or nums[currIndex] > nums[prevIndex]:
            c1 = 1 + self.solve(nums, currIndex, currIndex + 1, dp)
            
        # Try skipping
        c2 = self.solve(nums, prevIndex, currIndex + 1, dp)
        
        dp[prevIndex + 1] = max(c1, c2)
        return dp[prevIndex + 1]
'''
                    
    
