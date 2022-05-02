'''
"Maximum" makes me consider DP
Using subarrays could be sliding window

Min-Product is minimum_value * subarray_sum, so prefix_sum could be useful

For each index i, we get all subarrays where nums[i] is the minimum
    - next smallest to the left
    - next smallest to the right
    
Almost exactly same is "Largest Rectange in Histogram." Here, the width is the prefix sum from i to . Height is the peak value we are considering.
    - Since everything we are popping is larger than our current value, we can think of the popped values as our "last-change" to calculate subarrays with them as min-value.
'''

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        
        # Handle Boundary Conditions
        stack = deque([-1])
        nums.append(0)
        ans = 0
        
        
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                # We now have smaller val to left and smaller val to the right
                # Want prefix sum EXCLUDING those prev and next smaller vals, because
                # we want to calculate for all subarrays where popped val is the minimum
                min_index = stack.pop() 
                min_val = nums[min_index] 
                prev_smaller_index = stack[-1] 
                psum = prefix_sum[i] - prefix_sum[prev_smaller_index + 1] # Non-inclusive
                ans = max(ans, psum * min_val)
            stack.append(i)
            
        return ans % (10**9 + 7)
                
                
                
                
                
        
