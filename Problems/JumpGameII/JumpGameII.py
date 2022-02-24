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
