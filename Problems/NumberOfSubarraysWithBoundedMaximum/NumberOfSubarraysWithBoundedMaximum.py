'''
Can create function to calculate number of subarrays less than k. Then return:
    - count(right) - count(left - 1)
    
Two Pointer:

Keep track of the last index where:
    - R_i = i if nums[i] > Right
    - L_i = i if nums[i] >= Left
    
Then, at each index i, the number of subarrays with bounded maximum is R_i - L_i.
The sum of all these is the answer.

Another more DP way of looking at it, where dp[i] is the number of subarrays ending at i:
    - If nums[i] < L: Then we can only append nums[i] to a valid subarray. 
        - dp[i] = dp[i - 1]
    - If nums[i] > R: Then we can't have this element in any subarray. But we should also mark this index with prev.
        - dp[i] = 0, prev = i    **prev needs to be used to calculate 3rd case below
    - If left <= nums[i] <= right: Then the number of subarrays ending at i is all subarrays since the prev invalid ind
        - dp[i] = i - prev
        
Sum of all dp[i] is the answer. Since we only use dp[i-1] and prev, we can use constant space.


'''
# DP Solution
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        dp = 0
        prev = -1 # Before array
        ans = 0
        
        for i, num in enumerate(nums):
            
            if num < left and i > 0:
                ans += dp
            elif num > right:
                prev = i
                dp = 0
            elif left <= num <= right:
                dp = i - prev
                ans += dp
        return ans

# Sliding Window With count(bound)
'''
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        return self.count(nums, right) - self.count(nums, left - 1)
        
        
    # Counts the number of subarrays with a max less than "bound"
    def count(self, nums: List[int], bound: int) -> int:
        
        ans = 0
        count = 0
        
        for num in nums:
            count = count + 1 if num <= bound else 0
            ans += count
        
        return ans
'''
    
# Two Pointer Solution - One Pass
# To calculate the total subarrays ending at each index, we need to keep track of last
# index where nums[i] > R and where nums[i] >= L
'''
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        
        R_i = -1
        L_i = -1
        ans = 0
        
        for i, num in enumerate(nums):
            if num >= left:
                L_i = i
            if num > right:
                R_i = i
            ans += L_i - R_i
            
        return ans
        
'''

        
        

            
        
