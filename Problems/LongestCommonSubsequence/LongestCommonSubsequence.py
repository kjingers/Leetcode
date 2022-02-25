'''
Dynamic Programming with "Longest Common Substring" Pattern.

Unlikee "Longest Common Substring", we don't need to keep track of the max substring, since the count doesn't
reset if two characters don't match.

Again, 3 options:
    1. If characters match iterate both and add 1. Return this
    2. Iterate i
    3. Iterate j
    
max chars don't match, return max(c1, c2)
    


Bottom Up:

Recurrence relation

if s1[i - 1] == s2[j - 1]:
    dp[i][j] = 1 + dp[i - 1][j - 1]
else:
    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])




'''

# Bottom Up

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        maxLen = 0
        
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    
                maxLen = max(maxLen, dp[i][j])
                
        #print(dp)      
        #return maxLen
        return dp[len(text1)][len(text2)]
        
        
# Top-Down

'''
from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        return self.solve(text1, text2, 0, 0)
        
    @lru_cache(None)
    def solve(self, s1, s2, i, j):
        
        if i >= len(s1) or j >= len(s2):
            return 0
        
        c1 = 0
        if s1[i] == s2[j]:
            return 1 + self.solve(s1, s2, i + 1, j + 1)
            
        c1 = self.solve(s1, s2, i + 1, j)
        c2 = self.solve(s1, s2, i, j + 1)
        
        return max(c1, c2)
'''
            
        
        
        
        
