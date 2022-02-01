'''
We can take 1 to m steps. So, we call recursively with n-1, n-2, ... n-m steps remaining
- Base case: 0 steps remaining. Return 1 for a valid way
- Only call recursively if i is <= n. This avoids over jumping the end
'''

# Brute Force Method
# Time Complexity O(M^N)

def staircase(n, m):

  # Base Case:
  if n == 0:
    return 1

  ways = 0

  # If m = 2, then we can take either 1 or 2 steps
  # So we add all the ways after taking 1 step + after taking 2 steps
  # So, we call recursively with n-1 steps and n-2 steps remaining

  # ways = staircase(n-1, m) + staircase(n-2, m)

  # To generalize for 1 to m steps:
  for i in range(1, m+1):

    # This is how we prevent going past the top step
    if i <= n:
      ways += staircase(n-i, m)

  return ways

# DP with Memoization
# Time Complexity: O(M*N)

def nthStair(n, m, memo):
  
  # base case of when there is no stair
  if n == 0:    
    return 1
  
  # before recursive step check if result is memoized
  if n in memo: 
    return memo[n]
  
  ways = 0
  # iterate over number of steps, we can take
  for i in range(1,m+1):    
    
    # if steps remaining is smaller than the jump step, skip 
    if i <= n:           
      
      #recursive call with n i units lesser where i is the number of steps taken here   
      ways += nthStair(n-i, m, memo) 
      
  # memoize result before returning
  memo[n] = ways   
  return ways

def staircase(n, m):
  memo = {}
  # helper function to add memo dictionary to function
  return nthStair(n, m, memo) 

print(staircase(100, 6))

'''
Leetcode (m=2)
'''
'''
Similar to fibinocci. From each step, we calculate the ways after taking 1 step and 2 steps.
Time Complexity: With memoization, O(2n) = O(n)

'''

class Solution:
    def nStairsRemaining(self, n, memo):
        
        # Base Case: If n < 0, then not a valid way
        # If n == 0, then a valid way
        if n < 0:
            return 0
        elif n == 0:
            return 1
        elif n in memo:
            return memo[n]
        
        # Calculate ways recursively with 1 fewer step and 2 fewer steps
        # Add to memo
        memo[n] = self.nStairsRemaining(n-1, memo) + self.nStairsRemaining(n-2, memo)
        return memo[n]
    
        
        
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.nStairsRemaining(n, memo)



