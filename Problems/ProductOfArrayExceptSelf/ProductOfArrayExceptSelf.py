'''
Brute Force would be for each index, multiply the numbers at all other index.
Time Complexity: O(n^2)

This improve this, how can we store information as we calculate the product of numbers? Sliding window


We can do 2 passes of the array:
1. Left to right - For each index, calculate the product of all nums to the left
2. Right to left - For each index, calculate the product of all nums to the right
With these two arrays, we can multiply the numbers at each index in both arrays together to get
the sum of all numbers in array except self.

Time Complexity: O(n)
Space Complexity: O(n)
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Initialize arrays to ones
        leftProduct = [1] * len(nums)
        rightProduct = [1] * len(nums)
        output = [1] * len(nums)
        
        # Calculate product of all nums to left of each index
        prod = 1
        for i in range(1, len(nums)):
            prod *= nums[i - 1]
            leftProduct[i] = prod
        
        prod = 1
        # Calculate product of all nums to right of each index
        for i in range(len(nums) - 2, -1, -1):
            prod *= nums[i + 1]
            rightProduct[i] = prod
            
        # Multiply leftProduct with rightProduct to get product of all elements except self
        # at each index.
        for i in range(len(nums)):
            output[i] = leftProduct[i] * rightProduct[i]
        
        return output
            
            
            
        
        
        
