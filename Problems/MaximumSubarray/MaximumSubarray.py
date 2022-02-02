# Brute force: For each index i, calculate the subarray sum for all subarrays starting at index i
# Update Max if needed for each

# Better approach to figure out how to use rolling sum to decide whether to add previous sum or not
# 
# For each num, we can either:
# - Add Num[i] to previous sum if sum > 0
# - Make Sum = Num[i]
# 
# This works, because if previous sum is negative, it can't help us get a larger subarray sum, so start over.
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = nums[0]
        maxSum = nums[0]
        
        for i in range(1, len(nums)):
            
            if sum > 0:
                sum += nums[i]
            else:
                sum = nums[i]
            maxSum = max(maxSum, sum)
        
        return maxSum
        
