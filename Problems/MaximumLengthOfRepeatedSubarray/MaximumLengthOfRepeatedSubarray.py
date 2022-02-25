'''
Brute Force solution:

The tricky part for this problem, is that we need to keep track of the MAX length as we solve. So,
for top-down, we either need a global variable that we update each time, or pass in "count" to the function,
that contains the length of the preceding matched string.

Start from the beginning of each string. At each state, we have 3 options:
    1. If characters match from both strings, add one and recursively call with both indices incremented
    2. Can iterate just the index in the first string
    3. Can iterate just the intex in the second string
    
We either need to pass count to each function, or have a global variable that we update each time.

Top down DP. 2-D array to memoize dp[i][j] state
 dp[i][j] contains the common substring starting from nums1[i] and nums2[j]
 
 
 Bottom-up Solution:
 
 Recursive Formula:
 
if s1[i] == s2[j] 
  dp[i][j] = 1 + dp[i-1][j-1]
else 
  dp[i][j] = 0 
  
 
'''

# Bottom-up DP

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        dp = [[0 for _ in range(len(nums2) + 1)] for _ in range(len(nums1) + 1)]
        maxLen = 0
        
        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    maxLen = max(maxLen, dp[i][j])
                    
        
        return maxLen
            

# Brute Force - Top-down DP (TLE)
'''
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        self.ans = 0
        dp = [[-1 for _ in range(len(nums2))] for _ in range(len(nums1))]
        

        self.solve(nums1, nums2, 0, 0, dp)

        return self.ans
        
    def solve(self, nums1, nums2, i, j, dp):
        
        if i == len(nums1) or j == len(nums2):
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        count = 0
        # If characters match
        if nums1[i] == nums2[j]:
            count = 1 + self.solve(nums1, nums2, i + 1, j + 1, dp)
            
        c1 = self.solve(nums1, nums2, i + 1, j, dp)
        c2 = self.solve(nums1, nums2, i, j + 1, dp)
        
        dp[i][j] = count
        
        self.ans = max(self.ans, dp[i][j])
        return dp[i][j]
'''
        
