'''
At each step, we have two decisions:
1. Take 1 step
2. Take 2 steps

The number of ways from each step is always the same regardless of previous steps.
So, we can store step # and ways into a dictionary.
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.climb_rec(n, memo)
        
    def climb_rec(self, n, memo):
        
        # Base Case: If n == 0, then we are at the top step.
        # So, return 1 since it's a valid way to get to top step
        if n == 0:
            return 1
        elif n in memo:
            return memo[n]
        
        
        
        ways = 0
        
        # Loop 1 to m+1 (m = 2). Only call if # steps is <= n, so that we don't overshoot the top step
        # Use loop to generalize for m steps
        for i in range(1, 3):
            if i <= n:
                ways += self.climb_rec(n - i, memo)
                
        memo[n] = ways
        return ways
                
        
        
        
