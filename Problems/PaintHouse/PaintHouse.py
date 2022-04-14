'''
[red, blue, green]

Naive: Try all combinations and return the minimum cost of all options. Like staircase problem (with cost)
Time: O(2^n). At each house, we can make two decisions

Top-Down:

dp[index][color] is the minimum cost at index when paited with color
'''

# Bottom Up Constant Space
# Since we can see in our recurrence relation, we only use 2 values from the previous index
# Can store these in variable: prev, prevB, prevG

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = costs[0]
        
        # dp[0] = Red, dp[1] = Blue, dp[2] = Green

        
        for i in range(1, len(costs)):
            prevCosts = list(dp)
            print(prevCosts)
            dp[0] = costs[i][0] + min(prevCosts[1], prevCosts[2])
            dp[1] = costs[i][1] + min(prevCosts[0], prevCosts[2])
            dp[2] = costs[i][2] + min(prevCosts[0], prevCosts[1])

            
        return min(dp)

# Bottom Up
# Again, dp[index][color] is minimum cost of painting house at index with color color
# Recurrence Relation: dp[i][c] = cost[i][c] + min(dp[i-1][c + 1 % 3], dp[i-1][c + 2 % 3])
'''
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = [[-1 for _ in range(3)] for _ in range(len(costs))]
        
        for i in range(3):
            dp[0][i] = costs[0][i]          
        
        for i in range(1, len(costs)):
            for j in range(3):
                dp[i][j] = costs[i][j] + min(dp[i-1][(j + 1) % 3], dp[i - 1][(j + 2) % 3])
                
        return min(dp[-1])
        
        
'''

# Top Down
'''
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        dp = [[-1 for _ in range(3)] for _ in range(len(costs))]
        cost = self.helper(costs, 0, -1, dp)
        print(dp)
        return cost
        
    def helper(self, costs, index, prev, dp):
        
        if index == len(costs):
            return 0

        minCost = math.inf
        
        
        for colorIndex in range(3):
            if colorIndex == prev:
                continue
            
            if dp[index][colorIndex] != -1:
                cost = dp[index][colorIndex]
            else:
                dp[index][colorIndex] = costs[index][colorIndex] + self.helper(costs, index + 1, colorIndex, dp)
                cost = dp[index][colorIndex]

            minCost = min(minCost, cost)
         
        return minCost
'''
        
        
            
        
