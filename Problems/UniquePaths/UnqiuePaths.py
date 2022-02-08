'''
Fibonocci Numbers type problem.

At each spot, we can either:
1. Go down if row < m - 1
2. Go right if col < n - 1
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.uniquePaths_rec(dp, m, n, 0, 0)
        
    def uniquePaths_rec(self, dp, m, n, row, col):
        
        # Base Case
        if row == m - 1 and col == n - 1:
            return 1
        
        if dp[row][col] != -1:
            return dp[row][col]
        
        ways = 0
        
        if row < m - 1:
            ways += self.uniquePaths_rec(dp, m, n, row + 1, col)
            
        if col < n - 1:
            ways += self.uniquePaths_rec(dp, m, n, row, col + 1)
         
        dp[row][col] = ways
        return ways
        
        
