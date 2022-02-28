'''
Unbounded Knapsack. Instead of finding the minimum number of coins, we want the total number of ways
to reach amount.

Top Down w/ Memoizatiion:

We have two choices:

    1. if amount >= coins[i], then we can pick the coin
    2. We can skip the coin
    
dp[i][amnt] = sum of these two values
dp[i][amnt] represents the number of ways to get amnt with indexes up to i


Bottom Up

dp[i][0] = 1, since only 1 way to get a total of 0 (not picking anything)

dp[i][amnt] = dp[i - 1][amnt] + dp[i][amnt - coins[i]]

Can optimize space using dp[amount], which contains amount of ways for each amount
dp[amnt] = dp[amnt - coin] for coin in coins


'''

# Bottom up
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)
        dp = [[0 for _ in range(amount + 1)] for _ in range(n)]
        
        # 1 way to get amount of 0
        for i in range(n):
            dp[i][0] = 1
            
        for i in range(n):
            for j in range(1, amount + 1):
                if j >= coins[i]:
                    dp[i][j] = dp[i][j - coins[i]]
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                    
                
        return dp[n - 1][amount]
        

'''
# Top Down w/ Memoization
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)
        dp = [[-1 for _ in range(amount + 1)] for _ in range(n)]
        
        return self.solve(coins, amount, 0, dp)
        
    def solve(self, coins, amount, index, dp):
        
        # Base case
        if index == len(coins):
            return 0
        
        if dp[index][amount] != -1:
            return dp[index][amount]
        
        if amount == 0:
            dp[index][amount] = 1
            return dp[index][amount]
        
        c1 = 0
        # Take the coin
        if coins[index] <= amount:
            c1 = self.solve(coins, amount - coins[index], index, dp)
            
        # Don't take the coin
        c2 = self.solve(coins, amount, index + 1, dp)
        
        dp[index][amount] = c1 + c2
        
        return dp[index][amount]
        
'''
            
        
        
        
        
        
