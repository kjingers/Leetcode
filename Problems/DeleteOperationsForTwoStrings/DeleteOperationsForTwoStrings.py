'''
Can calculate the longest common subsequence. Then, we can calculate the total number of deletions by
the number of deletions needed to make word1 == LCS and word2 == LCS.


Recurrence Relation

if s1[i - 1] == s2[j - 1]:
    dp[i][j] = 1 + dp[i - 1][j - 1]
else:
    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
'''

# Bottom-Up DP
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n1 = len(word1)
        n2 = len(word2)
        
        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    
                    
        lcs = dp[n1][n2]
        
        return n1 - lcs + n2 - lcs
              
              
        
