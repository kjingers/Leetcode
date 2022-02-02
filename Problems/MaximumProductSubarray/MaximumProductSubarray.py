'''
If the array just had positive numbers, then we could solve very similar to "maximum subarray sum", 
where at each index, we either multiply the current number with the previous max product, or make the current
index the max product (create a new subarray starting from current index.)

However, since we can have negative numbers, we need to keep track of both the max and min subarray products.
We keep track of the minimum, since if its a negative number and our current index is negative, this product
would be greater than current index * max product (which would be come negative.)

So, at each index we have to calculate:
- previousMaxProd * nums[i]
- previousMinProd * nums[i] (If prevMin and nums[i] are both negative, this will become are new max)
- nums[i]

Once we have these 3 values, we need to:
- Store the max of these 3 values into previousMaxProduct
- Store the min of these 3 values into previousMinProduct
- 
'''


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        prevMax = nums[0]
        prevMin = nums[0]
        result = nums[0]
        
        
        for i in range(1, len(nums)):
            a = prevMin * nums[i]
            b = prevMax * nums[i]
            prevMax = max(a, b, nums[i])
            prevMin = min(a, b, nums[i])
            result = max(result, prevMax)
        return result
            
        
