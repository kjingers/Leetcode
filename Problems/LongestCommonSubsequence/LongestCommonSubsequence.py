'''
Brute Force strategy is to recursively compare both string index by index.

For an index i and index j:
- If they text1[i] == text[j], then add 1 and recursively call with i+1 and j+1. Return result
- Else, make two recursive calls for (i+1, j) and (i, j+1) and return the max

The longest substring or a given i and j is always the same. This calculation will be done many
times using the brute force method. So, we can memoize the resuults for a given i and j.

Memoized Time Complexity: O(mn)

'''


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # dp[index1][index2]
        dp = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        
        return self.LCS_rec(dp, text1, text2, 0, 0)
        
        
    def LCS_rec(self, dp, text1, text2, i, j):
        
        # Base case: One of the indicies is past the length of the string
        if i == len(text1) or j == len(text2):
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        # If the are the same, then increment both pointers and return
        # 1 + (longest subsequence of remaining substrings)
        if text1[i] == text2[j]:
            dp[i][j] = 1 + self.LCS_rec(dp, text1, text2, i + 1, j + 1)
            return dp[i][j]
        
        c1 = self.LCS_rec(dp, text1, text2, i + 1, j)
        c2 = self.LCS_rec(dp, text1, text2, i, j + 1)
        
        dp[i][j] = max(c1, c2)
        return dp[i][j]
    
    
'''
# Brute Force Method

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        return self.LCS_rec(text1, text2, 0, 0)
        
        
    def LCS_rec(self, text1, text2, i, j):
        
        # Base case: One of the indicies is past the length of the string
        if i == len(text1) or j == len(text2):
            return 0
        
        # If the are the same, then increment both pointers and return
        # 1 + (longest subsequence of remaining substrings)
        if text1[i] == text2[j]:
            return 1 + self.LCS_rec(text1, text2, i + 1, j + 1)
        
        c1 = self.LCS_rec(text1, text2, i + 1, j)
        c2 = self.LCS_rec(text1, text2, i, j + 1)
        
        return max(c1, c2)
'''
        
        
        
