'''
Brute force DP can achieve O(n^2) time complexity (Outside for-loop with inner for loop for each jump 1 to nums[i])

Greedy approach is to, starting at spot i = 0, see whih jump is the largest
    - Begin with left = 0, right = nums[0]
    - Loop until left >= n - 1
    - In the loop, left = right, and right = max(i + nums[i] for i in range(left, right + 1))
    - Each loop, we iterate the number of steps
    
Time Complexity: O(n)
Space: O(1)
'''

# Greedy

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        if n <= 1:
            return 0
        
        left, right = 0, nums[0]
        numJumps = 1
        
        # While before the last index
        while right < n - 1:
            maxJump = max([i + nums[i] for i in range(left, right + 1)])
            left = right + 1
            right = maxJump
            numJumps += 1
            
        return numJumps


# Top-Down DP
# dp[i] is the minimum number of jumps to each the end from index i
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [10001 for i in range(len(nums))]
        return self.jump_rec(nums, 0, dp)
        
        
    def jump_rec(self, nums, pos, dp):
        
        # Base Case
        if pos >= len(nums) - 1:
            return 0
        
        if dp[pos] != 10001:
            return dp[pos]
        
        for j in range(1, nums[pos] + 1):
            dp[pos] = min(dp[pos], 1 + self.jump_rec(nums, pos + j, dp))
            
        return dp[pos]
'''
# Bottom-up DP
# dp[n - 1] = 0
# Then loop backwards from n - 2 to 0.
# For each i, Iterate j from 1 to nums[i]
#   dp[i] = min(dp[i], 1 + dp[i + j])
#   **Bounds handling, so we don't check beyond last index**
#        dp[i] = min(dp[i], 1 + dp[min(i + j, n - 1)]
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        dp = [10001 for i in range(n)]
        dp[n - 1] = 0
        for i in range(n - 2, -1, -1):
            for j in range(1, nums[i] + 1):
                dp[i] = min(dp[i], 1 + dp[min(i + j, n - 1)])
                
        return dp[0]
        
'''
        
        
        
        
        
        
        
        
        
