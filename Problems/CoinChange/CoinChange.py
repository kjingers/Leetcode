'''
Unbounded Knapsack problem. Cannot use greedy, since picking the largest coin possible won't always give
the correct answer.

Top Down w/ memoization:

At each index and total, we can either:
    1. If total - coins[i] >= 0, we can pick that coin and recursively call at the same index
    2. Skip the current coin, and recursively call for all remaining coins
    
The minimum of the above two options is the minimum result to store in dp[i][T]

** NOTE: Base case should return 0. We add one after recursive call (if successful).
** Default c1 and fail case to inf, so we don't pic kthat for the min.

Bottom up:

dp[index][total] - Represents the Minimum number of coins needed to make total, using all coins up to index 'index'

dp[index][total] = min(dp[index - 1][total], 1 + dp[index][total - coin[index]])
    ** Must check if index > 0, and if total >= coins[i]

dp[index][0] = 0 for all indexes, because 0 coins required to make total of 0

Space Optimization:

Instead of a 2D array, we can have dp[amount]. Our outer loop loops through the amounts. For each amount ,we loop through all the coins, and pick the min of dp[amount - coin] if coin >= amount
'''

import math

# Bottom-up
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)
        
        # Initialize to math.inf, since we want the minimum
        dp = [[math.inf for _ in range(amount + 1)] for _ in range(n)]
        
        # For call indexes, takes 0 coins to get total of 0
        for i in range(n):
            dp[i][0] = 0
            
            
        for i in range(n):
            for tot in range(1, amount + 1):
                
                # Skip ith coin
                if i > 0:
                    dp[i][tot] = dp[i - 1][tot]
                
                # Take ith coin
                if coins[i] <= tot:
                    dp[i][tot] = min(dp[i][tot], 1 + dp[i][tot - coins[i]])
                    
                       
        return dp[n - 1][amount] if dp[n - 1][amount] != math.inf else -1
                              


# Top Down w/ Memoization
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[-1 for _ in range(amount + 1)] for _ in range(len(coins))]
        res = self.solve(coins, 0, amount, dp)
        
        return -1 if res == float('inf') else res
        
    def solve(self, coins, index, total, dp):
        
        # Base cases
        if index == len(coins):
            return float('inf')
        
        if dp[index][total] != -1:
            return dp[index][total]
        
        if total == 0:
            return 0
        
        c1 = float('inf')
        
        # Try picking the coin
        if total - coins[index] >= 0:
            c1 = self.solve(coins, index, total - coins[index], dp)
            
            if c1 != float('inf'):
                c1 += 1
         
        # Try skipping the coin
        c2 = self.solve(coins, index + 1, total, dp)
        
        # Return the minimum for the two options
        dp[index][total] = min(c1, c2)
        return dp[index][total]
            
'''
        
        
