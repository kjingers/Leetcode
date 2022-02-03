'''
Unbounded Knapsack problem, since we can use unlimited of each item.
So at each index we have two options:
1. Pick the current coin and recursively solve remaining total with same index
2. Do not pick current coin and recursively solve remaining total with next index

Can use memo with tuple as key.
Or use 2D array: dp[# coins][total]
'''
import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [[-1 for _ in range(amount + 1)] for _ in range(len(coins))]
        result = self.coinChange_rec(coins, amount, 0, dp)
        
        return -1 if result == math.inf else result
        
    
    def coinChange_rec(self, coins, amount, index, dp):
        
        # Base Cases:
        
        # If amount == 0, then the coins we picked satisfy the total
        if amount == 0:
            return 0
        
        # If we have no more coins, then there is not a possible solution with this decision.
        if index >= len(coins):
            return math.inf
        
        
        if dp[index][amount] != -1:
            return dp[index][amount]
        
        count1 = math.inf
        
        if coins[index] <= amount:
            res = self.coinChange_rec(coins, amount - coins[index], index, dp)
            
            if res != math.inf:
                count1 = res + 1
        
        count2 = self.coinChange_rec(coins, amount, index + 1, dp)
        
        dp[index][amount] = min(count1, count2)
        return dp[index][amount]
            
        
